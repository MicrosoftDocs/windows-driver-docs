---
title: amli dns
description: The amli dns extension displays an ACPI namespace object.
ms.assetid: 7db937ba-109f-4f4e-8dd3-4aa5d0dc13b2
keywords: ["amli dns Windows Debugging"]
topic_type:
- apiref
api_name:
- amli dns
api_type:
- NA
---

# !amli dns


The **!amli dns** extension displays an ACPI namespace object.

Syntax

``` syntax
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

```
AMLI(? for help)-> dns \bios

ACPI Name Space: \BIOS (80E5F378)
OpRegion(BIOS:RegionSpace=SystemMemory,Offset=0xfcb07500,Len=2816)
```

The following command displays the namespace for the object \_BST, and the tree subordinate to it:

```
kd> !amli dns /s \_sb.pci0.isa.bat1._bst

ACPI Name Space: \_SB.PCI0.ISA.BAT1._BST (c29c2044)
Method(_BST:Flags=0x0,CodeBuff=c29c20a5,Len=103)
```

To display the namespace for the device BAT1, type:

```
kd> !amli dns /s \_sb.pci0.isa.bat1
```

To display the namespace of everything subordinate to the DOCK device, type:

```
kd> !amli dns /s \_sb.pci0.dock
```

To display the namespace subordinate to the \_DCK method, type:

```
kd> !amli dns /s \_sb.pci0.dock._dck
```

To display the entire namespace, type:

```
kd> !amli dns
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20dns%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




