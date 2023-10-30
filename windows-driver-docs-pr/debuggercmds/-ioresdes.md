---
title: ioresdes (WinDbg)
description: The ioresdes extension displays the IO_RESOURCE_DESCRIPTOR structure at the specified address.
keywords: ["ioresdes Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ioresdes
api_type:
- NA
---

# !ioresdes


The **!ioresdes** extension displays the IO\_RESOURCE\_DESCRIPTOR structure at the specified address.

```dbgcmd
!ioresdes Address 
```

## <span id="ddk__ioresdes_dbg"></span><span id="DDK__IORESDES_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the IO\_RESOURCE\_DESCRIPTOR structure.

### DLL

Kdexts.dll

 

### Additional Information

See [Plug and Play Debugging](../debugger/plug-and-play-debugging.md) for applications of this extension command. For information about the IO\_RESOURCE\_DESCRIPTOR structure, see the Windows Driver Kit (WDK) documentation.

 

 





