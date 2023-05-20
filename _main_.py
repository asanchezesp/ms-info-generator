from github_info import GithubInfo

main_repo_name = '<YOUR-REPO-NAME>'
path_feign_clients = '<YOUR-JAVA-FILES-PATH>'
token = '<YOUR-ACCESS-TOKEN>'
gitInfo = GithubInfo(token,main_repo_name,path_feign_clients)
print(gitInfo.getInfoFromRepo())
