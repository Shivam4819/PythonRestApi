# Python Assignment

This is a Python based project which has basic rest api for different features.


## Tech-Stack
1. Python
2. MongoDb-atlas
3. Postman
4. Vs code

## API

1. addUser: This api add the user's data to the mongodb database and return the code as response

        curl --location --request POST 'http://127.0.0.1:5000/api/users/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "id":4,
            "first_name":"ravi",
            "last_name":"Darakjy",
            "company_name":"Chanay, Jeffrey B Jr",
            "city":"Brighton",
            "state":"MI",
            "zip":48116,
            "email":"josephine_darakjy@darakjy.org",
            "web":"http://www.chanayjeffreyaesq.com/",
            "age":48
        }'

2. getUser: This api fetch all the user's records from the database and send that as response to the postman

        curl --location --request GET 'http://127.0.0.1:5000/api/users/?limit=2'

3. specificUser: This api takes the used id and based on that fetches the specific user's record from the database and send response to the postman

        curl --location --request GET 'http://127.0.0.1:5000/api/users/1'

4. updateUser: This api updates the specific user's data in the database. It search the user based on the id.

        curl --location --request PUT 'http://127.0.0.1:5000/del?id=4' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "first_name":"tttttt",
            "last_name":"vvvvvvv",
            "age":10
        }'

5. deleteUser: This api deletes the user records from the db. It takes the user's id and search for that user

        curl --location --request DELETE 'http://127.0.0.1:5000/del?id=4'

## Database

1. MongoDb atlas is used which is a online mongodb db.
2. Refer to any video for setting the mongodb atlas account  