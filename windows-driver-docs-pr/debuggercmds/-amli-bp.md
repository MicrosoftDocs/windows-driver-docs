---
title: "!amli bp (WinDbg)"
description: "!The amli bp extension places a breakpoint in AML code."
keywords: ["!amli bp Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli bp
api_type:
- NA
---

# !amli bp

The **!amli bp** extension places a breakpoint in AML code.

Syntax

```dbgcmd
    !amli bp { MethodName | CodeAddress }
```

## Parameters


<span id="_______MethodName______"></span><span id="_______methodname______"></span><span id="_______METHODNAME______"></span> *MethodName*   
Specifies the full path of the method name on which the breakpoint will be set.

<span id="_______CodeAddress______"></span><span id="_______codeaddress______"></span><span id="_______CODEADDRESS______"></span> *CodeAddress*   
Specifies the address of the AML code at which the breakpoint will be set. If *CodeAddress* is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address.

## DLL

Kdexts.dll

### Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).

## Remarks

The AMLI Debugger supports a maximum of 10 breakpoints.

Here is an example. The following command will set a breakpoint on the \_DCK method:

```console
kd> !amli bp \_sb.pci0.dock._dck
```

 

 





