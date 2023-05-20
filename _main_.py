from github_info import GithubInfo

main_repo_name = 'demo-subrepos-parent'
path_feign_clients = 'src/main/java/es/asanchez/feign'
token = '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'
gitInfo = GithubInfo(token,main_repo_name,path_feign_clients)
print(gitInfo.getInfoFromRepo())
