---
title: DCH Design Principles and Best Practices
description: Describes DCH principles and best practices, including Declarative, Componentized, and Hardware Support App concepts.
ms.date: 06/20/2023
---

# DCH Design Principles and Best Practices

This page describes design principles and best practices for DCH-compliant driver packages.

## DCH Design Principles

There are three design principles to consider for a driver package to be DCH-compliant:

- Declarative **(D)**: Install the driver package by using only declarative INF directives. Don't include co-installers or RegisterDll functions.

- Componentized **(C)**: Edition-specific, OEM-specific, and optional customizations to the driver package are separate from the base driver package. As a result, the base driver package, which provides only core device functionality, can be targeted, flighted, and serviced independently from the customizations.

- Hardware Support App **(H)**: Any user interface (UI) component associated with a driver package must be packaged as a Hardware Support App (HSA) or preinstalled on the OEM device. An HSA is an optional device-specific app that's paired with a driver package. The application can be a [Universal Windows Platform (UWP)](/windows/uwp/get-started/universal-application-platform-guide) or [Desktop Bridge app](/windows/uwp/porting/desktop-to-uwp-root). You must distribute and update an HSA through the Microsoft Store. For details, see [Hardware Support App (HSA): Steps for driver developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md) and [Hardware Support App (HSA): Steps for app developers](../devapps/hardware-support-app--hsa--steps-for-app-developers.md).

The acronym "DCH" refers to the principles listed above. Please refer to the [DCH-Compliant Driver Package Example](dch-example.md) page to see how a driver sample can apply DCH design principles.

## Overview

Driver packages that are DCH-compliant contain an INF file and binaries that install and run on [Universal Windows Platform (UWP)-based editions of Windows](target-platforms.md). They also install and run on other editions of Windows 10 and 11 that share a common set of interfaces.

DCH-compliant driver binaries can use [KMDF](../wdf/index.md), [UMDF 2](../wdf/getting-started-with-umdf-version-2.md), or the Windows Driver Model (WDM).

DCH-compliant driver packages consist of the following parts:

- A base driver package
- Optional component packages
- An optional hardware support app

The base driver package contains all the core functionality and shared code. The optional component packages can contain customizations and additional settings.

Typically, a device manufacturer, or independent hardware vendor (IHV), writes the base driver package. Then, a system builder, or original equipment manufacturer (OEM), provides any optional component packages.

After an IHV has certified the base driver package, it can be deployed on all OEM systems. Because a base driver package can be used across all systems that share a hardware part, Microsoft can test the base driver package broadly via Windows Insider flighting, rather than limiting distribution to specific machines.

The OEM validates only the optional customizations that it provides for the OEM system.  

## Requirements

To create a driver package that follows DCH design principles, follow these steps:

*  Create an INF file for your driver package:
    1.  Review the [list of INF sections and directives that are valid in Universal driver packages](../install/using-a-universal-inf-file.md#which-inf-sections-are-invalid-in-a-universal-inf-file).
    2.  Use the [InfVerif](../devtest/infverif.md) tool to verify that your driver package's INF file follows Declarative (D) requirements.  It should pass `infverif /k`.
*  Ensure that any optional component packages that do not contain core driver functionality are separated from the base driver package.    
*  Hardware support applications associated with your driver package must be distributed through the Microsoft Store.

## Best practices

*  If you're using the Windows Driver Kit (WDK) with the latest available Visual Studio, set the **Target Platform** value in the driver project properties to `Universal`.  This automatically adds the correct libraries, and it runs the proper INF validation and ApiValidator as a part of build.  To do this:

    1. Open the driver project properties.
    2. Select **Driver Settings**.
    3. Use the drop-down menu to set **Target Platform** to `Universal`.
   
*  If your INF performs any custom setup actions that depend on the target platform, consider separating them out into an extension INF. You can update an extension INF independently from the base driver package to make it more robust and serviceable. For more information, see [Using an extension INF file](../install/using-an-extension-inf-file.md).
*  If you want to provide an application that works with your device, include a Hardware Support App. For more information, see [Hardware Support App (HSA): Steps for driver developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md).  An OEM can preload such an app by using [DISM - Deployment Image Servicing and Management](/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management-technical-reference-for-windows). Or, users can manually download the app from the Microsoft Store.
