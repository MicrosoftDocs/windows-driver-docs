---
title: hidkd.hidrd
description: The hidkd.hidrd command displays a HID report descriptor in both raw and parsed format.
ms.assetid: 8A9D76F2-7A36-4458-83A4-EDCB153EC45A
keywords: ["hidkd.hidrd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- hidkd.hidrd
api_type:
- NA
---

# !hidkd.hidrd


The **!hidkd.hidrd** command displays a HID report descriptor in both raw and parsed format.

```
!hidkd.hidrd rd Length
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______rd______"></span><span id="_______RD______"></span> *rd*   
Address of the raw report descriptor data. To get the address of the descriptor data, use the [**!hidfdo**](-hidkd-hidfdo.md) command.

<span id="_______Length______"></span><span id="_______length______"></span><span id="_______LENGTH______"></span> *Length*   
The length, in bytes, of the raw report descriptor data. To get the length, use the [**!hidfdo**](-hidkd-hidfdo.md) command.

## <span id="DLL"></span><span id="dll"></span>DLL


Hidkd.dll

Examples
--------

This example shows how to use the [**!hidfdo**](-hidkd-hidfdo.md) command followed by the **!hidrd** command. The output of **!hidfdo** shows both the address and length of the raw report descriptor data.

```
0: kd> !hidfdo 0xffffe00004f466e0
# FDO 0xffffe00004f466e0  (!devobj/!devstack)

  Name              : \Device\_HID00000002
  ...
  Report Descriptor : !hidrd 0xffffe00004281a80 0x127
  ...

0: kd> !hidrd 0xffffe00004281a80 0x127
Report Descriptor at 0xffffe00004281a80

## Raw Data

0x0000: 05 01 09 02 A1 01 05 01-09 02 A1 02 85 1A 09 01
0x0010: A1 00 05 09 19 01 29 05-95 05 75 01 15 00 25 01
0x0020: 81 02 75 03 95 01 81 01-05 01 09 30 09 31 95 02
...

## Parsed

Usage Page (Generic Desktop Controls)....................0x0000: 05 01
Usage (Mouse)............................................0x0002: 09 02
Collection (Application).................................0x0004: A1 01
..Usage Page (Generic Desktop Controls)..................0x0006: 05 01
..Usage (Mouse)..........................................0x0008: 09 02
..Collection (Logical)...................................0x000A: A1 02
....Report ID (26).......................................0x000C: 85 1A
...
End Collection ()........................................0x0126: C0
```

## <span id="see_also"></span>See also


[HID Extensions](hid-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!hidkd.hidrd%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





