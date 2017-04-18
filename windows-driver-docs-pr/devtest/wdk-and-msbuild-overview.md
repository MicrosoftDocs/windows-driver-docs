---
title: WDK and MSBuild overview
description: Visual Studio can manage multiple projects. This section describes the WDK build environment.
ms.assetid: BABF3C72-05E9-4424-AAF9-68DFD48CEC32
---

# WDK and MSBuild overview


Visual Studio can manage multiple projects. This section describes the WDK build environment.

A Visual Studio solution can consist of a single project or multiple projects: both driver projects and non-driver projects. Every project is associated with a platform toolset. The platform toolset extends and modifies the build process for a given target architecture in order to build a particular kind of binary. The binary can be a driver, a library, or an executable program.

The following figure shows a typical build process using the MSBuild platform. In the diagram, the driver project (MSBuild Project 1) uses driver platform toolset to build drivers. The driver project can reference Windows kernel-mode and user-mode headers and libraries. The Windows DLL project (MSBuild Project 2) builds a DLL and uses the Windows SDK platform toolset to build applications or user-mode libraries. Every platform toolset has its own set of targets. These targets invoke tasks. These tasks will execute the build tools.

For C/C++ native code (user mode and kernel mode) and managed code, the WDK installs the .NET Full Framework, Windows headers, libraries (user mode or kernel mode) and tools, .NET Tools and the VC compilers, CRT headers, and libraries. Along with these, to be able to build C/C++ projects with MSBuild, all the components required by the compiler must be installed.

![figure shows the wdk and msbuild platform for a visual studio driver solution.](images/build-platform-msbuild.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WDK%20and%20MSBuild%20overview%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




