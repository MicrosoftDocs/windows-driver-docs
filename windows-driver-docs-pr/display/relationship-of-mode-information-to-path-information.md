---
title: Relationship of Mode Information to Path Information
description: Relationship of Mode Information to Path Information
ms.assetid: 214717dd-1c01-4daf-9296-586299668d3a
keywords:
- connecting displays WDK Windows 7 display , CCD concepts, mode and path information
- connecting displays WDK Windows Server 2008 R2 display , CCD concepts, mode and path information
- configuring displays WDK Windows 7 display , CCD concepts, mode and path information
- configuring displays WDK Windows Server 2008 R2 display , CCD concepts, mode and path information
- CCD concepts WDK Windows 7 display , mode and path information
- CCD concepts WDK Windows Server 2008 R2 display , mode and path information
- mode and path information WDK Windows 7 display
- mode and path information WDK Windows Server 2008 R2 display
- path and mode information WDK Windows 7 display
- path and mode information WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Relationship of Mode Information to Path Information


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) CCD function always returns path information and source and target mode information for a particular display configuration. The following figure shows an example of how the source and target mode information relates to the path information. In this example, the QDC\_ALL\_PATHS flag was passed to the *Flags* parameter in the call to **QueryDisplayConfig**.

![diagram illustrating the relationship of mode information to path information](images/displayconfigpathandmode.png)

 

 





