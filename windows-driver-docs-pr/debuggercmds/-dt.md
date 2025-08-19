---
title: "!dt (WinDbg)"
description: "The !dt extension displays information about a CSR thread.This extension command should not be confused with the dt (Display Type) command."
keywords: ["!dt Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dt
api_type:
- NA
---

# !dt


The **!dt** extension displays information about a CSR thread.

This extension command should not be confused with the [**dt (Display Type)**](dt--display-type-.md) command.

```dbgcmd
!dt [v] CSR-Thread 
```

## <span id="ddk__dt_dbg"></span><span id="DDK__DT_DBG"></span>Parameters


<span id="_______v______"></span><span id="_______V______"></span> **v**   
Verbose mode.

<span id="_______CSR-Thread______"></span><span id="_______csr-thread______"></span><span id="_______CSR-THREAD______"></span> *CSR-Thread*   
Specifies the hexadecimal address of the CSR thread.

## DLL


Ntsdexts.dll



 

## Remarks

This extension displays the thread, process, client ID, flags, and reference count associated with the CSR thread. If verbose mode is selected, the display will also include list pointers, thread handle, and the wait block.

## See also


[**!dp (!ntsdexts.dp)**](-dp---ntsdexts-dp-.md)


