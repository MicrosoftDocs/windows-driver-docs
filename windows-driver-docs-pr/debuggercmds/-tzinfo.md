---
title: tzinfo (WinDbg)
description: The tzinfo extension displays the contents of the specified thermal zone information structure.
keywords: ["thermal zone information", "tzinfo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- tzinfo
api_type:
- NA
---

# !tzinfo


The **!tzinfo** extension displays the contents of the specified thermal zone information structure.

```dbgcmd
!tzinfo Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The address of a thermal zone information structure that you want to display.

### DLL

Kdexts.dll

 

### Additional Information

To view the system's power capabilities, use the [**!pocaps**](-pocaps.md) extension command. To view the system's power policy, use the [**!popolicy**](-popolicy.md) extension command. For information about power capabilities and power policy, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

 

 





