---
title: Bug Check 0xCB DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS
description: The DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS bug check has a value of 0x000000CB. This indicates that a driver or the I/O manager failed to release locked pages after an I/O operation.
keywords: ["Bug Check 0xCB DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS", "DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS"]
ms.date: 10/04/2022
topic_type:
- apiref
api_name:
- DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS
api_type:
- NA
---

# Bug Check 0xCB: DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS

The DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS bug check has a value of 0x000000CB. This indicates that a driver or the I/O manager failed to release locked pages after an I/O operation.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS Parameters

|Parameter|Description|
|--- |--- |
|1| The address of the internal lock tracking structure.|
|2| 0  (Reserved) |
|3| Address of the MDL containing the locked pages. |
|4| Number of locked pages |
 
For more information about memory descriptor list, see the following topics: 

- [Using MDLs](../kernel/using-mdls.md)
- [MDL structure (wdm.h)](/windows-hardware/drivers/ddi/wdm/ns-wdm-_mdl)

For more information on locking memory, see [Locking Pageable Code or Data](../kernel/locking-pageable-code-or-data.md).

To research the cause of this bug check, use the [!lockedpages](-lockedpages.md) debugger extension to display all of the locked MDLs for the current process.

## Remarks

This bug check is issued only if the registry value  is equal to DWORD 1. 

**\\\\HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\TrackLockedPages**

If this value is not set, the system will issue the less-informative [**bug check 0x76**](bug-check-0x76--process-has-locked-pages.md) (PROCESS\_HAS\_LOCKED\_PAGES).

This bug check can also be issued by Driver Verifier when the Pool Tracking option is enabled. For more information, see [Pool Tracking](../devtest/pool-tracking.md).