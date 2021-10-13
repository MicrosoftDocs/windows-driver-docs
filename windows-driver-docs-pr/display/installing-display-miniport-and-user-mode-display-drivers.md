---
title: Installing Display Miniport and User-Mode Display Drivers
description: Installation Requirements for Display Miniport and User-Mode Display Drivers
keywords:
- display driver model WDK Windows Vista , driver installations
- Windows Vista display driver model WDK , driver installations
- display driver model WDK Windows Vista , installing
- user-mode drivers WDK display
- INF files WDK display
- graphics device display miniport drivers WDK Windows Vista
- INF files WDK display , about driver installations
- miniport drivers WDK display , installing
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Installation Requirements for Display Miniport and User-Mode Display Drivers


A display miniport driver for a graphics device is installed on the operating system by using an INF file that is marked as **Class=Display**. This INF will be interpreted by the system-supplied display class installer during driver installation.

The INF file of the graphics device's display miniport driver for Windows Vista and later must store all software settings under the [**DDInstall section**](../install/inf-ddinstall-section.md). Doing so causes the operating system to copy all registry values to the Plug and Play (PnP) software key in the registry.

To ensure proper installation, the following information must be supplied in the INF file of any display miniport driver that conforms to the Windows Display Driver Model (WDDM).

[Setting the Driver Control Flags](setting-the-driver-control-flags.md)

[Adding Software Registry Settings](adding-software-registry-settings.md)

[Adding User-Mode Display Driver Names to the Registry](adding-user-mode-display-driver-names-to-the-registry.md)

[Loading a User-Mode Display Driver](loading-a-user-mode-display-driver.md)

[Setting the Driver Feature Score](setting-the-driver-feature-score.md)

[Setting a Copy-File Flag to Support PnP Stop](setting-a-copy-file-flag-to-support-pnp-stop.md)

[Setting the Start Type Value](setting-the-start-type-value.md)

[Disabling Interoperability with OpenGL](disabling-interoperability-with-opengl.md)

[Appending Information to the Friendly String Names of Graphics Adapters](appending-information-to-the-friendly-string-names-of-graphics-adapter.md)

[Omitting LayoutFile and CatalogFile Information](omitting-layoutfile-and-catalogfile-information.md)

[Identifying Source Disks and Files](identifying-source-disks-and-files.md)

[General x64 INF Information](general-x64-inf-information.md)

[General Install Information](general-install-information.md)

[Overriding Monitor EDIDs with an INF](overriding-monitor-edids.md)

You should refer to the [Overview of INF Files](../install/overview-of-inf-files.md) and [INF File Sections and Directives](../install/index.md) sections for general help in creating a display miniport driver INF file. For more information about registry root identifiers, such as **HKR**, see [**INF AddReg Directive**](../install/inf-addreg-directive.md).

**Note**   There are no INF sections and directives for uninstalling display drivers that are specific to graphic devices.

 

