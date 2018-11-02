---
title: INF Files
description: INF Files
ms.assetid: 8557a072-1b08-41f9-8c35-976a96ff639c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Files


Windows uses setup information (INF) files to install the following components for a device:

-   One or more drivers that support the device.

-   Device-specific configuration or settings to bring the device online.

You can use an *INX* file to automatically create an INF file. An INX file is an INF file that contains string variables that represent version information. The Build utility and the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool replace the string variables in INX files with text strings that represent a specific hardware architecture or framework version. For more information about INX files, see [Using INX Files to Create INF Files](https://msdn.microsoft.com/library/windows/hardware/ff545473).

This section includes the following topics:

-   [Overview of INF Files](overview-of-inf-files.md)
-   [Accessing INF Files from a Device Installation Application](accessing-inf-files-from-a-setup-application.md)
-   [Providing Vendor Icons for the Shell and AutoPlay](providing-vendor-icons-for-the-shell-and-autoplay.md)

 

 





