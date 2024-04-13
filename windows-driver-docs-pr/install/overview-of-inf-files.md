---
title: Overview of INF Files
description: Overview of INF Files
keywords:
- INF files WDK device installations
- INF files WDK device installations , creating
- Device setup WDK device installations , INF files
- device installations WDK , INF files
- installing devices WDK , INF files
- Install a driver by using an INF file
ms.date: 01/13/2022
---

# Overview of INF Files

A setup information (INF) file is a text file in a [driver package](driver-packages.md) that contains all of the information that device installation components use to install a driver package on a device. Windows uses INF files to install the following components for a device:

-   One or more drivers that support the device.

-   Device-specific configuration or settings to bring the device online.

You can use an *INX* file to automatically create an INF file. An INX file is an INF file that contains string variables that represent certain information such as version information, architecture the INF is built for, and current WDF version. The Build utility and the [Stampinf](../devtest/stampinf.md) tool replace the string variables in INX files with text strings that represent a specific hardware architecture or framework version. For more information about INX files, see [Using INX Files to Create INF Files](../wdf/using-inx-files-to-create-inf-files.md).


See [INF File Sections](inf-classinstall32-section.md) and [INF File Directives](inf-addcomponent-directive.md) for a complete description of the INF file format.
