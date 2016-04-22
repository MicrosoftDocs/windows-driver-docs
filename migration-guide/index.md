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
The WDCML XTOC file is key to refactoring the content. In this process, we'll create three seperate files to make it easier for people to understand which topics are going where. These XTOC files will also be used by tools to convert the OP content, the TOC file, and a redirects CSV file for the MSDN team to remove the old topics. By doing this refactoring in WDCML, we can take advantage of the autokeylinks elements for generating new "In this Section" lists.

### XTOC overview
To start, create three new XTOC files in your WDCML project:

* **projectname-OP.xtoc** This holds the conceputal content that will be migrated to OP. Create it by copying your projectname.xtoc file. 

* **projectname-REF.xtoc** This holds the reference content that will continue being published in WDCML.

* **XX-ToBeRemoved.xtoc** This holds topics that can be removed - reference and conceputal. Good candidates are "useless" orientation topics and DDI reference that is no longer needed. (It starts with XX so that it will appear at the bottom of the UI in XMetal.)


### Migration components
Once the content is split up into those three new XTOC files, they can be used to in the migration as follows...

![Migration components](images/MigrationComponents.png)

...When all is done, the **projectname-REF.xtoc** file can be copied over top of the original **projectname.xtoc** file. You'll use the **projectname-OP.xtoc** file with **con2md.exe**, the OP conversion tool, to convert your content from WDCML to MD format. It will also create a new **TOC.md** file for you. Finally, you can use **XX-ToBeRemoved.xtoc** and **projectname-OP.xtoc** to create a redirects CSV file so that MSDN can remove those WDCML topics and redirect requests to the specified topics.

### Refactoring goals
1. Both the OP and REF XTOCs can have **only a single topic at the root of the TOC**. Create a new WDCML topic if you need to. Note that there will be a new WDCML topic that's parent to the future OP and REF content.  

2. No DDI reference content is migrated to OP. 

3. As many low-value "orientation" (list of links) topics are removed.  See the next section for tips on cleaning up your IA.


### Tips for editing your XTOC files

* **Build a local CHM of the original XTOC**, projectname.xtoc. This way you can quickly click through topics to see what they look like (if you're trying to distinguish Ref from Conceptual or weed-out the useless orientation topics).

* I recommend **editing using XMetal in tandem with VS Code** to build your new XTOC files. The nice thing about Code is that it makes it easy to collapse and copy whole TOC nodes. 

![Collapsable XML nodes in VS Code](images/collapsableNodesVSCode.png)

* The other nice thing about VS code is that you can **open multiple tabs** (one for each of the XTOC files) and copy/paste XML nodes between the XTOC files. Even if you only use one tab, VS Code has a **Working files list** in the top left that lets you jump back and forth. As soon as you save a change, XMetal reloads the tree view UI.

* **Use this opportunity to clean up your content architecture.** Remove those useless topics that only provide content organization, such as "Design Guide" and "Reference". This example is in the reference, but the same applies to conceptual content you migrate to OP. Here, a reference section was broken up into several small TOC nodes. Most of them lacked even an intro sentence. The only value they provided is that the TOC provided some notion of what the DDIs were for. You can see here that even the top-most parent, **Secure Element DDI** didn't have all that much content (and manually-created  inaccurate "In this section" list).

#### BEFORE : Ref topics were grandchildren, children were "useless"
![TOC pre consolidation](images/TOCPreConsolidation.png)

#### AFTER : grandchildren became alphabetized children
The direct children were removed and the reference organization was performed using tables in the parent topic. Then, all references topics were brought up a level and alphabetized to be direct children of the parent topic.

You can also see how a new topic was created to be a single root at the top of the TOC. Depending on your project, this may not be necessary - you may already one that would be a great candidate.
![TOC post consolidation](images/TOCPostConsolidation.png)


### XTOC quality check
When you're all finsished (or you think you are), do a local CHM build of **projectname-OP.xtoc** and **projectname-REF.xtoc** and compare it to the original CHM. Make sure you have the all of the topics from the original CHM accounted for somewhere in the new XTOCs. 


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
