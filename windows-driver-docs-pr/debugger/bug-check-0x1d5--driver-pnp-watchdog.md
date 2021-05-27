---
title: Bug Check 0x1D5 DRIVER_PNP_WATCHDOG
description: The DRIVER_PNP_WATCHDOG bug check has a value of 0x000001D5. A system wide watchdog has expired. This indicates that driver has failed to complete a PnP operation within a specific time.
keywords: ["Bug Check 0x1D5 DRIVER_PNP_WATCHDOG", "DRIVER_PNP_WATCHDOG"]
ms.date: 01/11/2019
topic_type:
- apiref
api_name:
- DRIVER_PNP_WATCHDOG
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1D5: DRIVER\_PNP\_WATCHDOG

The DRIVER\_PNP\_WATCHDOG bug check has a value of 0x000001D5. This indicates that a driver has failed to complete a PnP operation within a specific time.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## DRIVER\_PNP\_WATCHDOG Parameters

|Parameter|Description|
|-------- |---------- |
|1| First few character of the service associated with the devnode.|
|2| Pointer to the nt!TRIAGE_PNP_WATCHDOG on Win10 RS4 and higher. |
|3| Thread responsible for the PnP Watchdog.|
|4| Milliseconds elapsed since the watchdog was armed. |


## ## Cause

This indicates that a driver has failed to complete a PnP operation within a specific time. The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

