from github import Github
import re

class GithubInfo:

    def __init__(self,token,main_repo_name,path):
        self.__g = Github(token)
        self.__main_repo_name = main_repo_name
        self.__path = path

    def __get_subrepo_names(self,main_content_repo):
        #Eliminamos los que no son submodulos
        subrepos = [content for content in main_content_repo if self.__main_repo_name not in content.git_url]
        return [content.name for content in subrepos]

    def __get_feign_clients(self,subrepos):
        feign_clients = {}
        for subrepo in subrepos:
            feign_clients[subrepo]=subrepo.get_contents(self.__path)
        return feign_clients

    def __get_clients_info(self,java_files):
        info = {}
        for subrepo,file in java_files.items():
            subrepoClients = {}
            content_decoded = file[0].decoded_content.decode("utf-8");
            #Obtenemos el microservicio al que hace peticiones
            client = re.search(r'name\s*=\s*"([^"]+)"', content_decoded).group(1)
            #Obtenemos los endpoints a los que hace peticiones
            endpoints = re.findall(r'@.*Mapping\(.*\)\n.*;', content_decoded)
            subrepoClients[client] = self.__get_detailed_info(endpoints)
            info[subrepo.name] = subrepoClients
        return info

    def __get_detailed_info(self,enpoints):
        detailed = []
        for request in enpoints:
            info = {}
            method = re.search(r'@(\w+)Mapping',request).group(1).upper()
            requestResult = re.search(r'public\s+(.*?)\s',request).group(1)
            regex = f"{requestResult}\\s+(.*?);"
            requestFunction = re.search(rf'{regex}',request).group(1)
            info['method'] = method
            info['result'] = requestResult
            info['function'] = requestFunction
            detailed.append(info)
        return detailed
    
    def getInfoFromRepo(self):
        # Obtén el repositorio principal
        main_repo = self.__g.get_user().get_repo(self.__main_repo_name)
        #Obtenemos los subrepositorios
        subrepo_names = self.__get_subrepo_names(main_repo.get_contents('.'))
        subrepos = [ self.__g.get_user().get_repo(name)for name in subrepo_names]
        #Obtenemos los ficheros .java del paquete por subrepositorio
        java_files = self.__get_feign_clients(subrepos)
        #Obtenemos la info de cada FeignClient
        result = self.__get_clients_info(java_files)
        return result