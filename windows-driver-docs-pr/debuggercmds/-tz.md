---
title: tz (WinDbg)
description: The tz extension displays the specified power thermal zone structure.
keywords: ["thermal zone", "tz Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- tz
api_type:
- NA
---

# !tz


The **!tz** extension displays the specified power thermal zone structure.

```dbgcmd
!tz [Address]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The address of a power thermal zone that you want to display. If this parameter is omitted, the display includes all thermal zones on the target computer.

### DLL

Kdexts.dll

 

### Additional Information

To view the system's power capabilities, use the [**!pocaps**](-pocaps.md) extension command. To view the system's power policy, use the [**!popolicy**](-popolicy.md) extension command. For information about power capabilities and power policy, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

To stop execution at any time, press CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





