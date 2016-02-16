# Windows Driver Documentation

Welcome to the windows-driver-docs-private repository, containing the source for the Windows Driver Kit documentation.  This page describes how you can contribute to this documentation. 

## Quick start guide

1.  When you're viewing a topic in https://msdn.microsoft.com/windows-drivers, click the Contribute to this topic button to go to the corresponding Markdown source file in this repository.
2.  If you haven't already, fork the repository into your own GitHub account.
3.  For minor edits, make your changes right in the GitHub UI.  For larger changes, clone your fork to your local computer.
    *  If you have cloned the repository to your local machine, you can build and preview your article locally.  This is a good way to discover problems before pushing your changes to the remote.
        1. Navigate to the root of the repository and run the command `.\.openpublishing.build.ps1`.
        2. Open `http://localhost:8080` in your browser.

    *  When you're done writing, push the changes back to your fork on GitHub.
4.  Open a pull request back to the official repository.
5.  The documentation owner reviews your request and if needed iterates with you in the context of the pull request.
6.  Your content is staged for review in a branch of: https://msdnstage.redmond.corp.microsoft.com/windows-drivers.
7.  After contributor and content owner sign off, your updates are published to https://msdn.microsoft.com/windows-drivers.

For more details about setup, see [Install and set up tools for authoring in GitHub](./contributor-guide/tools-and-setup.md).

To learn the Git commands for working locally, see [Git commands for creating a new article or updating an existing article](./contributor-guide/git-commands-for-master.md).
