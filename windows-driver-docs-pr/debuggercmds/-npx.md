---
title: "!npx (WinDbg)"
description: "The !npx extension displays the contents of the floating-point register save area."
keywords: ["registers, floating-point register save area", "!npx Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- npx
api_type:
- NA
---

# !npx

The **!npx** extension displays the contents of the floating-point register save area.

```dbgcmd
!npx Address
```

## <span id="ddk__npx_dbg"></span><span id="DDK__NPX_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the FLOATING\_SAVE\_AREA structure.

### DLL

Kdexts.dll

## Remarks

This extension command can only be used with an x86-based target computer.
