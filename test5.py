git 基本使用：开源的分布式版本控制系统
官网：https://git-scm.com/
git 仓库的概念
        使用git init 命令将一个目录(可理解为文件夹)初始化为一个仓库，即git管理的一个项目
        工作区-我们电脑能看到的目录。.git目录外(ll -a可显示所有包含隐藏目录)
        暂存区-stage /index，一般放在.git目录下的index文件，此时仓库变化没有给定一个新的版本号
        版本库 -数据在.git目录下，仓库的变动给定了一个新的版本号
本地操作
        将工作区编辑过的变动提交到暂存区
        git status 查看发生变动的文件
        git add file 将文件或变动过的文件提交到stage
        将stage内容提交到仓库，并生成新的版本号
        git status 查看哪些内容需要提交到仓库
        git commit -m "备注提交操作内容“
git  reflog
git log
git remote -v 产看链接的远程仓库
git branch 产看当前分支
git branch -a 产看所有分支
  \
与远程仓库操作
公共的远程仓库服务器指 github.com

公司、组织或个人服务器一般使用gitlab，比如gitlab.insos.cn
\
远程仓库复制到本地
'''
git clone https://github.com/BGI-shenzhen/fqcheck.git #会在当前目录下将远程仓库复制下来，并建立与这个服务器的 联系。最后可以指定其他路径目录
chmod 755/777 #第一个数字：文件所有者权限；第二个数字：与文件所有者同属一个用户组的其他用户的权限；第三个数字表示其他用户组的权限。读(r=4),写(w=2),执行(x=1)，rwx=7
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 PAT personal access token
^C
zhanghuiyuan@master 18:03:43 ~/test
$ cd ~/test/git_test5/202-
zhanghuiyuan@master 18:05:51 ~/test/git_test5/202-
$ git push
Username for 'https://github.com': ZHY31
Password for 'https://ZHY31@github.com':
        版本库-数据在.git目录下，仓库的变动给定了一个新的版本号
本地操作
        将工作区编辑过的变动提交到暂存区
        git status 查看发生变动的文件
        git add file 将文件或变动过的文件提交到stage
        将stage内容提交到仓库，并生成新的版本号
        git status 查看哪些内容需要提交到仓库
        git commit -m "备注提交操作内容“
gireflog
git log
git remote -v 产看链接的远程仓库
git branch 产看当前分支
git branch -a 产看所有分支
\
与远程仓库操作
公共的远程仓库服务器指 github.com

公司、组织或个人服务器一般使用gitlab，比如gitlab.insos.cn
\
远程仓库复制到本地
'''
git clone https://github.com/BGI-shenzhen/fqcheck.git #会在当前目录下将远程仓库>复制下来，并建立与这个服务器联系。最后可以指定其他路径目录
chmod /777 #第一个数字：文件所有者权限；第二个数字：与文件所有者同属一个用户组的
其他用户的权限；第三个数字表示其他用户组的权限。(r=4),写(w=2),执行(x)，rwx=7
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 PAT personal access token

 git remote set-url origin https://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@github.com/ZHY31/202-.git #将token加到远程库链接，避免同一个库push要都要输入token

