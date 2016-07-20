# Install and set up tools for authoring in VSO

Follow the steps in this article to set up tools for contributing to the Windows driver documentation.

## Contents

- [Determine whether you really need to follow the rest of these steps](#determine-whether-you-really-need-to-follow-the-rest-of-these-steps)
- [Install Git for Windows](#install-git-for-windows)
- [Select a Git shell environment](#select-a-git-shell-environment)
- [Install a Markdown editor](#install-a-Markdown-editor)
- [Make updates](#make-updates)
- [Configure your user name and email locally](#configure-your-user-name-and-email-locally)
- [Next steps](#next-steps)

## Determine whether you really need to follow the rest of these steps

You might not need to follow all the steps in this article. It depends on the sort of content contribution you want or need to make.

### Submit a text-only change to an existing article

If you only need or want to make textual updates to an existing article, you probably don't need to follow the rest of the steps. You can use VSO's web-based Markdown editor to submit your changes. Just click the Contribute link in the article you want to modify.  Then click the edit icon in the VSO version of the article.

### All other changes
You need to install the tools if you want to make any of the following sorts of changes:

 - Major changes to an article
 - Create and publish a new article
 - Add new images or update images
 - Update an article over a period of days without publishing changes each of those days

## Install Git for Windows

Install Git for Windows from [http://git-scm.com/download/win](http://git-scm.com/download/win). This download installs the Git version control system, and it installs Git Bash, a command-line app that you can use to interact with your local Git repository.

You can accept the default settings; if you want the commands to be available within the Windows command line, select the option that enables it.

<p align="center">
 ![GitHub profile example](./media/tools-and-setup/gitbashinstall.png)

(Note: Git for Windows is not the same as "Github for Windows". "Github for Windows" is a different GUI-based tool that will also work if you want to read up on yourself. [https://windows.github.com/](https://windows.github.com/))

## Select a Git shell environment

Here are a few options:

* Git Bash -- included with Git for Windows
* **[GitHub Desktop](https://git-for-windows.github.io/)** -- Allows you to manage different repos offline and handle merge conflicts.
* **[PoshGit](https://github.com/dahlbyk/posh-git)** -- Integrates Git with PowerShell.
* **[SourceTree](https://www.atlassian.com/software/sourcetree/overview)** -- A more feature-rich GUI than GitHub Desktop. You'll need to use a personal access token as your password; see instructions [here](https://confluence.atlassian.com/display/SOURCETREEKB/Two-Factor+Authentication+%282FA%29+with+GitHub+in+SourceTree).
* **[Tortoise Git](https://tortoisegit.org/)** -- Once installed, you interact with Git by using contextual menu commands in your local repository.


## Install a Markdown editor

We author content using simple Markdown notation in the files, rather than complex "markup" (HTML, XML, etc.). So, you'll need to install a Markdown editor.

- **[Visual Studio Code](https://code.visualstudio.com/)** - Most of us use VS Code.

- **Atom**: GitHub's Atom Markdown editor: [http://atom.io](http://atom.io). It does not require a license for business use. It has spell check.

## Make updates

1.  The first time you want to make changes in the repo locally, you need to clone it.

        git clone https://cpubwin.visualstudio.com/_git/drivers
        
    If you already have a clone, update it using these commands:
    
        git checkout master
        git pull origin master

1. Create a new branch, make changes, and push the branch to the server.
```    
git checkout -b my-new-feature
###
git push -u origin my-new-feature
```
2. In your browser, navigate to https://cpubwin.visualstudio.com/_git/drivers and open a pull request from my-new-feature back into master.

## Configure your user name and email locally

To ensure you are listed correctly as a contributor, you need to configure your user name and email locally in Git.

1. Start your Git shell and switch into drivers:

   ```
   cd drivers
   ```

2. Configure your user name so it matches your name as you set it up in your GitHub profile:

    ```
    git config --global user.name "John Doe"
    ```
3. Configure your email so it matches the primary email designated in your GitHub profile; if you're a MSFT employee, it should be your MSFT email address:

    ```
    git config --global user.email "alias@example.com"
    ```
4. Type `git config -l` and review your local settings to ensure the user name and email in the configuration are correct.

## Next steps

- [Create a local working branch](./git-commands-for-master.md) on your computer so you can start work.

### Contributors' Guide Links

- [Overview article](./../README.md)
- [Index of guidance articles](./contributor-guide-index.md)
