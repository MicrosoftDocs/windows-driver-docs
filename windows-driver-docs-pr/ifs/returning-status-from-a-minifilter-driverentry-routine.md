---
title: Returning Status from a Minifilter DriverEntry Routine
description: Returning Status from a Minifilter DriverEntry Routine
ms.assetid: a9448908-f712-43f7-99c0-e02abc1678ed
keywords:
- status values WDK file system
- returning status WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Status from a Minifilter DriverEntry Routine


## <span id="ddk_returning_status_from_a_minifilter_driverentry_routine_if"></span><span id="DDK_RETURNING_STATUS_FROM_A_MINIFILTER_DRIVERENTRY_ROUTINE_IF"></span>


A minifilter driver's **DriverEntry** routine normally returns STATUS\_SUCCESS. But if minifilter initialization fails, the **DriverEntry** routine should return an appropriate error NTSTATUS value.

If the **DriverEntry** routine returns a status value that is not a success NTSTATUS value, the system responds by unloading the minifilter driver. The minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine is not called. For this reason, the **DriverEntry** routine must free any memory that was allocated for system resources before returning a status value that is not a success NTSTATUS value.

 

 




