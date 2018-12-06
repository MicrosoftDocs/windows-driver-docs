---
ms.assetid: 6e8be17d-6e98-441e-9a2c-e62a007786ee
title: Developing, Testing, and Deploying Drivers
description: Starting with Windows Driver Kit (WDK) 8, the Windows driver development environment and debuggers are integrated into Microsoft Visual Studio.
keywords:
- developing drivers
- debugging drivers
- testing drivers
- deploying drivers
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Developing, Testing, and Deploying Drivers

The Windows driver development environment and the Windows debuggers are integrated into Microsoft Visual Studio. In this integrated driver development environment, most of the tools you need for coding, building, packaging, deploying, debugging, and testing a driver are available in the Visual Studio user interface.

>[!VIDEO https://www.microsoft.com/videoplayer/embed/9673727b-89ef-4a54-8228-dad41dbd8201]

To set up the integrated development environment, first install Visual Studio and then install the WDK. You can find information about how to get Visual Studio and the WDK [here](http://go.microsoft.com/fwlink/p/?linkid=239721). [Debugging Tools for Windows](https://msdn.microsoft.com/Library/Windows/Hardware/Ff551063) is included when you install the WDK.

The WDK uses MSBuild.exe, which is available both in the Visual Studio user interface and as a command-line tool. Drivers created in the Visual Studio environment use Project and Solution files to describe a project or group of projects. The Visual Studio environment provides a tool for converting legacy Sources and Dirs files to Project and Solution files.

The Visual Studio environment provides templates for:

-   New drivers
-   Driver packages
-   New tests
-   Enhancement of existing tests
-   Custom driver deployment scripts

In the Visual Studio environment, you can configure the build process so that it automatically creates and signs a driver package. Static and run-time analysis tools are available in Visual Studio. You can configure a target computer for testing your driver and automatically deploy your driver to the target computer each time you rebuild. In Visual Studio you can establish a kernel-mode debugging session with a target computer. You can choose from an extensive set of run-time tests, and you can write your own tests.

The topics in this section show you how to use Visual Studio to perform several of the tasks involved in driver development, deployment, and testing.



