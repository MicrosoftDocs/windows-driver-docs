---
title: Bug Check 0x102 DPC_WATCHDOG_TIMEOUT
description: The DPC_WATCHDOG_TIMEOUT bug check has a value of 0x00000102. This indicates that The DPC watchdog routine was not executed within the allocated time interval.
ms.assetid: 1BEC2701-3127-4FB9-AD0F-DD54A9F2C2C3
keywords: ["Bug Check 0x102 DPC_WATCHDOG_TIMEOUT", "DPC_WATCHDOG_TIMEOUT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DPC_WATCHDOG_TIMEOUT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x102: DPC\_WATCHDOG\_TIMEOUT


The DPC\_WATCHDOG\_TIMEOUT bug check has a value of 0x00000102. This indicates that The DPC watchdog routine was not executed within the allocated time interval.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DPC\_WATCHDOG\_TIMEOUT Parameters


| Parameter | Description                                            |
|-----------|--------------------------------------------------------|
| 1         | DPC watchdog time out interval in nominal clock ticks. |
| 2         | The PRCB address of the hung processor.                |
| 3         | Reserved                                               |
| 4         | Reserved                                               |

 

Cause
-----

This bug check typically means that either an ISR is hung at an IRQL that is below clock level and above dispatch level, or a DPC routine is hung on the specified processor.

For example for StorPort Miniport drivers, StorPort.sys handles I/O completions in a routine that runs at DISPATCH\_LEVEL and that serially calls the I/O completion routines of all IRPs that have just completed. If I/O completion routines singly or together take too much time, the keyboard and/or mouse may stop responding. It is also possible that the Windows DPC Watchdog timer routine will decide that the StorPort routine has taken excessive time to finish.

Resolution
----------

A kernel driver in the storage stack can reduce the problem's likelihood by efficient coding of the driver's I/O completion routine. If it is still not possible to do all necessary processing in the completion routine in enough time, the routine can create a work element for the I/O work, queue up the element to a work queue and return STATUS\_MORE\_PROCESSING\_REQUIRED; a worker thread of the driver should then find the work element, do the work and do IoCallerDriver for the IRP to ensure the IRP's further I/O processing.

 

 




