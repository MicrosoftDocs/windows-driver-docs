---
title: "!amli ln (WinDbg)"
description: "The !amli ln extension displays the specified method or the method containing a given address."
keywords: ["!amli ln Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli ln
api_type:
- NA
---

# !amli ln


The **!amli ln** extension displays the specified method or the method containing a given address.

Syntax

```dbgcmd
    !amli ln [ MethodName | CodeAddress ]
```

## <span id="ddk__amli_ln_dbg"></span><span id="DDK__AMLI_LN_DBG"></span>Parameters


<span id="_______MethodName______"></span><span id="_______methodname______"></span><span id="_______METHODNAME______"></span> *MethodName*   
Specifies the full path of the method name. If *MethodName* specifies an object that is not actually a method, an error results.

<span id="_______CodeAddress______"></span><span id="_______codeaddress______"></span><span id="_______CODEADDRESS______"></span> *CodeAddress*   
Specifies the address of the AML code that is contained in the desired method. If *CodeAddress* is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address.

## DLL

Kdexts.dll

## Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).

## Remarks

If neither *MethodName* nor *CodeAddress* is specified, the method associated with the current context is displayed.

The following command shows the method being currently run:

```console
kd> !amli ln
c29accf5: \_WAK
```

The method \_WAK is shown, with address 0xC29ACCF5.

 

 





