---
title: amli u
description: The amli u extension unassembles AML code.
ms.assetid: 0a8b160f-9aae-4ef0-a569-8e701de9679c
keywords: ["amli u Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- amli u
api_type:
- NA
---

# !amli u


The **!amli u** extension unassembles AML code.

Syntax

```
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

```
kd> !amli u 80e5d701

ffffffff80e5d701 : CreateWordField(CRES, 0x1, IRQW)
ffffffff80e5d70c : And(\_SB_.PCI0.LPC_.PIRA, 0xf, Local0)
ffffffff80e5d723 : Store(One, Local1)
ffffffff80e5d726 : ShiftLeft(Local1, Local0, IRQW)
ffffffff80e5d72d : Return(CRES)
```

The following command will disassemble the \_DCK method:

```
kd> u \_sb.pci0.dock._dck
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20u%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




