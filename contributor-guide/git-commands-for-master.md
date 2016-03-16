# Git commands for creating a new article or updating an existing article


## Standard process (working from master)
Follow the steps in this article to create a local working branch on your computer so that you can create a new article for https://msdn.microsoft.com/windows/hardware/drivers or update an existing article.

1. Start the command-line tool that you use for Git.
 <!-- **Note:** If you are working in the public repository, change windows-driver-docs-pr to windows-driver-docs in all the commands. -->
2. Change to windows-driver-docs-pr:

        cd windows-driver-docs-pr
3. Check out the master branch:

        git checkout master

4. Create a fresh local working branch derived from the master branch:

        git pull upstream master:<working branch>

5. Move into the new working branch:

        git checkout <working branch>

6. Let your fork know you created the local working branch:

        git push origin <working branch>

7. Create your new article or make changes to an existing article. Use Windows Explorer to open and create new Markdown files, and use [Visual Studio Code](https://code.visualstudio.com/) as your Markdown editor. After you created or modified your article and images, go to the next step.
        
8. Add and commit your changes:

        git add .
        git commit –m "<comment>"

   Or, to add only the specific files you modified:

        git add <file path>
        git commit –m "<comment>"
<!--will OP build untracked files? -->

8. Optionally, build and preview your article locally.
    * Navigate to the root of the repository and run the command `.\.openpublishing.build.ps1 -parameters:target=serve`.
    * Open `http://localhost:8080` in your browser.
    
9. Update your local working branch with changes from upstream:

        git pull upstream master

10. Push the changes to your fork on GitHub:

        git push origin <working branch>
        
12. When you are ready to submit your content to the upstream master branch for staging, validation, and/or publishing, in the GitHub UI, create a pull request from your fork to the master branch.

14. The pull request acceptor reviews your pull request, provides feedback, and/or accepts your pull request.

15. Optionally verify your published article or changes at
 https://msdn.microsoft.com/windows/hardware/drivers/*directory*/*name-of-your-article-without-the-MD-extension*

**Notes:**

## Working with release branches

When you are working with a release branch, the best way to create a local working branch from the release branch is to use this command syntax:

    git checkout upstream/<upstream branch name> -b <local working branch name>

This creates the local branch directly from the upstream branch, avoiding any local merging.
