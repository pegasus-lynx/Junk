def convert(file_name):
    data = []
    row = []

    with open(file_name, 'r') as file:
        for cnt, line in enumerate(file):
            # print(line)

            flag=True
            if len(line)<5:
                data.append(row)
                row = []
                flag=False
                
            if flag:
                row.append(line.split())

    return data
        
        