---
title: Returning Status
description: Returning Status
ms.assetid: fd490517-f4c5-4e20-9eac-6a9ac7d04992
keywords:
- status values WDK file system
- success status values WDK file system
- returning status WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Status


## <span id="ddk_returning_status_if"></span><span id="DDK_RETURNING_STATUS_IF"></span>


A file system filter driver's **DriverEntry** routine normally returns STATUS\_SUCCESS. However, if driver initialization fails, the **DriverEntry** routine should return an appropriate error status value.

If the **DriverEntry** routine returns a status value that is not a success status value, the system responds by unloading the driver. For this reason, the **DriverEntry** routine must always free any memory that was allocated for system resources, such as device objects, before returning a status value that is not a success status value.

 

 




