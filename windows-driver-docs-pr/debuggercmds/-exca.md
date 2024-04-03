---
title: "!exca (WinDbg)"
description: "The !exca extension displays PC-Card Interrupt Controller (PCIC) Exchangable Card Architecture (ExCA) registers."
keywords: ["PCIC (PC Card Interrupt Controller)", "ExCA registers", "!exca Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- exca
api_type:
- NA
---

# !exca

The **!exca** extension displays PC-Card Interrupt Controller (PCIC) Exchangable Card Architecture (ExCA) registers.

```dbgcmd
!exca BasePort.SocketNumber
```

## <span id="ddk__exca_dbg"></span><span id="DDK__EXCA_DBG"></span>Parameters


<span id="_______BasePort______"></span><span id="_______baseport______"></span><span id="_______BASEPORT______"></span> *BasePort*   
Specifies the base port of the PCIC.

<span id="_______SocketNumber______"></span><span id="_______socketnumber______"></span><span id="_______SOCKETNUMBER______"></span> *SocketNumber*   
Specifies the socket number of the ExCA register on the PCIC.

## DLL

Kext.dll

 

The **!exca** extension is only available for an x86-based target computer.

## Additional Information

The [**!cbreg**](-cbreg.md) extension can be used to display CardBus Socket registers and CardBus ExCA registers by address.

