---
title: mps (WinDbg)
description: The mps extension displays BIOS information for the Intel Multiprocessor Specification (MPS) of the target computer.
keywords: ["mps Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- mps
api_type:
- NA
---

# !mps


The **!mps** extension displays BIOS information for the Intel Multiprocessor Specification (MPS) of the target computer.

```dbgcmd
!mps [Address] 
```

## <span id="ddk__mps_dbg"></span><span id="DDK__MPS_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the MPS table in the BIOS. If this is omitted, the information is obtained from the HAL. This will require HAL symbols.

### DLL

Kdexts.dll

 

This extension command can only be used with an x86-based target computer.

### Additional Information

For more information about BIOS debugging, see [Debugging BIOS Code](../debugger/debugging-bios-code.md). For more information about the MPS, refer to the appropriate version of the Intel MultiProcessor Specification.

 

 





