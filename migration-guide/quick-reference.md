# For Writers: WDCML-to-OP migration quick reference
This is a quick reference for the Git commands and links used in WDCML to OP migration.

## Cloning the repo and creating a working branch
| Git command | Description |
|-------------|-------------|
|   `C:\myrepo> git clone https://github.com/Microsoft/windows-driver-docs-pr.git`| Clone the driver docs repo|
| `C:\myrepo\windows-driver-docs-pr [master]> .\.openpublishing.build.ps1 -parameters:targets=serve`|Do a **local** build|
|Open your browser to --> [http://localhost:8080](http://localhost:8080) |View the **local** build|
|`C:\myrepo\windows-driver-docs-pr [master]> git remote show origin`|See the branches on origin and local|
|`C:\myrepo\windows-driver-docs-pr [master]> git checkout -b working-branch`|Create a **local** working branch|

## Commit changes locally and push them to origin
| Git command | Description |
|-------------|-------------|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git add .`|Capture differences to a unit of change|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git commit -m "New projectname topics from con2md conversion."`|Commit the changes to your **local** repo|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git checkout master`| Move to the master branch|
|`C:\myrepo\windows-driver-docs-pr [master]>git pull origin`|Pull down the latest master changes|
|`C:\myrepo\windows-driver-docs-pr [master]>git checkout working-branch`|Go back over to the working branch|
|`C:\myrepo\windows-driver-docs-pr [working-branch]>git merge master`|Add latest master changes to working branch|
