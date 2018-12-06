---
ms.assetid: 51CD05AB-2626-4E27-AA08-09547D546218
title: Converting WDK 8.1 Projects to WDK 10
description: How to convert a driver project created with Microsoft Visual Studio 2013 and the Windows Driver Kit (WDK) 8.1 to a driver project that builds in Microsoft Visual Studio 2015 with the Windows Driver Kit (WDK) 10.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Converting WDK 8.1 Projects to WDK 10

This topic describes how to convert a driver project that was created using Microsoft Visual Studio 2013 and Windows Driver Kit (WDK) 8.1 to a driver project that builds in Microsoft Visual Studio 2015 with the Windows Driver Kit (WDK) 10.

Visual Studio 2015 has new compiler warnings and errors. Even if your driver project built with no errors in Visual Studio 2013, you might see errors when you build it in Visual Studio 2015.

Use these steps to convert the projects in a driver solution.

1.  In Visual Studio 2015, open the legacy driver solution.

    Visual Studio automatically runs ProjectUpgradeTool to convert the projects in this solution. You can also run this tool from the command line. By default, when you install the WDK, ProjectUpgradeTool.exe installs in Windows Kits\\10\\bin\\x86.

    Visual Studio opens a **Review Solution Actions** dialog with the title **Upgrade VC++ Compiler and Libraries**. Click **OK** and Visual Studio attempts to upgrade all projects in the solution.

    If you see a **File Modification Detected** dialog, choose **Reload All**.

2.  In the Solution Explorer pane, right-click the driver project name and choose **Properties**. Click the **Configuration Manager** button. In the **Active solution configuration** list, choose **&lt;New...&gt;**. Type a name and copy the settings from a Windows 8.1 project context. Click **OK**.

    Typically, the converted solution contains two configuration profiles, one for debug (testing) and one for release. To create a similar environment with WDK 10, simply choose **&lt;New...&gt;** twice. To create a debug profile, copy from the **Win 8.1 Debug** profile. To create a release profile, copy from the **Win 8.1 Release** profile.

3.  In WDK versions prior to WDK 10, your driver solution always needed a package project. In WDK 10, you only need a package project if you are including multiple drivers in a driver package. Use the following guidelines:

    -   If you have only one driver in the solution and a package project exists, delete it.

    -   If you have more than one driver in the solution, ensure that your solution contains a package project. Then, for each driver project in the solution, open project properties and navigate to **Configuration Properties &gt; Driver Settings**. Set **BuildPackage** to **No**. If you are building from the command line, set **/p:SupportsPackaging=false**.

4.  Again in driver project properties, choose **Properties**. Navigate to **Configuration Properties &gt; Driver Settings &gt; General &gt; Target OS Version**. Select Windows 10.

    Verify that **Target Platform** is set to **Desktop**, and build the solution. Fix any errors that occur.

5.  Once the solution builds successfully, change **Target Platform** to **Universal**.

    Build the solution again. At this point, the only errors are from the ApiValidator tool, which checks if the driver calls any non-universal functionality. Replace any calls to non-universal DDIs with calls to universal DDIs.

    For more information about ApiValidator, see [Validating Universal Windows drivers](validating-universal-drivers.md).

    To learn how to determine the target platform for a given DDI, see [Target platform on driver reference pages](windows-10-editions-for-universal-drivers.md).

 

 





