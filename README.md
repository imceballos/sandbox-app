## Sandbox APP

### Usage:

docker-compose -f docker-compose.yml build

docker-compose -f docker-compose.yml up

### Introduction:

This is the introduction section for the Balance challenge, there is required to develop a App to expose data stored into PostgresSQL, to execute the queries will be used GraphQL methodologies.

### Developer Notes:

The application uses Flask as a main Framework, the app is organized into multiples modules, there are:
- routes: Contains the endpoints according to the path separated by Blueprint to organize endpoints that be imported to the main module.

- business: Core of the business, includes methods called by endpoints, validators.

- Models: SQLAlchemy modules, with the models, that define the table schema, columns fields and types. Database schemas are defined by the classes into the models module, there are defined with SQLAlchemy. Then are created two schemas: accounts and transactions.

### Architecture: 
The main application contains a Dockerfile and a docker-compose manifest, this is a containerized app, launch a PostgresSQL Database into the port 5432, the database exsits, but is empty, then to create the table schemas is required the entrypoint.sh file, that executes the bash commands: python manage.py, that run the cli command to create the database and seed the DB with Account and Transaction data.


### About the data: 

The merge.dev library does not work to get the Transaction entries via HTTP request, only works with the Account data (by merge.dev), Transaction data was created using Faker library, this is useful to get the data and simulate the final usage. All the scripts  required to get the data from merge.dev (MergeAccountingClient) is contained into main/business.


### Endpoints:
 
To invoke the GraphQL API, please visit the following routes:

Disclaimer (There are not defined the three required endpoints, but these two represents a base case that could be extended)

a) http://localhost:23006/getIncomeExpenseForDate

InputData: query {
  transactionsBetweenDates(accountId: "1", initialDate: "1980-01-01", endDate: "2015-12-31") {
    id
    transactionType
    totalAmount
  }
}



b) http://localhost:23006/getAccountBalanceBreakdown

InputData: query {
  totalBalance(companyId: "1")
}