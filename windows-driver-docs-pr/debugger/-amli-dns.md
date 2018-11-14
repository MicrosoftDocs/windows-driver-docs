---
title: amli dns
description: The amli dns extension displays an ACPI namespace object.
ms.assetid: 7db937ba-109f-4f4e-8dd3-4aa5d0dc13b2
keywords: ["amli dns Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli dns
api_type:
- NA
ms.localizationpriority: medium
---

# !amli dns


The **!amli dns** extension displays an ACPI namespace object.

Syntax

```dbgcmd
    !amli dns [/s] [Name | Address]
```

## <span id="ddk__amli_dns_dbg"></span><span id="DDK__AMLI_DNS_DBG"></span>Parameters


<span id="________s______"></span><span id="________S______"></span> **/s**   
Causes the entire namespace subtree under the specified object to be displayed recursively.

<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the namespace path.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the namespace node.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

If neither *Name* nor *Address* is specified, the entire ACPI namespace tree is displayed recursively. The **/s** parameter is always assumed in this case, even if it is not specified.

This command is useful for determining what a particular namespace object is—whether it is a method, a field unit, a device, or another type of object.

Without the **/s** parameter, this extension is equivalent to the [**!nsobj**](-nsobj.md) extension. With the **/s** parameter, it is equivalent to the [**!nstree**](-nstree.md) extension.

Here are some examples. The following command displays the namespace for the object **bios**:

```console
AMLI(? for help)-> dns \bios

ACPI Name Space: \BIOS (80E5F378)
OpRegion(BIOS:RegionSpace=SystemMemory,Offset=0xfcb07500,Len=2816)
```

The following command displays the namespace for the object \_BST, and the tree subordinate to it:

```console
kd> !amli dns /s \_sb.pci0.isa.bat1._bst

ACPI Name Space: \_SB.PCI0.ISA.BAT1._BST (c29c2044)
Method(_BST:Flags=0x0,CodeBuff=c29c20a5,Len=103)
```

To display the namespace for the device BAT1, type:

```console
kd> !amli dns /s \_sb.pci0.isa.bat1
```

To display the namespace of everything subordinate to the DOCK device, type:

```console
kd> !amli dns /s \_sb.pci0.dock
```

To display the namespace subordinate to the \_DCK method, type:

```console
kd> !amli dns /s \_sb.pci0.dock._dck
```

To display the entire namespace, type:

```console
kd> !amli dns
```

 

 





