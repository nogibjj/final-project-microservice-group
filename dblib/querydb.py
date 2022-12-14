from databricks import sql
import os
import json

def querydb(query="SELECT * FROM default.ds_salaries_csv LIMIT 2"):
    #print("here")
    with sql.connect(
        # server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        # http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        # access_token=os.getenv("DATABRICKS_TOKEN"),
        server_hostname="adb-3416579242992940.0.azuredatabricks.net",
        http_path="sql/protocolv1/o/3416579242992940/1208-200836-79mhoxi4",
        access_token="dapif5fa18c3b0b300a50f1ef21ae16859cd-3",
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result



## select according to salary and year, get experience level, job title, company location and company size
def selectSalary(salary="70000", year="2020"):
    #sqlquery = "SELECT experience, job_title, company_location, company_size FROM default.ds_salaries_csv where work_year=" + year +" and salary_currency=" + currency + " and salary=" + salary;
    sqlquery = "SELECT experience_level, job_title, company_location, company_size FROM default.ds_salaries_csv where work_year=" + year + " and salary=" + salary;
    #print(sqlquery)
    res = querydb(sqlquery)
    resdict = []
    count = 0
    for row in res:
        count = count+1
        resdict.append({"experience_level": row[0], 'job_title' : row[1], 'company_location' : row[2], 'company_size' : row[3]})
    
    if count == 0 :
        return {"result" : "null"}
    return resdict

# def getResultAvr(queryResult):
#     sum = 0
#     for row in queryResult:
#         sum+=int(row['salary_in_usd'])
#     return round(sum / len(queryResult), 2)

# def testdb():
#     ansdict = {}
#     largeCQuery = "SELECT salary_in_usd, company_size FROM default.ds_salaries_csv where work_year="+"2020"+" and employment_type=\'"+"FT"+"\' and job_title=\'"+"Data Scientist"+"\' and experience_level=\'"+"SE"+"\' and company_size=\'L\'"
#     largeResult = querydb(largeCQuery)
#     ansdict["Average salary of large size company(USD)"] = getResultAvr(largeResult)
#     print(ansdict)


# query average salary of different levels in one specific position
def querySalaryofLevels(position):
    queryentrylevel = "SELECT salary_in_usd From default.ds_salaries_csv where job_title=\'"+position+"\' and experience_level=\'EN\' and employment_type=\'FT\' and company_location=\'US\';"
    querymediumlevel = "SELECT salary_in_usd From default.ds_salaries_csv where job_title=\'"+position+"\' and experience_level=\'MI\' and employment_type=\'FT\' and company_location=\'US\';"
    queryseniorlevel = "SELECT salary_in_usd From default.ds_salaries_csv where job_title=\'"+position+"\' and experience_level=\'SE\' and employment_type=\'FT\' and company_location=\'US\';"
    entryres = querydb(queryentrylevel)
    mediumres = querydb(querymediumlevel)
    seniorres = querydb(queryseniorlevel)
    entryAvg = calSalaryAvg(entryres)
    mediumAvg = calSalaryAvg(mediumres)
    seniorAvg = calSalaryAvg(seniorres)
    return [entryAvg, mediumAvg, seniorAvg]



def calSalaryAvg(salarylist):
    sum = 0
    for salary in salarylist:
        sum += int(salary["salary_in_usd"])
    return round(sum / len(salarylist), 2)
   


# query average salary of this specific position in this specific country of all levels within the 3 years
def querySalaryofCountryandTitle(country, title):
    querysentence = "SELECT salary_in_usd From default.ds_salaries_csv where employment_type=\'FT\' and job_title=\'"+title+"\' and company_location=\'"+country+"\';"
    queryres = querydb(querysentence)
    average_salary = calSalaryAvg(queryres)
    return average_salary



if __name__ == "__main__":
    selectSalary()
