---
title: wdfkd.wdfusbpipe
description: The wdfkd.wdfusbpipe extension displays information about a Kernel-Mode Driver Framework (KMDF) USB pipe object's I/O target.
keywords: ["wdfkd.wdfusbpipe Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfusbpipe
api_type:
- NA
---

# !wdfkd.wdfusbpipe


The **!wdfkd.wdfusbpipe** extension displays information about a Kernel-Mode Driver Framework (KMDF) USB pipe object's I/O target.

```dbgcmd
!wdfkd.wdfusbpipe Handle [Flags]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFUSBPIPE-typed USB pipe object.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. A hexadecimal value that modifies the kind of information to return. The default value is 0x0. Flags can be any combination of the following bits:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
The display will include the properties of the I/O target.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

 

 





