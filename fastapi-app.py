from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb
from dblib.querydb import querySalaryofLevels
from dblib.querydb import selectSalary
from dblib.querydb import querySalaryofCountryandTitle
from dblib.querydb import querySalaryByCurrency

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Databricks"}


@app.get("/subt/{num1}/{num2}")
async def subt(num1: int, num2: int):
    """do subtraction"""

    total = num1 - num2
    return {"result": total}


#calculate the average salary in USD in terms of different company size, according to given year, employment type, position and level.
#eg. root/2020/FT/Data%20Scientist/SE
def getResultAvr(queryResult):
    sum = 0
    if len(queryResult) == 0:
        return 0
    for row in queryResult:
        sum+=int(row['salary_in_usd'])
    return round(sum / len(queryResult), 2)


#@app.get("/{year}/{emtype}/{pos}/{level}")
@app.get("/year/{year}/type/{emtype}/pos/{pos}/level/{level}")
async def getSalaryAverageByCsize(year: str, emtype: str, pos:str, level:str):
    largeCQuery = "SELECT salary_in_usd, company_size FROM default.ds_salaries_csv where work_year="+year+" and employment_type=\'"+emtype+"\' and job_title=\'"+pos+"\' and experience_level=\'"+level+"\' and company_size=\'L\'"
    mediumCQuery = "SELECT salary_in_usd, company_size FROM default.ds_salaries_csv where work_year="+year+" and employment_type=\'"+emtype+"\' and job_title=\'"+pos+"\' and experience_level=\'"+level+"\' and company_size=\'M\'"
    smallCQuery = "SELECT salary_in_usd, company_size FROM default.ds_salaries_csv where work_year="+year+" and employment_type=\'"+emtype+"\' and job_title=\'"+pos+"\' and experience_level=\'"+level+"\' and company_size=\'S\'"
    ansdict = {}
    largeResult = querydb(largeCQuery)
    mediumResult = querydb(mediumCQuery)
    smallResult = querydb(smallCQuery)
    ansdict["Average salary of large size company(USD)"] = getResultAvr(largeResult)
    ansdict["Average salary of medium size company(USD)"] = getResultAvr(mediumResult)
    ansdict["Average salary of small size company(USD)"] = getResultAvr(smallResult)
    print(ansdict)
    return ansdict


# query 1:
#   input: job position -- full-time
#   output: the average salary of different levels in this position in the US from 2020-2022
@app.get("/salaryofposition/{position}")
async def getSalaryofPosition(position: str):
    salarylist_Avg = querySalaryofLevels(position)
    ansdict = {}
    ansdict["Average salary of entry level position (USD)"] = salarylist_Avg[0]
    ansdict["Average salary of medium level position (USD)"] = salarylist_Avg[1]
    ansdict["Average salary of senior level position (USD)"] = salarylist_Avg[2]
    return ansdict


# query 2:
#   input: salary and year
#   output: get experience level, job title, company location and company size
@app.get("/salary/{salary}/year/{year}")
async def selectBySalaryAndYear(salary: str, year: str):
    #salarylist_Avg = selectSalary(position)
    res = selectSalary(salary, year)
    return res

# query 3:
#   input: country and position
#   output: average salary of this specific position in this specific country of all levels within the 3 years
@app.get("/country/{country}/position/{position}")
async def queryBycountry_position(country: str, position: str):
    res = querySalaryofCountryandTitle(country, position)
    ansdict = {}
    ansdict["Average salary of the position: " + position + " in the country: " + country + " (USD)"] = res
    return ansdict

#query 4
#input : currency
#output: average salary of the selected currency
@app.get("/currency/{currency}")
async def queryByremote_Currency(currency:str):
    res=querySalaryByCurrency(currency)
    ans={};
    ans["Average salary of the salary currency: "+currency+" is "]=res
    return ans
# @app.get("/query")
# async def query():
#     """Execute a SQL query"""

#     result = querydb()
#     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")