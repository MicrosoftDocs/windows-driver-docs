---
title: Getting started writing a Hyper-V Extensible Switch extension
description: This section describes how to start writing a Hyper-V Extensible Switch extension
ms.assetid: 91C6ED75-1057-4520-8E8E-28817D8F3C81
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting Started Writing a Hyper-V Extensible Switch Extension


A Hyper-V Extensible Switch extension is an NDIS filter or Windows Filtering Platform (WFP) filter that runs inside the Hyper-V Extensible Switch (also called the "Hyper-V virtual switch").

There are 3 classes of extensions: capture, filtering, and forwarding. All of them can be implemented as NDIS filter drivers. Filtering extensions can also be implemented as WFP filter drivers.

For an architectural overview for driver developers, see [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md).

To create a Hyper-V Extensible Switch extension, follow these steps:

1.  Learn the extension architecture and programming model.
    -   Read the online documentation for NDIS-based extensions, beginning with [Hyper-V Extensible Switch](hyper-v-extensible-switch.md). Capture, filtering, and forwarding extensions use the standard NDIS filtering API. The NDIS interfaces have been enhanced to provide configuration, notifications, and identification of virtual switches and virtual machines.
        [Hyper-V Extensible Switch Functions](https://msdn.microsoft.com/library/windows/hardware/hh598171)
        [Hyper-V Extensible Switch Enumerations](https://msdn.microsoft.com/library/windows/hardware/hh598168)
        [Hyper-V Extensible Switch Structures and Unions](https://msdn.microsoft.com/library/windows/hardware/hh598189)
        [Hyper-V Extensible Switch OIDs](https://msdn.microsoft.com/library/windows/hardware/hh598178)
        [Hyper-V Extensible Switch Status Indications](https://msdn.microsoft.com/library/windows/hardware/hh598188)
        [Hyper-V Extensible Switch Macros](https://msdn.microsoft.com/library/windows/hardware/hh598175)
    -   Read the online documentation for WFP-based extensions, beginning with [Using Virtual Switch Filtering](using-virtual-switch-filtering.md).
    -   Watch the following instructional videos on extensions.
        -   [TechEd session on Hyper-V Extensible Switch](http://channel9.msdn.com/Events/TechEd/NorthAmerica/2012/VIR307)
        -   [Hyper-V Extensible Switch, Part I—Introduction](http://channel9.msdn.com/posts/Hyper-V-Extensible-Switch-Part-I--Introduction)
        -   [Hyper-V Extensible Switch, Part II—Understanding the Control Path](http://channel9.msdn.com/posts/Hyper-V-Extensible-Switch-Part-II--Understanding-the-Control-Path)
        -   [Hyper-V Extensible Switch, Part III—The Ins and Outs of the Datapath for Capture and Filter Extensions](http://channel9.msdn.com/posts/Hyper-V-Extensible-Switch-Part-III--The-Ins-and-Outs-of-the-Data-Path-for-Capture-and-Filter-Extensi)
    -   There are several PowerShell commands that can be used to manage extensions. These are listed in [Managing Installed Hyper-V Extensible Switch Extensions](managing-installed-hyper-v-extensions.md).

2.  Set up your development environment.
    -   Install Microsoft Visual Studio Professional 2012.
    -   Download and install [Windows Driver Kit 8](https://msdn.microsoft.com/library/windows/hardware/gg487428.aspx).

3.  Study the sample extensions.
    -   Download the [NDIS forwarding extension sample](http://go.microsoft.com/fwlink/p/?LinkId=618935).
    -   Download the [WFP sample](http://go.microsoft.com/fwlink/p/?LinkId=618934). This is a functioning prototype that includes vSwitch capability.

4.  Write your extension.
    -   You can use one of the samples as a starting point, port existing filter code, or write your extension from scratch.
    -   If you’re developing an NDIS extension, you can use the standard NDIS INF with a few changes as outlined in [INF Requirements for Hyper-V Extensible Switch Extensions](inf-requirements-for-hyper-v-extensions.md).

5.  Build your extension and unit-test it.
    -   You must [use Visual Studio to build your extension](https://msdn.microsoft.com/library/windows/hardware/ff554644.aspx).
    -   You can familiarize yourself with the extension build process by using Visual Studio to compile and run the sample extensions.

6.  Learn about the Windows certification (logo) process for getting an extension signed.
    -   An extension must pass the tests in the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613).
    -   The requirements for an extension are listed under the Filter.Driver.vSwitchExtension.ExtensionRequirements in the [Windows Hardware Certification Requirements - Filter Driver](https://msdn.microsoft.com/library/windows/hardware/jj128255) .

7.  Set up your Windows Hardware Certification Kit environment.
    -   Download and install the [Windows Hardware Certification Kit](https://msdn.microsoft.com/windows/hardware/hh852359).

8.  Run the WHCK tests for extensions:
    -   Filter.Driver.Fundamentals
    -   Filter.Driver.Security
    -   Filter.Driver.vSwitchExtension

9.  After your final extension passes WHCK certification, submit it to Microsoft.
    -   Your extension must be submitted as an MSI install package with a specific format to ensure that it can be tracked and deployed by management packages, such as [System Center Virtual Machine Manager (SCVMM) 2012](http://technet.microsoft.com/magazine/hh300651.aspx). The MSI format is defined in [Extension Driver MSI Packaging Requirements](https://msdn.microsoft.com/library/windows/hardware/hh921657.aspx).

10. List your extension on WindowsServerCatalog.com.
    -   List a brief description of your extension on WindowsServerCatalog.com.
    -   Information on listing a certified extension on WindowsServerCatalog.com will be available soon.

 

 





