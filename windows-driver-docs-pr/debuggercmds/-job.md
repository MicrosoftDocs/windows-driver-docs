---
title: job (WinDbg)
description: The job extension displays a job object.
keywords: ["job Windows Debugging"]
ms.date: 08/29/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- job
api_type:
- NA
---

# !job

The **!job** extension displays a job object.

```dbgcmd
!job [Process [Flags]] 
```

## Parameters

*Process*

Specifies the hexadecimal address of a process or a thread whose associated job object is to be examined. If this is omitted, or equal to zero, the job associated with the current process is displayed.

*Flags*

Specifies what the display should contain. This can be a sum of any of the following bit values. The default is 0x1:

Bit 0 (0x1)  
Causes the display to include job settings and statistics.

Bit 1 (0x2)  

Causes the display to include a list of all processes in the job.

### DLL

Kdexts.dll

### Additional Information

For information about job objects, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

Here is an example of the output from this extension:

```dbgcmd
kd> !process 52c
Searching for Process with Cid == 52c
PROCESS 8276c550  SessionId: 0  Cid: 052c    Peb: 7ffdf000  ParentCid: 0060
    DirBase: 01289000  ObjectTable: 825f0368  TableSize:  24.
    Image: cmd.exe
    VadRoot 825609e8 Vads 30 Clone 0 Private 77. Modified 0. Locked 0.
    DeviceMap e1733f38
    Token                             e1681610
    ElapsedTime                       0:00:12.0949
    UserTime                          0:00:00.0359
    .....
    CommitCharge                      109
    Job                               8256e1f0

kd> !job 8256e1f0
Job at ffffffff8256e1f0
  TotalPageFaultCount      0
  TotalProcesses           1
  ActiveProcesses          1
  TotalTerminatedProcesses 0
  LimitFlags               0
  MinimumWorkingSetSize    0
  MaximumWorkingSetSize    0
  ActiveProcessLimit       0
  PriorityClass            0
  UIRestrictionsClass      0
  SecurityLimitFlags       0
  Token                    00000000
```

 

 





