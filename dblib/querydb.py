from databricks import sql
import os


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

def testdb():
    largeCQuery = "SELECT salary_in_usd, company_size FROM default.ds_salaries_csv where work_year="+"2020"+" and employment_type=\'"+"FT"+"\' and job_title=\'"+"Data Scientist"+"\' and experience_level=\'"+"SE"+"\' and company_size=\'L\'"
    largeResult = querydb(largeCQuery)
    print(type(largeResult))


## 
def selectSalary(salary="70000", year="2020"):
    #sqlquery = "SELECT experience, job_title, company_location, company_size FROM default.ds_salaries_csv where work_year=" + year +" and salary_currency=" + currency + " and salary=" + salary;
    sqlquery = "SELECT experience_level, job_title, company_location, company_size FROM default.ds_salaries_csv where work_year=" + year + " and salary=" + salary;
    print(sqlquery)
    res = querydb(sqlquery)
    print(type(res))

if __name__ == "__main__":
    testdb()
    #selectSalary()