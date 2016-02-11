# Windows Driver Documentation Contributor Guide

Welcome to the windows-driver-docs-private repository, housing the source for the Windows Driver Kit documentation that is published to:

* Live branch: https://msdn.microsoft.com/windows-drivers
* Any other branch: https://msdnstage.redmond.corp.microsoft.com/windows-drivers

> **Note**: Currently, this repository contains only the driver development subset of the full WDK documentation. To find the rest of the driver kit docs, see the [Windows Driver Kit docs on MSDN](https://msdn.microsoft.com/en-us/library/windows/hardware/ff557573).

When you're viewing a topic in https://msdn.microsoft.com/windows-drivers, you can click the Contribute to this topic button to go to the corresponding Markdown source file in this repository.

This repository also contains guidance to help you contribute to our technical documentation.  For a list of the articles in the contributors' guide, see [the index](contributor-guide/contributor-guide-index.md).

## Ways to contribute

You can contribute to [Windows driver documentation](https://msdn.microsoft.com/windows-drivers) in a couple different ways:

* You can easily contribute to technical articles in the GitHub user interface. Either find the article in this repository, or visit the article on [https://msdn.microsoft.com/windows-drivers](https://msdn.microsoft.com/windows-drivers) and click the Contribute to this topic button to go to the GitHub source for the article.
* If you are making substantial changes to an existing article, adding or changing images, or contributing a new article, you need to fork this repository, install [a Git command line shell](./contributor-guide/tools-and-setup.md#Select-a-Git-shell-environment), [a Markdown editor](./contributor-guide/tools-and-setup.md#install-a-Markdown-editor), and learn some Git commands.


## Repository organization

The content in the Windows driver-content repository follows the organization of documentation on [https://msdn.microsoft.com/windows-drivers](https://msdn.microsoft.com/windows-drivers).

The subfolders contain the documentation articles formatted as Markdown files with an *.md* extension.

For example, articles in the develop directory are published to  *https://msdn.microsoft.com/en-us/windows-drivers/develop/{article-name-without-md}/*.

### \contributor-guide

This folder contains articles that are part of our contributors' guide.  

## Use GitHub, Git, and this repository

For information about how to contribute, how to use the GitHub UI to contribute small changes, and how to fork and clone the repository for more significant contributions, see [Install and set up tools for authoring in GitHub](./contributor-guide/tools-and-setup.md).

If you install a Git shell and choose to work locally, the steps for creating a new local working branch, making changes, and submitting the changes back to the main branch are listed in [Git commands for creating a new article or updating an existing article](./contributor-guide/git-commands-for-master.md).

### Branches

We recommend that you create local working branches that target a specific scope of change. Each branch should be limited to a single concept/article both to streamline work flow and reduce the possibility of merge conflicts.  The following efforts are of the appropriate scope for a new branch:

* A new article (and associated images)
* Spelling and grammar edits on an article.
* Applying a single formatting change across a large set of articles (e.g. new copyright footer).

Validation and Preview
-----------------------

If you have cloned the repository to your local machine, you can build and preview your article locally.  This is a good way to discover problems before pushing your changes to the remote.

1. Navigate to the root of the repository and run the command `.\.openpublishing.build.ps1`.
2. Open `http://localhost:8080` in your browser.
