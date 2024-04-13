---
title: "!wdfkd.wdfusbinterface"
description: "The !wdfkd.wdfusbinterface extension displays information about a specified Kernel-Mode Driver Framework (KMDF) USB interface object, including its possible and current settings."
keywords: ["!wdfkd.wdfusbinterface Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfusbinterface
api_type:
- NA
---

# !wdfkd.wdfusbinterface

The **!wdfkd.wdfusbinterface** extension displays information about a specified Kernel-Mode Driver Framework (KMDF) USB interface object, including its possible and current settings.

```dbgcmd
!wdfkd.wdfusbinterface Handle [Flags]
```

## Parameters

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFUSBINTERFACE-typed USB interface object.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. A hexadecimal value that modifies the kind of information to return. The default value is 0x0. Flags can be any combination of the following bits:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
The display will include the properties of the I/O target for each KMDF USB pipe object.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).
