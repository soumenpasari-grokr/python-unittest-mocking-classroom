import mysql.connector

class DbHelper:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost',user='root',passwd='root',database='employees')
        self.cursor = self.conn.cursor()

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        query = 'select max(salary) as max_salary from salaries'
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        query = 'select min(salary) as min_salary from salaries'
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]
    
    def max_salary_is_greater_than_min(self):
        max_salary = self.get_maximum_salary()
        min_salary = self.get_minimum_salary()
        if max_salary > min_salary:
            return True
        else:
            return False

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)