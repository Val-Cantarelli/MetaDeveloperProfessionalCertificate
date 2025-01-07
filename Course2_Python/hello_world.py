httpsStatus = 404

match httpsStatus:
    case 200 | 201:
        print("Sucess")
    
    case 404:
        print("Not found")