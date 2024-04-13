---
title: "!exchain (WinDbg)"
description: "The !exchain extension displays the current exception handler chain."
keywords: ["!exchain Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- exchain
api_type:
- NA
---

# !exchain


The **!exchain** extension displays the current exception handler chain.

```dbgcmd
!exchain [Options]
```

## <span id="ddk__exchain_dbg"></span><span id="DDK__EXCHAIN_DBG"></span>Parameters


*Options*
One of the following values:

<span id="_c"></span><span id="_C"></span>**/c**  
Displays information that is relevant for debugging a C++ **try**/**catch** exception, if such an exception is detected.

<span id="_C"></span><span id="_c"></span>**/C**  
Displays information that is relevant for debugging a C++ **try**/**catch** exception, even when such an exception has not been detected.

<span id="_f"></span><span id="_F"></span>**/f**  
Displays information that is obtained by walking the CRT function tables, even if a CRT exception handler was not detected.

## DLL


Ext.dll



 

The **!exchain** extension is available only for an x86-based target computer.

## Remarks

The **!exchain** extension displays the list of exception handlers for the current thread.

The list begins with the first handler on the chain (the one that is given the first opportunity to handle an exception) and continues on to the end. The following example shows this extension.

```dbgcmd
0:000> !exchain
0012fea8: Prymes!_except_handler3+0 (00407604)
  CRT scope  0, filter: Prymes!dzExcepError+e6 (00401576)
                func:   Prymes!dzExcepError+ec (0040157c)
0012ffb0: Prymes!_except_handler3+0 (00407604)
  CRT scope  0, filter: Prymes!mainCRTStartup+f8 (004021b8)
                func:   Prymes!mainCRTStartup+113 (004021d3)
0012ffe0: KERNEL32!GetThreadContext+1c (77ea1856)
```

