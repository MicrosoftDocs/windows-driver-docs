# Windows Driver Documentation Contributor Guide

You've found the GitHub repository that houses the source for the technical documentation that is published to  [https://msdn.microsoft.com/windows-drivers/documentation](https://msdn.microsoft.com/windows-drivers/documentation).

This repository also contains guidance to help you contribute to our technical documentation.  For a list of the articles in the contributors' guide, see [the index](contributor-guide/contributor-guide-index.md).

## Contribute to Windows driver documentation

Thank you for your interest in Windows driver documentation!

* [Ways to contribute](#ways-to-contribute)
* [Repository organization](#repository-organization)
* [Use GitHub, Git, and this repository](#use-github-git-and-this-repository)
* [How to use Markdown to format your topic](#how-to-use-Markdown-to-format-your-topic)
* [More resources](#more-resources)
* [Index of all contributors' guide articles](./contributor-guide/contributor-guide-index.md) (opens new page)

## Ways to contribute

You can contribute to [Windows driver documentation](https://msdn.microsoft.com/windows-drivers/documentation) in a couple different ways:

* You can easily contribute to technical articles in the GitHub user interface. Either find the article in this repository, or visit the article on [https://msdn.microsoft.com/windows-drivers/documentation](https://msdn.microsoft.com/windows-drivers/documentation) and click the link in the article that goes to the GitHub source for the article.
* If you are making substantial changes to an existing article, adding or changing images, or contributing a new article, you need to fork this repository, install Git Bash, Markdown Pad, and learn some git commands.


## Repository organization

The content in the Windows driver-content repository follows the organization of documentation on [https://msdn.microsoft.com/windows-drivers/documentation](https://msdn.microsoft.com/windows-drivers/documentation).

The subfolders contain the documentation articles formatted as Markdown files with an *.md* extension.

For example, articles in the develop directory are published to  *https://msdn.microsoft.com/en-us/windows-drivers/develop/{article-name-without-md}/*.

### \contributor-guide

This folder contains articles that are part of our contributors' guide.  

## Use GitHub, Git, and this repository

For information about how to contribute, how to use the GitHub UI to contribute small changes, and how to fork and clone the repository for more significant contributions, see [Install and set up tools for authoring in GitHub](./contributor-guide/tools-and-setup.md).

If you install GitBash and choose to work locally, the steps for creating a new local working branch, making changes, and submitting the changes back to the main branch are listed in [Git commands for creating a new article or updating an existing article](./contributor-guide/git-commands-for-master.md)

### Branches

We recommend that you create local working branches that target a specific scope of change. Each branch should be limited to a single concept/article both to streamline work flow and reduce the possibility of merge conflicts.  The following efforts are of the appropriate scope for a new branch:

* A new article (and associated images)
* Spelling and grammar edits on an article.
* Applying a single formatting change across a large set of articles (e.g. new copyright footer).

## How to use Markdown to format your topic

All the articles in this repository use GitHub flavored Markdown.  Here's a list of resources.

- [Markdown basics](https://help.github.com/articles/Markdown-basics/)

- For our list of Markdown editors, see the [tools and setup topic](./contributor-guide/tools-and-setup.md#install-a-Markdown-editor).


## More resources

See the [index of our contributor's guide](./contributor-guide/contributor-guide-index.md) for all our guidance topics.

* Live branch: https://msdn.microsoft.com/windows-drivers/documentation
* Any other branch: https://ppe.msdn.microsoft.com/windows-drivers/documentation

If you don't have the permission to push to this repo, fork it to your own account and use pull request to submit your changes back.

Validation and Preview
----------------------

Before pushing your changes to the remote, you can build and preview your article  locally.  Here are your options:

1. To validate your changes, run the command `.\.openpublishing.build.ps1` under the root of the repo.
2. To preview your changes:
   * From a command prompt, run `powershell .openpublishing.build.ps1 -parameters:targets=serve` under the root of the repo.
   * From PowerShell, run '.\.openpublishing.build.ps1 -parameters:targets=serve'
   * Open `http://localhost:8080` in your browser.
