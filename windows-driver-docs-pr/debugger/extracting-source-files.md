---
title: Extracting Source Files
description: Extracting Source Files
ms.assetid: b7c859a9-5264-401c-ad96-ad044bcc140e
keywords: ["extracting source files", "source servers, extracting source files"]
---

# Extracting Source Files


To extract all of the source files from all the modules for which you want to provide source, use the command:

```
srctool.exe -x
```

This tool must be executed on .pdb files that have already been source-indexed for your version control system on a computer that has version control access. This places all source files into a common directory tree. Copy the contents of this tree to the root of the Web site. You can do this as often as you want on any new products or modules that you want to add. There is no worry about files overwriting each other because the directory tree structure keeps dissimilar files separated and uniquely accessible.

### <span id="walk"></span><span id="WALK"></span>Walk

The Walk (Walk.cmd) script is included in Debugging Tools for Windows. This script searches recursively through a directory tree and executes any specified command on any file that matches a specified file mask. The syntax is:

```
walk.cmd FileMask Command
```

where *FileMask* specifies a file mask, with or without an accompanying starting directory, and *Command* specifies the command to be executed.

Here is an example that runs the srctool.exe file extraction command on all .pdb files in c:\\symbols and its subdirectories:

```
walk.cmd c:\symbols\*.pdb srctool.exe -x
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Extracting%20Source%20Files%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




