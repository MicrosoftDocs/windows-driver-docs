---
ms.assetid: 6e8be17d-6e98-441e-9a2c-e62a007786ee
title: Developing, Testing, and Deploying Drivers
description: Starting with Windows Driver Kit \(WDK\) 8, the Windows driver development environment and the Windows debuggers are integrated into Microsoft Visual Studio.
keywords: 'developing drivers'
keywords: 'debugging drivers'
keywords: 'testing drivers'
keywords: 'deploying drivers'
---

# Developing, Testing, and Deploying Drivers

The Windows driver development environment and the Windows debuggers are integrated into Microsoft Visual Studio. In this integrated driver development environment, most of the tools you need for coding, building, packaging, deploying, debugging, and testing a driver are available in the Visual Studio user interface.

<iframe
src="https://hubs-video.ssl.catalog.video.msn.com/embed/9673727b-89ef-4a54-8228-dad41dbd8201/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe>

To set up the integrated development environment, first install Visual Studio and then install the WDK. You can find information about how to get Visual Studio and the WDK [here](http://go.microsoft.com/fwlink/p/?linkid=239721). [Debugging Tools for Windows](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff551063) is included when you install the WDK.

The WDK uses MSBuild.exe, which is available both in the Visual Studio user interface and as a command-line tool. Drivers created in the Visual Studio environment use Project and Solution files to describe a project or group of projects. The Visual Studio environment provides a tool for converting legacy Sources and Dirs files to Project and Solution files.

The Visual Studio environment provides templates for:

-   New drivers
-   Driver packages
-   New tests
-   Enhancement of existing tests
-   Custom driver deployment scripts

In the Visual Studio environment, you can configure the build process so that it automatically creates and signs a driver package. Static and run-time analysis tools are available in Visual Studio. You can configure a target computer for testing your driver and automatically deploy your driver to the target computer each time you rebuild. In Visual Studio you can establish a kernel-mode debugging session with a target computer. You can choose from an extensive set of run-time tests, and you can write your own tests.

The topics in this section show you how to use Visual Studio to perform several of the tasks involved in driver development, deployment, and testing.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Developing,%20Testing,%20and%20Deploying%20Drivers%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")

