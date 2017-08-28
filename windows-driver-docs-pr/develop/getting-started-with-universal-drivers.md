---
ms.assetid: E109BD80-F9CB-4F1F-A6FD-1142E27EC6AD
title: Getting Started with Universal Windows drivers
description: Universal Windows drivers allow you to create one driver that runs on multiple device types, from embedded systems to tablets and PCs.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Getting Started with Universal Windows drivers

Universal Windows drivers enable developers to create a single driver package that runs across multiple different device types, from embedded systems to tablets and desktop PCs.

A Universal Windows driver is a driver package that contains an INF file and binaries that will install and run on Universal Windows Platform (UWP) based editions of Windows 10, such as Windows 10 for desktop editions (Home, Pro, and Enterprise), Windows 10 S, Windows 10 Mobile, Windows 10 IoT Core, Windows Server 2016, as well as other Windows 10 editions that share a common set of interfaces.

A Universal INF file is an INF file that only uses the [subset of INF syntax](../install/using-a-universal-inf-file.md#which-inf-sections-are-invalid-in-a-universal-inf-file) that is supported on [UWP-based editions of Windows 10](windows-10-editions-for-universal-drivers.md).

Any binaries referenced by the Universal INF file must use only device driver interfaces (DDI) that are included in [UWP-based editions of Windows 10](windows-10-editions-for-universal-drivers.md).  These DDIs are marked as **Universal** on the corresponding documentation reference pages.  The driver binary can use [KMDF](../wdf/index.md), [UMDF 2](../wdf/getting-started-with-umdf-version-2.md) or the Windows Driver Model (WDM).

Other binaries contained in your Universal Windows driver must pass the [API validation tests](../devtest/infverif.md).

## Design Principles

When you write a universal driver package, there are four design principles to consider:

*  Declarative: Use directives in the INF file for installation operations and not extension points such as co-installers, RegisterDlls, etc.
*  Componentized: System and/or OEM-specific customizations are in an [extension INF](../install/using-an-extension-inf-file.md) driver package separate from the primary driver package, facilitating independent updates of different components owned by different organizations.
*  Hardware Support Apps (HSA): Use [custom capabilities](../devapps/creating-a-custom-capability-to-pair-driver-with-hsa.md) to associate a hardware-specific UWP (Universal Windows Platform) application with your driver.  The resulting app can be delivered and serviced from the Windows Store.
*  Universal API compliance: Binaries in the universal driver package only call APIs and DDIs that are included in the OneCore subset.  INF files use only universal INF syntax.

Below, you'll find requirements and recommendations related to these principles.  Also check out [Universal Driver Scenarios](universal-driver-scenarios.md), which describes how the [DCHU universal driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU) applies the DCHU design principles.

## Requirements

The following are required when writing a universal driver package:

*  Create a universal INF file for your driver:
    1.  Review the list of INF sections and directives that are valid in universal driver packages in [Using a Universal INF File](../install/using-a-universal-inf-file.md#which-inf-sections-are-invalid-in-a-universal-inf-file).
    2.  Use the [InfVerif](../devtest/infverif.md) tool to verify that your driver package's INF file is universal.
*  Use the ApiValidator tool to verify that the APIs your binaries call are valid for a universal driver package.  See [Validating Universal Windows drivers](validating-universal-drivers.md).

## Best Practices

Use the following best practices:

*  If you are using the WDK with Visual Studio, set the **Target Platform** value in the driver project properties to `Universal`.  This will automatically pull in the correct libraries, as well as running the Universal INF validation and APIValidator as a part of build.  To do this:

    1. Open the driver project properties.
    2. Select **Driver Settings**.
    3. Use the drop-down menu to set **Target Platform** to `Universal`.
    
*  If your INF performs any custom setup actions that depend on the target platform, consider separating them out into an extension INF.  You can update an extension INF independently from the primary driver package to improve robustness and servicing.  See [Using an Extension INF File](../install/using-an-extension-inf-file.md).
*  If you would like to provide an application that works with your device, please provide a UWP app.  For details, see [Hardware access for Universal Windows Platform apps](../devapps/hardware-access-for-universal-windows-platform-apps.md).  In Windows 10, version 1703, the OEM needs to pre-load such an app using [DISM - Deployment Image Servicing and Management](https://docs.microsoft.com/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management-technical-reference-for-windows).  Alternatively, users can manually download the app from the Windows Store.
*  In [**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md), set the destination directories to 13 to make the driver run from the Driver Store.  This will not work for some devices.
