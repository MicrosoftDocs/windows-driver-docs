---
title: .time (Display System Time)
description: The .time command displays information about the system time variables.
keywords: ["Display System Time (.time) command", ".time (Display System Time) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .time (Display System Time)
api_type:
- NA
---

# .time (Display System Time)


The **.time** command displays information about the system time variables.

```dbgcmd
.time [-h Hours]
```

## <span id="ddk_meta_display_system_time_dbg"></span><span id="DDK_META_DISPLAY_SYSTEM_TIME_DBG"></span>Parameters


<span id="_______-h________Hours______"></span><span id="_______-h________hours______"></span><span id="_______-H________HOURS______"></span> **-h** **** *Hours*   
Specifies the offset from Greenwich Mean Time, in hours. A negative value of *Hours* must be enclosed in parentheses.

<span></span>  

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode, kernel mode|
|Targets|Live, crash dump|
|Platforms|All|

 

## Remarks

The system time variables control performance counter behavior.

Here is an example in kernel mode:

```dbgcmd
kd> .time
Debug session time: Wed Jan 31 14:47:08 2001
System Uptime: 0 days 2:53:56 
```

Here is an example in user mode:

```dbgcmd
0:000> .time
Debug session time: Mon Apr 07 19:10:50 2003
System Uptime: 4 days 4:53:56.461
Process Uptime: 0 days 0:00:08.750
  Kernel time: 0 days 0:00:00.015
  User time: 0 days 0:00:00.015
```

 

 





