---
title: "!wdfkd.wdfchildlist"
description: "The !wdfkd.wdfchildlist extension displays a child list's state and information about all of the device identification descriptions that are in the child list."
keywords: ["!wdfkd.wdfchildlist Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfchildlist
api_type:
- NA
---

# !wdfkd.wdfchildlist

The **!wdfkd.wdfchildlist** extension displays a child list's state and information about all of the device identification descriptions that are in the child list.

```dbgcmd
!wdfkd.wdfchildlist Handle 
```

## Parameters

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A WDFCHILDLIST-typed handle to the child list.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

The following example shows a **!wdfkd.wdfchildlist** display.

```dbgcmd
kd> !wdfchildlist 0x7cc090c8 

## Dumping WDFCHILDLIST 0x7cc090c8
---------------------------------------
owning !WDFDEVICE 0x7ca7b1c0
ID description size 0x8

State:
-----
List is unlocked, changes will be applied immediately
No scans or enumerations are active on the list

Descriptions:
------------
 PDO !WDFDEVICE 0x7cad31c8, ID description 0x83ac4ff4
 +Device WDM !devobj 0x81fb00e8, WDF pnp state WdfDevStatePnpStarted (0x119)
 +Device found in last scan

No pending insertions are in the list.

Callbacks:
---------
 EvtChildListCreateDevice:  wdfrawbusenumtest!RawBus_RawPdo_Create (f22263b0)
```
