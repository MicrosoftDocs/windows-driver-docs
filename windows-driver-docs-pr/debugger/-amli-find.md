---
title: amli find
description: The amli find extension finds an ACPI namespace object.
ms.assetid: bacb1be2-f079-49da-a8d2-1e9821b20ed3
keywords: ["amli find Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- amli find
api_type:
- NA
---

# !amli find


The **!amli find** extension finds an ACPI namespace object.

Syntax

```
!amli find Name
```

## <span id="ddk__amli_find_dbg"></span><span id="DDK__AMLI_FIND_DBG"></span>Parameters


<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the name of the namespace object (without the path).

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

The **!amli find** command takes the name of the object and returns the full path and name. The *Name* parameter must be the final segment of the full path and name.

Here are some examples. The following command will find all declarations of the object \_SRS:

```
kd> !amli find _srs
\_SB.LNKA._SRS
\_SB.LNKB._SRS
\_SB.LNKC._SRS
\_SB.LNKD._SRS
```

This is not simply a text search. The command **!amli find srs** does not display any hits, because the final segment of each of these declarations is "\_SRS", not "SRS". The command **!amli find LNK** similarly does not return hits. The command **!amli find LNKB** would display the single node that terminates in "LNKB", not the four children of this node shown in the previous display:

```
kd> !amli find lnkb
\_SB.LNKB.
```

If you need to see the children of a node, use the [**!amli dns**](-amli-dns.md) command with the **/s** parameter.

Here is another example, issued from the AMLI Debugger prompt. This shows all declarations of the object \_BST in the namespace:

```
AMLI(? for help)-> find _bst
\_SB.PCI0.ISA.BAT1._BST
\_SB.PCI0.ISA.BAT2._BST
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20find%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




