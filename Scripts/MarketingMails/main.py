from utils import *

if __name__ ==  "__main__":

    takeCommand = True
    history = []
    browser = open_browser()

    while takeCommand:
        print(">>> ", end=" ")
        command = input()
        tokens = command.split()
        history.append(command)

        if tokens[0] == "exit":
            takeCommand = False
        elif tokens[0] == "create":
            company = tokens[1]
            pitch = [tokens[i] for i in range(2,len(tokens))]       
        
            links = make_deliverables(browser, company, pitch)
            create_mail(browser, company, links)
        elif tokens[0] == "verify":
            pass
        elif tokens[0] == "delete":
            company = tokens[1]
            delete_company_folder(company)
        elif tokens[0] == "history":
            print(*history, sep="\n")
        else:
            print(" Wrong Query : " + command )
        

    browser.close()

