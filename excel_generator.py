from openpyxl import Workbook

class ExcelGenerator:

    __headers = ['Microservice','Method','Path','Request function','Result']
    def __init__(self,values):
        self.__values = values

    def generate(self):
        # Crear un nuevo libro de trabajo (workbook)
        workbook = Workbook()
        #Eliminamos la hoja activa por defecto
        default_sheet = workbook.active
        workbook.remove(default_sheet)

        for k,microservice in self.__values.items():
            sheet = workbook.create_sheet(title=k)
            sheet.append(self.__headers)
            for endpoint,requests in microservice.items():
                for request in requests:
                    row = []
                    row.append(endpoint)
                    row.append(request['method'])
                    row.append(request['path'])
                    row.append(request['function'])
                    row.append(request['result'])
                    sheet.append(row)

        # Guardar el archivo Excel
        workbook.save('microservices.xlsx')    