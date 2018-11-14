---
title: Bug Check 0x1CF HARDWARE_WATCHDOG_TIMEOUT  
description: The HARDWARE_WATCHDOG_TIMEOUT bug check has a value of 0x000001CF.
keywords: ["Bug Check 0x1CF HARDWARE_WATCHDOG_TIMEOUT",  "HARDWARE_WATCHDOG_TIMEOUT"]
ms.author: domars
ms.date: 05/23/2018
topic_type:
- apiref
api_name:
- HARDWARE_WATCHDOG_TIMEOUT 
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check Bug Check 0x1CF: HARDWARE\_WATCHDOG\_TIMEOUT 

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

The HARDWARE_WATCHDOG_TIMEOUT bug check has a value of 0x000001CF. This indicates that the system is hung and not processing timer ticks.


## HARDWARE\_WATCHDOG\_TIMEOUT Parameters
 
Parameter | Description 
|---------|--------------|
1 | The time since the watchdog was last reset, in interrupt time.
2 | The current interrupt time.
3 | The current QPC timestamp.
4 | The index of the clock processor.


 

 




