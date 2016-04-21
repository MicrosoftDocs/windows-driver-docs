# WDCML migration guide for driver documentation

This content is to help writers migrate the driver documentation (the conceptual portion) over to the open publishing platform. At a high level, migration consists of these steps:

1. [Get your Git account and tools set up](#s1)
2. [Refactor the WDCML TOC (create OP and REF XTOC files)](#s2)
3. [Convert the conceptual topics to OP](#s3)
4. [Do a local build of the OP content](#s4)
5. [Create working branch in windows-driver-docs-pr](#s5)
6. [Add OP content to the working branch](#s6)
7. [Build a .CSV file for redirecting old topics to OP ](#s7)
8. [Create new WDCML parent topic in HW_NODES](#s8)
9. [Update WDCML TOC to show only reference topics](#s9)
10. [Update Dev Center HXT file for new OP and REF](#s10)  
11. [Test and clean up content experience](#s11)
12. [Prepare for deployment (timing!)](#s12)
13. [Submit redirect request to MSDN team](#s13)

## <h2 id="s1"> Get your Git account and tools set up</a>

You'll want to make sure you have **GitHub set up**, install **Visual Studio Code**, and get **PowerShell** working with Git too. The last two are options, but those tools will be used throughout this topic in examples. 

* Set up GitHub: [Install and set up tools for authoring in GitHub](https://github.com/Microsoft/windows-driver-docs-pr/blob/master/contributor-guide/tools-and-setup.md)    
* Make sure you've been granted writer permissions on [Open Source Hub](https://opensourcehub.microsoft.com) (*ask Ted*)
* Install Visual Studio Code: [Setting up Visual Studio Code](https://code.visualstudio.com/docs/editor/setup)  
* Got to IDWEB and become a member of the **MSDN Reporting** security group
* Install PSGET: [http://psget.net/](http://psget.net/)
* Install GIT (the local tool): [https://git-scm.com/](https://git-scm.com/)
* Install POSH GIT: [https://github.com/dahlbyk/posh-git](https://github.com/dahlbyk/posh-git)
* Install PANDOC.exe: [https://github.com/jgm/pandoc/releases/tag/1.14.0.1](https://github.com/jgm/pandoc/releases/tag/1.14.0.1)
* Install GIT credential manager: [https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.2.2](https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.2.2)

Set up your local environment variables. Add paths for:  
* Pandoc.exe (it's probably at C:\Users\yourUserName\AppData\Local\Pandoc)
* The con2md conversion tool (it's under BuildX\Cmd)


## <h2 id="s2"> Refactor the WDCML TOC (create OP and REF XTOC files)</a>

## <h2 id="s3"> Convert the conceptual topics to OP</a>

## <h2 id="s4"> Do a local build of the OP content</a>

## <h2 id="s5"> Create working branch in windows-driver-docs-pr</a>

## <h2 id="s6"> Add OP content to the working branch</a>

## <h2 id="s7"> Build a .CSV file for redirecting old topics to OP</a>

## <h2 id="s8"> Create new WDCML parent topic in HW_NODES</a>

## <h2 id="s9"> Update WDCML TOC to show only reference topics</a>

## <h2 id="s10"> Update Dev Center HXT file for new OP and REF</a>

## <h2 id="s11"> Test and clean up content experience</a>

## <h2 id="s12"> Prepare for deployment (timing!)</a>

## <h2 id="s13"/> Submit redirect request to MSDN team</a>
