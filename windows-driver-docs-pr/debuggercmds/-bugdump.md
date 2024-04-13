---
title: "!bugdump (WinDbg)"
description: "The !bugdump extension formats and displays the information contained in the bug check callback buffers."
keywords: ["!bugdump Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- bugdump
api_type:
- NA
---

# !bugdump

The **!bugdump** extension formats and displays the information contained in the bug check callback buffers.

```dbgsyntax
    !bugdump [Component] 
```

## <span id="ddk__bugdump_dbg"></span><span id="DDK__BUGDUMP_DBG"></span>Parameters

<span id="_______Component______"></span><span id="_______component______"></span><span id="_______COMPONENT______"></span> *Component*   
Specifies the component whose callback data is to be examined. If omitted, all bug check callback data is displayed.

### DLL

Kdexts.dll

## Remarks

This extension can only be used after a bug check has occurred, or when you are debugging a kernel-mode crash dump file.

The *Component* parameter corresponds to the final parameter used in [**KeRegisterBugCheckCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckcallback).

The buffers that hold callback data are not available in a Small Memory Dump. These buffers are present in Kernel Memory Dumps and Full Memory Dumps. However, in Windows XP SP1, Windows Server 2003, and later versions of Windows, the dump file is created before the drivers' **BugCheckCallback** routines are called, and therefore these buffers will not contain the data written by these routines.

If you are performing live debugging of a crashed system, all callback data will be present.

## Additional Information

For more information, see [Reading Bug Check Callback Data](../debugger/reading-bug-check-callback-data.md).
