---
title: callback (WinDbg)
description: The callback extension displays the callback data related to the trap for the specified thread.
keywords: ["callback data for system traps", "callback Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- callback
api_type:
- NA
---

# !callback


The **!callback** extension displays the callback data related to the trap for the specified thread.

```dbgsyntax
!callback Address [Number]
```

## <span id="ddk__callback_dbg"></span><span id="DDK__CALLBACK_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the thread. If this is -1 or omitted, the current thread is used.

<span id="_______Number______"></span><span id="_______number______"></span><span id="_______NUMBER______"></span> *Number*   
Specifies the number of the desired callback frame. This frame is noted in the display.

### DLL

Kdexts.dll

 

This extension command can only be used with an x86-based target computer.

### Additional Information

For information about system traps, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

If the system has not experienced a system trap, this extension will not produce useful data.

 

 





