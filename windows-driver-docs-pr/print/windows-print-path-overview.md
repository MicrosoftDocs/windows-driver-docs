---
title: Windows Print Path Overview
description: Windows Print Path Overview
ms.assetid: c06e122b-a4d8-4b3a-9db0-0bc8f2728177
keywords:
- XPSDrv printer drivers WDK , print paths
- print paths WDK XPSDrv
- GDI print path WDK XPSDrv
- XPS print path WDK XPSDrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Print Path Overview

Windows provides two primary print paths and two additional conversion paths. The two primary print paths are:

-   GDI print path (similar to the Windows Server 2003 print path). This path is also called the Win32 path and originates in a Win32 application by using the GDI graphic API.

-   XPS print path. This path originates in a Windows Presentation Foundation (WPF) application or from the XPS Print API.

The two conversion options are:

-   GDI-to-XPS conversion (MXDC).

-   XPS-to-GDI conversion (XGC).

### General Data Flow

The following illustration shows the different print path and conversion options of the XPSDrv subsystem.

![diagram illustrating the different print-path and conversion options of the xpsdrv subsystem](images/printpathoverview.png)

For more information about configuring the filter pipeline service, see [Filter Pipeline Configuration File](filter-pipeline-configuration-file.md).

For more information about configuring the Version 3 Print Driver for Windows Vista and later versions of Windows, see [Version 3 XPSDrv Print Driver Components](version-3-xpsdrv-print-driver-components.md).
