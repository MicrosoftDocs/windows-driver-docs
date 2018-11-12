---
title: hidkd.hidrd
description: The hidkd.hidrd command displays a HID report descriptor in both raw and parsed format.
ms.assetid: 8A9D76F2-7A36-4458-83A4-EDCB153EC45A
keywords: ["hidkd.hidrd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- hidkd.hidrd
api_type:
- NA
ms.localizationpriority: medium
---

# !hidkd.hidrd


The **!hidkd.hidrd** command displays a HID report descriptor in both raw and parsed format.

```dbgcmd
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

```dbgcmd
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

 

 






