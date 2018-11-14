---
title: amli bp
description: The amli bp extension places a breakpoint in AML code.
ms.assetid: 830df6b8-835c-4485-a28a-e9a028f166f5
keywords: ["amli bp Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli bp
api_type:
- NA
ms.localizationpriority: medium
---

# !amli bp


The **!amli bp** extension places a breakpoint in AML code.

Syntax

```dbgcmd
    !amli bp { MethodName | CodeAddress }
```

## <span id="ddk__amli_bp_dbg"></span><span id="DDK__AMLI_BP_DBG"></span>Parameters


<span id="_______MethodName______"></span><span id="_______methodname______"></span><span id="_______METHODNAME______"></span> *MethodName*   
Specifies the full path of the method name on which the breakpoint will be set.

<span id="_______CodeAddress______"></span><span id="_______codeaddress______"></span><span id="_______CODEADDRESS______"></span> *CodeAddress*   
Specifies the address of the AML code at which the breakpoint will be set. If *CodeAddress* is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

The AMLI Debugger supports a maximum of 10 breakpoints.

Here is an example. The following command will set a breakpoint on the \_DCK method:

```console
kd> !amli bp \_sb.pci0.dock._dck
```

 

 





