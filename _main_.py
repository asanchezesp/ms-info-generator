#Requires:
#   - openpyxl
#   - github

from github_info import GithubInfo
from excel_generator import ExcelGenerator

main_repo_name = '<YOUR-REPO-NAME>'
path_feign_clients = '<YOUR-JAVA-FILES-PATH>'
token = '<YOUR-ACCESS-TOKEN>'
gitInfo = GithubInfo(token,main_repo_name,path_feign_clients).getInfoFromRepo()
excelGenerator = ExcelGenerator(gitInfo)
excelGenerator.generate()