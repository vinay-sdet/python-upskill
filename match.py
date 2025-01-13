def status_codes(statusCode):
    match statusCode:
        case 200:  
            return "OK"
        case 404:
            return "Not Found"
        case 400:
            return "Bad request"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"





statusUser = int(input("Enter Status Code: "))
decodedStatusCode = status_Codes(statusUser)
print(f"You entered status code as {statusUser} which means --> {decodedStatusCode}")