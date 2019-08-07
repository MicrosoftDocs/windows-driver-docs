---
ms.assetid: E109BD80-F9CB-4F1F-A6FD-1142E27EC6AD
title: Getting Started with Universal Windows drivers
description: Universal Windows drivers allow you to create one driver that runs on multiple device types, from embedded systems to tablets and PCs.
ms.date: 04/20/2018
ms.localizationpriority: medium
---

# Getting Started with Universal Windows drivers

Universal Windows drivers enable developers to create a single driver package that runs across multiple device types, from embedded systems to tablets to desktop PCs.

A Universal Windows driver package contains an INF file and binaries that install and run on [Universal Windows Platform (UWP) based editions of Windows 10](windows-10-editions-for-universal-drivers.md). They also install and run on other editions of Windows 10 that share a common set of interfaces.

The driver binary can use [KMDF](../wdf/index.md), [UMDF 2](../wdf/getting-started-with-umdf-version-2.md), or the Windows Driver Model (WDM).

A universal driver consists of the following parts:
- A base driver 
- Optional component packages 
- An optional hardware support app 

The base driver contains all core functionality and shared code. The optional component packages can contain customizations and additional settings.

Typically, a device manufacturer, or independent hardware vendor (IHV), writes the base driver. Then, a system builder, or original equipment manufacturer (OEM), provides any optional component packages.

After the IHV has certified the base driver, it can be deployed on all OEM systems. Because a base driver can be used across all systems that share a hardware part, Microsoft can test the base driver broadly by using Windows Insider *driver flighting* instead of limiting distribution to specific machines.

The OEM validates only the optional customizations that it provides for the OEM device.

Universal drivers are distributed through Windows Update, and hardware support apps are distributed through Microsoft Store.

## Design principles

When you write a universal driver package, there are four design principles to consider:

* Declarative **(D)**: Install the driver by using only declarative INF directives. Don't include any co-installers, RegisterDll functions, and the like.
* Componentized **(C)**: Edition-specific, OEM-specific, and optional customizations to the driver are separate from the base driver package. Therefore, the base driver, which provides only core device functionality, can be targeted, flighted, and serviced independently from the customizations.
* Hardware Support Apps **(H)**: Any user interface (UI) component associated with a universal driver must be packaged as a Hardware Support App (HSA) or preinstalled on the OEM device.  An HSA is an optional device-specific app that's paired with a driver. The application can be a [Universal Windows Platform (UWP)](https://docs.microsoft.com/windows/uwp/get-started/universal-application-platform-guide) or [Desktop Bridge](https://docs.microsoft.com/windows/uwp/porting/desktop-to-uwp-root) app.  You must distribute and update an HSA through the Microsoft Store.  For details, see [Hardware Support App (HSA): Steps for Driver Developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md) and [Hardware Support App (HSA): Steps for App Developers](../devapps/hardware-support-app--hsa--steps-for-app-developers.md).
* Universal API compliance **(U)**: Binaries in the universal driver package call only those APIs and DDIs that are included in UWP-based editions of Windows 10. These DDIs are marked as **Universal** on the corresponding documentation reference pages. INF files use only universal INF syntax.

In the documentation, we use the acronym **DCHU** to refer to the these principles. Later in this article, you'll find guidance on how to make your driver package DCHU-compliant.
Also check out [Universal Driver Scenarios](universal-driver-scenarios.md), which describes how the [DCHU universal driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU) applies the DCHU design principles.

## Requirements

When you write a universal driver package, make sure that you follow these steps:

*  Create a [universal INF file](../install/using-an-extension-inf-file.md) for your driver:
    1.  Review the [list of INF sections and directives that are valid in universal driver packages](../install/using-a-universal-inf-file.md#which-inf-sections-are-invalid-in-a-universal-inf-file).
    2.  Use the [InfVerif](../devtest/infverif.md) tool to verify that your driver package's INF file is universal.
*  Use the [ApiValidator tool](validating-universal-drivers.md) to verify that the APIs your binaries call are valid for a universal driver package.

## Best practices

*  If you're using the Windows Driver Kit (WDK) with Visual Studio, set the **Target Platform** value in the driver project properties to `Universal`.  This automatically adds the correct libraries, and it runs the Universal INF validation and APIValidator as a part of build.  To do this:

    1. Open the driver project properties.
    2. Select **Driver Settings**.
    3. Use the drop-down menu to set **Target Platform** to `Universal`.
    
*  If your INF performs any custom setup actions that depend on the target platform, consider separating them out into an extension INF. You can update an extension INF independently from the base driver package to make it more robust and serviceable. For more information, see [Using an extension INF file](../install/using-an-extension-inf-file.md).
*  If you want to provide an application that works with your device, include a UWP app. For more information, see [Hardware Support App (HSA): Steps for Driver Developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md).  An OEM can preload such an app by using [DISM - Deployment Image Servicing and Management](https://docs.microsoft.com/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management-technical-reference-for-windows). Or, users can manually download the app from the Microsoft Store.
*  In the [**INF DestinationDirs section**](../install/inf-destinationdirs-section.md), set the destination directories to [dirid 13](../install/using-dirids.md) to make the driver run from the [driver store](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/driver-store). This setting won't work for some devices.
*  Submit your universal driver package for certification in the Windows Hardware Compatibility Program. See the following topics for more details:

   *  [Create a new hardware submission](../dashboard/create-a-new-hardware-submission.md)
   *  [Managing hardware submissions in the Windows Hardware Dev Center dashboard](../dashboard/manage-your-hardware-submissions.md)
   *  [Get drivers signed by Microsoft for multiple Windows versions](../dashboard/get-drivers-signed-by-microsoft-for-multiple-windows-versions.md)
   *  [Driver flighting](../dashboard/driver-flighting.md)
