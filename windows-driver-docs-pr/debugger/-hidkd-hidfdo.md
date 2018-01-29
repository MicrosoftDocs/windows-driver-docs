---
title: hidkd.hidfdo
description: The hidkd.hidfdo command displays HID information associated with a functional device object (FDO).
ms.assetid: CB8E8844-B5A7-4273-8401-D4F3C8CBAC4C
keywords: ["hidkd.hidfdo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- hidkd.hidfdo
api_type:
- NA
---

# !hidkd.hidfdo


The **!hidkd.hidfdo** command displays HID information associated with a functional device object (FDO).

```
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!hidkd.hidfdo%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





