---
title: DCH Design Principles and Best Practices
description: Explore the DCH principles and best practices, including Declarative, Componentized, and Hardware Support App concepts.
ms.date: 07/14/2025
ms.topic: best-practice
---

# DCH design principles and best practices

This article describes design principles and best practices for DCH-compliant driver packages. DCH stands for Declarative **(D)**, Componentized **(C)**, and Hardware Support App **(H)**.

## DCH design principles

There are three design principles to consider for a driver package to be DCH-compliant:

- **Declarative**: Install the driver package by using only declarative INF directives. Don't include coinstallers or RegisterDll functions.

- **Componentized**: Edition-specific, OEM-specific, and optional customizations to the driver package are separate from the base driver package. As a result, the base driver package, which provides only core device functionality, can be targeted, flighted, and serviced independently from the customizations.

- **Hardware Support App (HSA)**: Any user interface (UI) component associated with a driver package must be packaged as an HSA or preinstalled on the OEM device. An HSA is an optional device-specific app paired with a driver package. The application can be a [Universal Windows Platform (UWP)](/windows/uwp/get-started/universal-application-platform-guide) or [Desktop Bridge app built with an MSIX package from your code](/windows/msix/desktop/source-code-overview). You must distribute and update an HSA through the Microsoft Store. For more information, see [HSA: Steps for driver developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md) and [HSA: Steps for app developers](../devapps/hardware-support-app--hsa--steps-for-app-developers.md).

To see how a driver sample can apply DCH design principles, see [DCH-compliant driver package example](dch-example.md).

## Overview of DCH

Driver packages that are DCH-compliant contain an INF file and binaries that install and run on [UWP-based editions of Windows](target-platforms.md). They also install and run on other editions of Windows 10 and 11 that share a common set of interfaces.

DCH-compliant driver binaries can use [Kernel-Mode Driver Framework (KMDF)](../wdf/index.md), [ User-Mode Driver Framework 2 (UMDF)](../wdf/getting-started-with-umdf-version-2.md), or the Windows Driver Model (WDM).

DCH-compliant driver packages consist of the following parts:

- A base driver package
- Optional component packages
- An optional hardware support app

The base driver package contains all the core functionality and shared code. The optional component packages can contain customizations and other settings.

Typically, a device manufacturer, or independent hardware vendor (IHV), writes the base driver package. Then, a system builder, or original equipment manufacturer (OEM), provides any optional component packages.

After an IHV certifies the base driver package, it can be deployed on all OEM systems. Because a base driver package can be used across all systems that share a hardware part, Microsoft can test the base driver package broadly. Microsoft can use Windows Insider flighting, rather than limiting distribution to specific machines.

The OEM validates only the optional customizations that it provides for the OEM system.  

## DCH requirements

To create a driver package that follows DCH design principles, follow these steps:

1. Create an INF file for your driver package:

   1. Review the [list of INF sections and directives that are valid in Universal driver packages](../install/using-a-universal-inf-file.md#which-inf-sections-are-invalid-in-a-universal-inf-file).
   
   1. Use the [InfVerif](../devtest/infverif.md) tool to verify that your driver package's INF file follows Declarative (D) requirements. The package should pass the check by the `infverif /k` command.

1. Ensure that any optional component packages that don't contain core driver functionality are separated from the base driver package. 

1. Hardware support apps associated with your driver package must be distributed through the Microsoft Store.

## DCH best practices

When you develop for DCH-compliance, follow these best practices:

* If you use the Windows Driver Kit (WDK) with the latest version of Visual Studio, set the **Target Platform** value in the driver project properties to `Universal`. This setting automatically adds the correct libraries, and runs the proper INF validation and ApiValidator as a part of build. To complete this task, follow these steps:

   1. Open the driver project properties.
   1. Select **Driver Settings**.
   1. Use the drop-down menu to set the **Target Platform** value to `Universal`.

* If your INF performs any custom setup actions that depend on the target platform, consider separating the actions into an extension INF. You can update an extension INF independently from the base driver package to make it more robust and serviceable. For more information, see [Using an extension INF file](../install/using-an-extension-inf-file.md).

* If you want to provide an application that works with your device, include an HSA. For more information, see [HSA: Steps for driver developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md). An OEM can preload an HSA app by using [Deployment Image Servicing and Management (DISM)](/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management-technical-reference-for-windows), or, users can manually download the app from the Microsoft Store.
