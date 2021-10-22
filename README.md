"# bookHub" 


## Base url: http://127.0.0.1:8000/

By using the following endpoint, URL is formed by baseurl + endpoint


## Main endpoints

| Endpoint name |  Link  | Method |  Purpose |  
|---------------|--------|--------|----------|
 
|  signup | /signup | POST | For signup into system |  
|  login | /login | POST | For login into system |  
|  logout | /logout | POST | For logout from system |  
|  forget-password | /forget-password | POST | For user |  
|  reset-password  | /reset-password | POST | Active registered users |   
|  user-dashboard | /user-dashboard | GET | signin users |   


##### Sample response list for Whole project:

1. HTTP_201_CREATED
2. HTTP_400_BAD_REQUEST
3. HTTP_401_UNAUTHORIZED
4. HTTP_403_FORBIDDEN
5. HTTP_415_UNSUPPORTED_MEDIA_TYPE
6. HTTP_409_CONFLICT
7. HTTP_404_NOT_FOUND
8. HTTP_204_NO_CONTENT
9. HTTP_500_INTERNAL_SERVER_ERROR
10. HTTP_200_OK

