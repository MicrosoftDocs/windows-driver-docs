---
title: Getting started writing a Hyper-V Extensible Switch extension
description: This section describes how to start writing a Hyper-V Extensible Switch extension
ms.date: 04/20/2017
---

# Getting Started Writing a Hyper-V Extensible Switch Extension

A Hyper-V Extensible Switch extension is an NDIS filter or Windows Filtering Platform (WFP) filter that runs inside the Hyper-V Extensible Switch (also called the "Hyper-V virtual switch").

There are 3 classes of extensions: capture, filtering, and forwarding. All of them can be implemented as NDIS filter drivers. Filtering extensions can also be implemented as WFP filter drivers.

For an architectural overview for driver developers, see [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md).

To create a Hyper-V Extensible Switch extension, follow these steps:

1. Learn the extension architecture and programming model.
    -   Read the online documentation for NDIS-based extensions, beginning with [Hyper-V Extensible Switch](hyper-v-extensible-switch.md). Capture, filtering, and forwarding extensions use the standard NDIS filtering API. The NDIS interfaces have been enhanced to provide configuration, notifications, and identification of virtual switches and virtual machines.
        [Hyper-V Extensible Switch Functions](/windows-hardware/drivers/ddi/_netvista/)
        [Hyper-V Extensible Switch Enumerations](/windows-hardware/drivers/ddi/ntddndis/index)
        [Hyper-V Extensible Switch Structures and Unions](/windows-hardware/drivers/ddi/_netvista/)
        [Hyper-V Extensible Switch OIDs](./hyper-v-extensible-switch-oids.md)
        [Hyper-V Extensible Switch Status Indications](./hyper-v-extensible-switch-status-indications.md)
        [Hyper-V Extensible Switch Macros](/windows-hardware/drivers/ddi/ntddndis/)
    -   Read the online documentation for WFP-based extensions, beginning with [Using Virtual Switch Filtering](using-virtual-switch-filtering.md).
    -   Watch the following instructional videos on extensions.  
        -   [Hyper-V Extensible Switch, Part I—Introduction](https://channel9.msdn.com/posts/Hyper-V-Extensible-Switch-Part-I--Introduction)
        -   [Hyper-V Extensible Switch, Part II—Understanding the Control Path](https://channel9.msdn.com/posts/Hyper-V-Extensible-Switch-Part-II--Understanding-the-Control-Path)
        -   [Hyper-V Extensible Switch, Part III—The Ins and Outs of the Datapath for Capture and Filter Extensions](https://channel9.msdn.com/posts/Hyper-V-Extensible-Switch-Part-III--The-Ins-and-Outs-of-the-Data-Path-for-Capture-and-Filter-Extensi)
    -   There are several PowerShell commands that can be used to manage extensions. These are listed in [Managing Installed Hyper-V Extensible Switch Extensions](managing-installed-hyper-v-extensions.md).

2.  Set up your development environment.
    -   Install Microsoft Visual Studio Professional.
    -   Download and install [Windows Driver Kit](../download-the-wdk.md).

3.  Study the sample extensions.
    -   Download the [NDIS forwarding extension sample](https://go.microsoft.com/fwlink/p/?LinkId=618935).
    -   Download the [WFP sample](https://go.microsoft.com/fwlink/p/?LinkId=618934). This is a functioning prototype that includes vSwitch capability.

4.  Write your extension.
    -   You can use one of the samples as a starting point, port existing filter code, or write your extension from scratch.
    -   If you’re developing an NDIS extension, you can use the standard NDIS INF with a few changes as outlined in [INF Requirements for Hyper-V Extensible Switch Extensions](inf-requirements-for-hyper-v-extensions.md).

5.  Build your extension and unit-test it.
    -   You must [use Visual Studio to build your extension](https://visualstudio.microsoft.com/vs/).
    -   You can familiarize yourself with the extension build process by using Visual Studio to compile and run the sample extensions.

6.  Learn about the Windows certification (logo) process for getting an extension signed.
    -   An extension must pass the tests in the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/).
    -   The requirements for an extension are listed under the Filter.Driver.vSwitchExtension.ExtensionRequirements in the [Windows Hardware Certification Requirements - Filter Driver](/previous-versions/windows/hardware/cert-program/windows-hardware-certification-requirements---filter-driver) .

7.  Set up your Windows Hardware Lab Kit environment.
    -   Download and install the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/).

8.  Run the WHCK tests for extensions:
    -   Filter.Driver.Fundamentals
    -   Filter.Driver.Security
    -   Filter.Driver.vSwitchExtension

9.  After your final extension passes WHCK certification, submit it to Microsoft.
    -   Your extension must be submitted as an MSI install package with a specific format to ensure that it can be tracked and deployed by management packages, such as [System Center Virtual Machine Manager (SCVMM) 2012](/previous-versions/technet-magazine/hh300651(v=msdn.10)). The MSI format is defined in [Extension Driver MSI Packaging Requirements](./extension-driver-msi-packaging-requirements.md).

10. List your extension on WindowsServerCatalog.com.
    -   List a brief description of your extension on WindowsServerCatalog.com.
    -   Information on listing a certified extension on WindowsServerCatalog.com will be available soon.
