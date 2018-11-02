---
title: Extracting Source Files
description: Extracting Source Files
ms.assetid: b7c859a9-5264-401c-ad96-ad044bcc140e
keywords: ["extracting source files", "source servers, extracting source files"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Extracting Source Files


To extract all of the source files from all the modules for which you want to provide source, use the command:

```console
srctool.exe -x
```

This tool must be executed on .pdb files that have already been source-indexed for your version control system on a computer that has version control access. This places all source files into a common directory tree. Copy the contents of this tree to the root of the Web site. You can do this as often as you want on any new products or modules that you want to add. There is no worry about files overwriting each other because the directory tree structure keeps dissimilar files separated and uniquely accessible.

### <span id="walk"></span><span id="WALK"></span>Walk

The Walk (Walk.cmd) script is included in Debugging Tools for Windows. This script searches recursively through a directory tree and executes any specified command on any file that matches a specified file mask. The syntax is:

```console
walk.cmd FileMask Command
```

where *FileMask* specifies a file mask, with or without an accompanying starting directory, and *Command* specifies the command to be executed.

Here is an example that runs the srctool.exe file extraction command on all .pdb files in c:\\symbols and its subdirectories:

```console
walk.cmd c:\symbols\*.pdb srctool.exe -x
```

 

 





