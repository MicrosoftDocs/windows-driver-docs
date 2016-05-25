# For Writers: WDCML-to-OP migration quick reference
This is a quick reference for the Git commands and links used in WDCML to OP migration.

## Cloning the repo and creating a working branch
| Git command | Description |
|-------------|-------------|
|   `C:\myrepo> git clone https://github.com/Microsoft/windows-driver-docs-pr.git`| Clone the driver docs repo|
| `C:\myrepo\windows-driver-docs-pr [master]> .\.openpublishing.build.ps1 -parameters:targets=serve`|Do a **local** build|
|[http://localhost:8080](http://localhost:8080) |View the **local** build|
|`C:\myrepo\windows-driver-docs-pr [master]> git remote show origin`|See the branches on origin and local|
|`C:\myrepo\windows-driver-docs-pr [master]> git checkout -b working-branch`|Create a **local** working branch|

## **WORKING BRANCH**: Commit changes locally and push them to origin
| Git command | Description |
|-------------|-------------|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git add .`|Capture differences to a unit of change|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git commit -m "New projectname topics from con2md conversion."`|Commit the changes to your **local** repo|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git checkout master`| Move to the master branch|
|`C:\myrepo\windows-driver-docs-pr [master]>git pull origin`|Pull down the latest master changes|
|`C:\myrepo\windows-driver-docs-pr [master]>git checkout working-branch`|Go back over to the working branch|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git merge master`|Add latest master changes to working branch|
| `C:\myrepo\windows-driver-docs-pr [working-branch]> .\.openpublishing.build.ps1 -parameters:targets=serve`|Do a **local** build|
|[http://localhost:8080](http://localhost:8080) |View the **local** build|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git push -u origin working-branch`|Push local changes to **working-branch** on origin|
|[https://msdnstage.redmond.corp.microsoft.com/en-us/windows/hardware/drivers/foldername?branch=working-branch](https://msdnstage.redmond.corp.microsoft.com/en-us/windows/hardware/drivers/foldername?branch=working-branch)|View your working branch on MSDNStage|


## <h2 id="update-master"> **Update MASTER BRANCH**: Merge changes from working branch into master</a>
| Git command | Description |
|-------------|-------------|
|`C:\myrepo\windows-driver-docs-pr [anywhere]> git remote show origin`|See the branches on origin and local|
|`C:\myrepo\windows-driver-docs-pr [anywhere]>git checkout master`|Make sure you're in the **master** branch|
|`C:\myrepo\windows-driver-docs-pr [master]>git pull origin`|Pull down the latest **master** changes from origin|
|`C:\myrepo\windows-driver-docs-pr [master]>git checkout working-branch`|Go over to the **working branch**|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git pull origin`|Pull down the latest **working-branch** changes from origin|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git merge master`|Add latest master changes to working branch|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git checkout master`|Go back to the **master** branch|
|`C:\myrepo\windows-driver-docs-pr [master]>git merge working-branch`|Add latest working branch changes to master|
|`C:\myrepo\windows-driver-docs-pr [master]>git push -u origin master`|Push local changes to **master** on origin|
|[https://msdnstage.redmond.corp.microsoft.com/en-us/windows/hardware/drivers/foldername?branch=master](https://msdnstage.redmond.corp.microsoft.com/en-us/windows/hardware/drivers/foldername?branch=master)|View your master branch on MSDNStage (you may need to explictly specify the master branch - it may think you still want to view working branch content)|


## <h2 id="use-temp">**Use TEMP BRANCH**: Use a temp local branch to make a small change</a>
| Git command | Description |
|-------------|-------------|
|`C:\myrepo\windows-driver-docs-pr [master]> git remote show origin`|See the branches on origin and local|
|`C:\myrepo\windows-driver-docs-pr [master]> git checkout -b temp-branch`|Create a **local** *temporary* working branch|
|`C:\myrepo\windows-driver-docs-pr [temp-branch]> code .`|Open Visual Studio Code|
|***Make your change*** --> such as [running scripts](https://github.com/Microsoft/windows-driver-docs-pr/blob/master/migration-guide/index.md#clean) or [editing the TOC.md](https://github.com/Microsoft/windows-driver-docs-pr/blob/master/migration-guide/index.md#toc)|Make changes to your local repo| 
|`C:\myrepo\windows-driver-docs-pr [temp-branch]>git add .`|Capture differences to a unit of change|
|`C:\myrepo\windows-driver-docs-pr [temp-branch]>git commit -m "New projectname topics from con2md conversion."`|Commit the changes to your **local** repo|
|[**Update the MASTER BRANCH**](#update-master)|Use instructions from previous section to update the master branch with changes from the temp branch|
