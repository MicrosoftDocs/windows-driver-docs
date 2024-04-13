---
ms.assetid: 6e8be17d-6e98-441e-9a2c-e62a007786ee
title: Developing, Testing, and Deploying Drivers
description: Starting with Windows Driver Kit (WDK) 8, the Windows driver development environment and debuggers are integrated into Microsoft Visual Studio.
keywords:
- developing drivers
- testing drivers
- deploying drivers
ms.date: 08/23/2017
ms.topic: article
---

# Developing, Testing, and Deploying Drivers

The Windows driver development environment and the Windows debuggers are integrated into Microsoft Visual Studio. In this integrated driver development environment, most of the tools you need for coding, building, packaging, deploying, and testing a driver are available in the Visual Studio user interface.

To set up the integrated development environment, first install Visual Studio and then install the WDK. You can find information about how to get Visual Studio and the WDK on the [WDK setup and download page](../download-the-wdk.md). The [Debugging Tools for Windows](../debugger/index.md) are included with the WDK installation.

The WDK uses MSBuild.exe, which is available both in the Visual Studio user interface and as a command-line tool. Drivers created in the Visual Studio environment use Project and Solution files to describe a project or group of projects. The Visual Studio environment provides a tool for converting legacy Sources and Dirs files to Project and Solution files.

The Visual Studio environment provides templates for:

- New drivers
- Driver packages
- New tests
- Enhancement of existing tests
- Custom driver deployment scripts

In the Visual Studio environment, you can configure the build process so that it automatically creates and signs a driver package. Static and run-time analysis tools are available in Visual Studio. You can configure a target computer for testing your driver and automatically deploy your driver to the target computer each time you rebuild. You can choose from an extensive set of run-time tests, and you can write your own tests.

The topics in this section show you how to use Visual Studio to perform several of the tasks involved in driver development, deployment, and testing.

## Additional Videos

You'll find videos on the following pages in the Windows driver docs:

- [Using the Windows Performance Toolkit (WPT) with WDF](../wdf/using-the-windows-performance-toolkit--wpt--with-wdf.md)
- [Video: Accessing driver IFR logs without a debugger](../wdf/video--accessing-driver-ifr-logs-without-a-debugger.md)
- [Video: Debugging your driver with WDF source code](../wdf/video--debugging-your-driver-with-wdf-source-code.md)
- [Videos: Debugging UMDF Drivers](../wdf/videos--debugging-umdf-drivers.md)