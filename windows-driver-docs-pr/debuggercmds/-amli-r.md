---
title: "!amli r (WinDbg)"
description: "The !amli r extension displays information about the current context or the specified context."
keywords: ["!amli r Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli r
api_type:
- NA
---

# !amli r

The **!amli r** extension displays information about the current context or the specified context.

Syntax

```dbgcmd
   !amli r [ContextAddress]
```

## Parameters

<span id="_______ContextAddress______"></span><span id="_______contextaddress______"></span><span id="_______CONTEXTADDRESS______"></span> *ContextAddress*   
Specifies the address of the context block to be displayed. The address of a context block can be determined from the **Ctxt** field in the [**!amli lc**](-amli-lc.md) display. If *ContextAddress* is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address. If this parameter is omitted, the current context is displayed.

## DLL

Kdexts.dll

## Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).

## Remarks

If the AMLI Debugger prompt appears suddenly, this is a useful command to use.

For example, the following command will display the current context of the interpreter:

```console
AMLI(? for help)-> r

Context=c18b4000*, Queue=00000000, ResList=00000000
ThreadID=c15a6618, Flags=00000010
StackTop=c18b5eec, UsedStackSize=276 bytes, FreeStackSize=7636 bytes
LocalHeap=c18b40c0, CurrentHeap=c18b40c0, UsedHeapSize=88 bytes
Object=\_WAK, Scope=\_WAK, ObjectOwner=c18b4108, SyncLevel=0
AsyncCallBack=ff06b5d0, CallBackData=0, CallBackContext=c99efddc

MethodObject=\_WAK
80e0ff5c: Local0=Unknown()
80e0ff70: Local1=Unknown()
80e0ff84: Local2=Unknown()
80e0ff98: Local3=Unknown()
80e0ffac: Local4=Unknown()
80e0ffc0: Local5=Unknown()
80e0ffd4: Local6=Unknown()
80e0ffe8: Local7=Unknown()
80e0e040: RetObj=Unknown()

Next AML Pointer: ffffffff80e630df:[\_WAK+16]

ffffffff80e630df : If(S4BW
ffffffff80e630e5 : {
ffffffff80e630e5 : | Store(Zero, S4BW)
ffffffff80e630eb : }
```

 

 





