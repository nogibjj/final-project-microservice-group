from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

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

@app.get("/{year}/{emtype}/{pos}/{level}")
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



# @app.get("/query")
# async def query():
#     """Execute a SQL query"""

#     result = querydb()
#     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")