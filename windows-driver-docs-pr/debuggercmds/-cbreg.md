---
title: "!cbreg (WinDbg)"
description: "The !cbreg extension displays CardBus Socket registers and CardBus Exchangable Card Architecture (ExCA) registers."
keywords: ["CardBus", "ExCA registers", "!cbreg Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- cbreg
api_type:
- NA
---

# !cbreg


The **!cbreg** extension displays CardBus Socket registers and CardBus Exchangable Card Architecture (ExCA) registers.

```dbgsyntax
    !cbreg [%%]Address 
```

## <span id="ddk__cbreg_dbg"></span><span id="DDK__CBREG_DBG"></span>Parameters


<span id="_______________"></span> **%%**   
Indicates that *Address* is a physical address rather than a virtual address.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the register to be displayed.

## DLL

Kext.dll

 

The **!cbreg** extension is only available for an x86-based target computer.

## Additional Information

The [**!exca**](-exca.md) extension can be used to display PCIC ExCA registers by socket number.

