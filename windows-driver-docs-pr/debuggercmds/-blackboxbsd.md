---
title: blackboxbsd
description: The blackboxbsd extension displays the secondary boot information for Boot Status Data (BSD).
keywords: ["blackboxbsd Windows Debugging"]
ms.date: 12/06/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- blackboxbsd
api_type:
- NA
---

# !blackboxbsd

The **!blackboxbsd** extension displays cached Boot Status Data (BSD) information when it is available in a kernel mode dump file.   The information is retrieved from cached data in the kernel mode dump which was saved at the time the bugcheck occurred, and may not always be available.

Syntax

```dbgcmd
!blackboxbsd  
```

## <span id="Parameters"></span>Parameters
*None*   


## <span id="DLL"></span><span id="dll"></span>DLL

ext.dll


## <span id="Remarks"></span>Remarks

Driver developers can add secondary boot information to dump files. Driver developers (and the OS) can decide when to add this information to the dump file. This means that not all kernel mode dump files will contain secondary boot information. For more information, see [Writing a Bug Check Reason Callback Routine](../kernel/writing-a-bug-check-callback-routine.md).

### Example Command Output

```dbgcmd
0: kd> !ext.blackboxbsd
Version: 136
Product type: 1

Auto advanced boot: FALSE
Advanced boot menu timeout: 30
Last boot succeeded: TRUE
Last boot shutdown: FALSE
Sleep in progrees: FALSE

Power button timestamp: 0
System running: TRUE
Connected standby in progress: FALSE
User shutdown in progress: FALSE
System shutdown in progress: FALSE
Sleep in progress: 6
Connected standby scenario instance id: 5
Connected standby entry reason: 12
Connected standby exit reason: 31
System sleep transitions to on: 8
Last reference time: 0x1d3645f716b79e3
Last reference time checksum: 0xb6ae84b7
Last update boot id: 6

Boot attempt count: 1
Last boot checkpoint: TRUE
Checksum: 0x7f
Last boot id: 6
Last successful shutdown boot id: 2
Last reported abnormal shutdown boot id: 5

Error info boot id: 0
Error info repeat count: 0
Error info other error count: 0
Error info code: 0
Error info other error count: 0

Power button last press time: 0x1d365b105eb9e3b
Power button cumulative press count: 6
Power button last press boot id: 6
Power button last power watchdog stage: 0x20
Power button watchdog armed: FALSE
Power button shutdown in progress: FALSE
Power button last release time: 0x1d36112993b1191
Power button cumulative release count: 5
Power button last release boot id: 6
Power button error count: 0
Power button current connected standby phase: 1
Power button transition latest checkpoint id: 9
Power button transition latest checkpoint type: 0
Power button transition latest checkpoint sequence number: 77
```

 
