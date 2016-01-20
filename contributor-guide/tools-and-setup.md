# Install and set up tools for authoring in GitHub

Follow the steps in this article to set up tools for contributing to the Windows driver documentation. Casual and occasional contributors can probably use the GitHub UI described in step 2.

If you're unfamiliar with Git, you might want to review some Git terminology: [https://help.github.com/articles/github-glossary](https://help.github.com/articles/github-glossary). In addition, this StackOverflow thread contains a glossary of Git terms you'll encounter in this set of steps: [http://stackoverflow.com/questions/7076164/terminology-used-by-git](http://stackoverflow.com/questions/7076164/terminology-used-by-git)

## Contents

- [Create a GitHub account and set up your profile](#create-a-github-account-and-set-up-your-profile)
- [Determine whether you really need to follow the rest of these steps](#determine-whether-you-really-need-to-follow-the-rest-of-these-steps)
- [Permissions in GitHub](#permissions-in-github)
- [Install Git for Windows](#install-git-for-windows)
- [Enable two-factor authentication](#enable-two-factor-authentication)
- [Install a Markdown editor](#install-a-Markdown-editor)
- [Configure Atom](#configure-atom)
- [Fork the repository and copy it to your computer](#fork-the-repository-and-copy-it-to-your-computer)
- [Configure your user name and email locally](#configure-your-user-name-and-email-locally)
- [Next steps](#next-steps)

## Create a GitHub account and set up your profile

To contribute to the Windows driver content, you'll need a [GitHub](http://www.github.com) account.

If you are a Microsoft contributor, you need to set up your GitHub account so that you're a member of the Microsoft organization on GitHub. Set up your profile as follows:

- **Profile picture**: a picture of you (required)
- **Name**: your first and last name (required)
- **Email**: your Microsoft email address (required)
- **Company**: Microsoft Corporation (required)
- **Location**: list your location (required)

## Determine whether you really need to follow the rest of these steps

You might not need to follow all the steps in this article. It depends on the sort of content contribution you want or need to make.

### Submit a text-only change to an existing article

If you only need or want to make textual updates to an existing article, you probably don't need to follow the rest of the steps. You can use GitHub's web-based Markdown editor to submit your changes. Just click the Contribute link in the article you want to modify.  Then, click the edit icon in the GitHub version of the article.

That opens the easy-to-use web editor that makes it easy to submit changes. You don't need to follow the other steps in this article.

### All other changes
You need to install the tools if you want to make any of the following sorts of changes:

 - Major changes to an article
 - Create and publish a new article
 - Add new images or update images
 - Update an article over a period of days without publishing changes each of those days

## Permissions in GitHub

<!--Anybody with a GitHub account can contribute to Windows driver technical content through our public repository at [https://github.com/Windows driver/Windows driver-content](https://github.com/Windows driver/Windows driver-content). No special permissions are required.-->

If you are a Microsoft FTE and are a member of the Microsoft organization on GitHub, you have read-only permissions on our private content repository:  [Microsoft/windows-driver-docs-private ](https://github.com/Microsoft/windows-driver-docs-private).

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


## Enable two-factor authentication

You have to enable two factor authentication (2FA) on your GitHub account if you are working in the private content repository. It's required in the private repository.

To enable this, follow the instructions in both the following GitHub help topics:

- [About Two-Factor Authentication](https://help.github.com/articles/about-two-factor-authentication/)
- [Creating an access token for command-line use](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)

After you enable 2FA, you have to enter the access token instead of your GitHub password at the command prompt when you try to access a GitHub repository from the command line. The access token is not the authentication code that you get in a text message when you set up 2FA. It's a long string that looks something like this:  fdd3b7d3d4f0d2bb2cd3d58dba54bd6bafcd8dee. A few notes about this:

- When you create your access token, save it in a text file to make it readily accessible when you need it.

- Later, when you need to paste the token, you have two ways to paste in the command line:

 - Click the icon in the upper left corner of the command line window>Edit>Paste.
 - Right-click the icon in the upper left corner of the window and click Properties>Options>QuickEdit Mode. This configures the command line so you can paste by right-clicking in the command line window.

## Install a Markdown editor

We author content using simple Markdown notation in the files, rather than complex "markup" (HTML, XML, etc.). So, you'll need to install a Markdown editor.

- **Atom**: Most of us use GitHub's Atom Markdown editor: [http://atom.io](http://atom.io). It does not require a license for business use. It has spell check.

- **[Visual Studio Code](https://www.visualstudio.com/products/code-vs.aspx)** - Microsoft's entry in this space.

## Configure Atom

If you use Atom, you'll need to set a few things up.

- Atom defaults to using 2 spaces for tabs, but Markdown expects 4 spaces. If you leave it at the default of two, your article will look great in local preview, but not when it’s imported into our rendering environment. So, configure Atom to use 4 spaces - you can find this setting under File>Settings>Editor Settings>Tab Length.
- You will probably also want to turn on Soft Wrap in this section too, which does the same as "word wrap" in Notepad.
- To turn on the Markdown preview, click Packages>Markdown Preview>Toggle Preview. You can use Ctrl-Shift-M to toggle the preview HTML view.

## Fork the repository and copy it to your computer

1. Create a fork of the repository in GitHub - go to the top-right of the page and click the Fork button. If prompted, select your account as the location where the fork should be created.

 This creates a copy of the repository within your Git Hub account. Generally speaking, technical writers and program managers need to fork windows-driver-docs-private, the private repo. <!--Community contributors need to fork Windows driver-content, the public repo.-->

  You only need to fork one time; after your first setup, if you want to copy your fork to another computer, you only have to run the commands that follow in this section to copy the repo to your computer.  If you choose to create forks of both repositories, you will need to create a fork for each repository.

2. Copy the Personal Access Token that you got from [https://github.com/settings/applications#personal-access-tokens](https://github.com/settings/applications#personal-access-tokens). You can accept the default permissions for the token.  Save the Personal Access Token in a text file for later reuse.

3. Next, copy the repository to your computer with your credentials embedded in the command string.  To do this, open your Git shell as administrator. At the command prompt, enter the following command.  This command creates a windows-driver-docs-private directory on your computer.  If you're using the default location, it will be at c:\users<your Windows user name>\windows-driver-docs-private.

<!-- Public repo:

        git clone https://[your GitHub user name]:[token]@github.com/<your GitHub user name>/Windows driver-content.git
 -->
Private repo:

        git clone https://[your GitHub user name]:[token]@github.com/<your GitHub user name>/windows-driver-docs-private.git

For example, this clone command could look something like this:

        git clone https://smithj:b428654321d613773d423ef2f173ddf4a312345@github.com/smithj/windows-driver-docs-private.git  

## Set remote repository connection and configure credentials

Create a reference to the root repository by entering these commands. This sets up connections to the repository in GitHub so that you can get the latest changes onto your local machine and push your changes back to GitHub. This command also configures your token locally so that you don't have to enter your name and password each time you try to access the upstream repo and your fork on GitHub.

<!-- Public repo:

        cd windows-driver-docs-private
        git remote add upstream https://[your GitHub user name]:[token]@github.com/Microsoft/windows-driver-docs.git
        git fetch upstream -->

Private repo:

        cd Windows driver-content-pr
        git remote add upstream https://[your GitHub user name]:[token]@github.com/Microsoft/windows-driver-docs-private.git
        git fetch upstream

This usually takes a while. After you do this, you won't have to fork again or enter your credentials again. You would only have to copy the forks to a local computer again if you set the tools up on another computer.


## Configure your user name and email locally

To ensure you are listed correctly as a contributor, you need to configure your user name and email locally in Git.

1. Start your Git shell and switch into <!--Windows driver-content or -->windows-driver-docs-private:

   <!-- ````
   cd Windows driver-content
   ````

 or
-->
   ````

   cd windows-driver-docs-private
   ````

2. Configure your user name so it matches your name as you set it up in your GitHub profile:

    ````
    git config --global user.name "John Doe"
    ````
3. Configure your email so it matches the primary email designated in your GitHub profile; if you're a MSFT employee, it should be your MSFT email address:

    ````
    git config --global user.email "alias@example.com"
    ````
4. Type `git config -l` and review your local settings to ensure the user name and email in the configuration are correct.

## Next steps

- [Create a local working branch](./git-commands-for-master.md) on your computer so you can start work.
<!--- Copy [the Markdown template](../Markdown templates/Markdown-template-for-new-articles.md) as the basis for a new article.
-->

### Contributors' Guide Links

- [Overview article](./../README.md)
- [Index of guidance articles](./contributor-guide-index.md)
