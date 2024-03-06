---
title: pocaps (WinDbg)
description: The pocaps extension displays the power capabilities of the target computer.
keywords: ["pocaps Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pocaps
api_type:
- NA
---

# !pocaps


The **!pocaps** extension displays the power capabilities of the target computer.

```dbgcmd
!pocaps
```

## <span id="ddk__pocaps_dbg"></span><span id="DDK__POCAPS_DBG"></span>


### DLL

Kdexts.dll

 

### Additional Information

To view the system's power policy, use the [**!popolicy**](-popolicy.md) extension command. For information about power capabilities and power policy, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

Here is an example of this command's output:

```dbgcmd
kd> !pocaps
PopCapabilities @ 0x8016b100
  Misc Supported Features:  S4 FullWake
  Processor Features:      
  Disk Features:            SpinDown
  Battery Features:        
  Wake Caps
    Ac OnLine Wake:         Sx
    Soft Lid Wake:          Sx
    RTC Wake:               Sx
    Min Device Wake:        Sx
    Default Wake:           Sx
```

 

 





