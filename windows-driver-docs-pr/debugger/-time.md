---
title: time (WinDbg)
description: time
keywords: ["time extension (obsolete)"]
ms.date: 06/11/2021
---

# !time


## <span id="ddk__time_dbg"></span><span id="DDK__TIME_DBG"></span>


The **!time** extension command displays information about the system time and interrupt time and can operate on explicit time stamps and the current time.

### Environment


|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

Here is an example in user mode:

```dbgcmd
0:000> !time
CURRENT TIME:
System:               01d75f1c`8588b6ee (2021 Jun 11 23:50:13.477)
Interrupt:            0000020e`22112c46 (2 days, 14:46:12.434)
```

## See also

[.time (Display System Time)](-time--display-system-time-.md)

[.echotime (Show Current Time)](-echotime--show-current-time-.md)

[.echotimestamps (Show Time Stamps)](-echotimestamps--show-time-stamps-.md)

[!runaway](-runaway.md)
 

 





