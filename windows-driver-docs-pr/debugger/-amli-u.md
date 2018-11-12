---
title: amli u
description: The amli u extension unassembles AML code.
ms.assetid: 0a8b160f-9aae-4ef0-a569-8e701de9679c
keywords: ["amli u Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli u
api_type:
- NA
ms.localizationpriority: medium
---

# !amli u


The **!amli u** extension unassembles AML code.

Syntax

```dbgcmd
    !amli u [ MethodName | CodeAddress ]
```

## <span id="ddk__amli_u_dbg"></span><span id="DDK__AMLI_U_DBG"></span>Parameters


<span id="_______MethodName______"></span><span id="_______methodname______"></span><span id="_______METHODNAME______"></span> *MethodName*   
Specifies the full path of the method name to be disassembled.

<span id="_______CodeAddress______"></span><span id="_______codeaddress______"></span><span id="_______CODEADDRESS______"></span> *CodeAddress*   
Specifies the address of the AML code where disassembly will begin. If *CodeAddress* is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

If neither *MethodName* nor *CodeAddress* is specified and you are issuing this command from an AMLI

The disassembly display will continue until the end of the method is reached.

**Note**   The standard [**u (Unassemble)**](u--unassemble-.md) command will not give proper results with AML code.

 

Here are some examples. To disassemble the object at address 0x80E5D701, use the following command:

```console
kd> !amli u 80e5d701

ffffffff80e5d701 : CreateWordField(CRES, 0x1, IRQW)
ffffffff80e5d70c : And(\_SB_.PCI0.LPC_.PIRA, 0xf, Local0)
ffffffff80e5d723 : Store(One, Local1)
ffffffff80e5d726 : ShiftLeft(Local1, Local0, IRQW)
ffffffff80e5d72d : Return(CRES)
```

The following command will disassemble the \_DCK method:

```console
kd> u \_sb.pci0.dock._dck
```

 

 





