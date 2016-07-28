# Contributing to Windows Driver Documentation

Thank you for your interest in the Windows driver documentation! 
See below for details on how you can contribute to our technical documentation.

## Sign a CLA

If you are not a Microsoft employee, you must [sign a Microsoft Contribution Licensing Agreement (CLA)](https://cla.microsoft.com/) before you can contribute to any Microsoft repositories. 
If you've already contributed to Microsoft repositories in the past, congratulations! 
You've already completed this step.

## Public and private repos

The driver docs are hosted on two different sites.

If you are not a Microsoft employee, work in the [public content repository](https://github.com/Microsoft/windows-driver-docs).

If you are a Microsoft employee, work in the [private content repository](https://cpubwin.visualstudio.com/drivers/_git/drivers).  

## Editing topics

To edit an existing file, if you're already in the repo, simply navigate to the file and click the "Edit" button.  Alternatively, from an MSDN page, click the **Contribute** button and you will be taken directly to the relevant Markdown source file in the repo.  

> **Note** We're actively moving docs into the repo, so the one you want might not be there yet.  If you don't see a **Contribute** button for a page you'd like to change, please open an issue in the repo and be sure to provide the URL of the page in question.
 
If you're using the GitHub-based public repo, GitHub automatically forks the official repo into your personal GitHub account, where you can make your changes. 

If you're using the VSO-based private repo, use the drop-down arrow next to the Commit button and select **Commit to new branch**.

Either way, when you're done, submit a pull request back to the master branch of the official repository. 
After your pull request is created, someone on the Windows driver documentation team reviews your changes.

If your request is accepted, updates are published to https://msdn.microsoft.com/windows/hardware/drivers.

## Making more substantial changes

To make substantial changes to an existing article, add or change images, or contribute a new article, you will need to create a local clone of the content.

If you are using the public repo, fork the official repo into your personal GitHub account, and then clone the fork down to your local computer.  Work locally, then push your changes back into your fork.  Then open a pull request back to the master branch of the official public repo.

If you are using the private repo, clone the private repo to your local computer.  Create a new branch from master, make your changes, and then push your new branch back into the VSO private repo.  Then open a pull request back to the master branch.

## Resources

For editing Markdown on your local computer, we recommend [Visual Studio Code](https://code.visualstudio.com/).

You can learn the basics of Markdown in just a few minutes.  To get started, check out [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

