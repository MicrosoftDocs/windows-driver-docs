---
title: hidkd.hidfdo
description: The hidkd.hidfdo command displays HID information associated with a functional device object (FDO).
ms.assetid: CB8E8844-B5A7-4273-8401-D4F3C8CBAC4C
keywords: ["hidkd.hidfdo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- hidkd.hidfdo
api_type:
- NA
ms.localizationpriority: medium
---

# !hidkd.hidfdo


The **!hidkd.hidfdo** command displays HID information associated with a functional device object (FDO).

```dbgcmd
!hidkd.hidfdo fdo
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______fdo______"></span><span id="_______FDO______"></span> *fdo*   
Address of an FDO. To get the addresses of FDOs that are associated with HID drivers, use the [**!usbhid.hidtree**](-hidkd-hidtree.md) command.

## <span id="DLL"></span><span id="dll"></span>DLL


Hidkd.dll

Examples
--------

Here is an example of the output of the **!hidfdo** command. The example first calls [**!hidtree**](-hidkd-hidtree.md) to get the address of an FDO.

```dbgcmd
0: kd> !hidkd.hidtree
HID Device Tree
...
FDO  VendorID:0x045E(Microsoft Corporation) ProductID:0x0745 Version:0x0634
!hidfdo 0xffffe00004f466e0
...
0: kd> !hidfdo 0xffffe00004f466e0
# FDO 0xffffe00004f466e0  (!devobj/!devstack)

  Name              : \Device\_HID00000002
  Vendor ID         : 0x045E(Microsoft Corporation)
  Product ID        : 0x0745
  Version Number    : 0x0634
  Is Present?       : Y
  Report Descriptor : !hidrd 0xffffe00004281a80 0x127
  Per-FDO IFR Log   : !rcdrlogdump HIDCLASS -a 0xFFFFE0000594D000

  Position in HID tree

  dt FDO_EXTENSION 0xffffe00004f46850
```

## <span id="see_also"></span>See also


[HID Extensions](hid-extensions.md)

 

 






