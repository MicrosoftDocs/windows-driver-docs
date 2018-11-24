---
ms.assetid: C5CD87E3-26C0-48AA-B75E-1EFFB0B5519D
title: Creating a Driver From Existing Source Files
description: The WDK is integrated with Microsoft Visual Studio, and uses the same compiler and build tools that you use to build Visual Studio solutions and projects.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Driver From Existing Source Files

The WDK is integrated with Microsoft Visual Studio, and uses the same compiler and build tools that you use to build Visual Studio solutions and projects. [MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804) replaces the Windows Build Utility (Build.exe) that was used in versions of the WDK prior to Windows Driver Kit (WDK) 8.

To convert a driver that was created with a previous version of the WDK, create a new Windows driver solution in Visual Studio using one of the provided Windows driver templates. If you start with a template for your driver model, the structure of the project will be in place and the correct platform tool set will be selected. You can then add your source files to the solution. For information about selecting templates, see [Creating a New Device Function Driver](creating-a-new-driver.md), [Creating a New Filter Driver](creating-a-new-filter-driver.md), or [Creating a New Software Driver](creating-a-new-software-driver.md).

## <span id="related_topics"></span>Related topics


* [WDK and the Visual Studio build environment](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454286)
* [ProjectUpgradeTool](https://msdn.microsoft.com/Library/Windows/Hardware/Dn265174)
* [MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804)
* [Walkthrough: Using MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262807)
* [Creating a New Device Function Driver](creating-a-new-driver.md)
* [Creating a New Filter Driver](creating-a-new-filter-driver.md)
* [Creating a New Software Driver](creating-a-new-software-driver.md)
 

 






