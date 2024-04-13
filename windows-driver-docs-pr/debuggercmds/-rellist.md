---
title: "!rellist (WinDbg)"
description: "The !rellist extension displays a Plug and Play relation list."
keywords: ["!rellist Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rellist
api_type:
- NA
---

# !rellist

The **!rellist** extension displays a Plug and Play relation list.

```dbgcmd
!rellist Address [Flags] 
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the relation list.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies additional information to include in the display. This can be any combination of the following bits (the default is zero):

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include the CM\_RESOURCE\_LIST. The display also includes the boot resources list, if it is available.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the display to include the resource requirements list (IO\_RESOURCE\_LIST).

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Causes the display to include the translated CM\_RESOURCE\_LIST.

### DLL

Kdexts.dll

## Additional Information

See [Plug and Play Debugging](../debugger/plug-and-play-debugging.md) for applications of this extension command. For information about these list structures, see the Windows Driver Kit (WDK) documentation.
