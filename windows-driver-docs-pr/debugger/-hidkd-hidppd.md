---
title: hidkd.hidppd HID extension
description: The hidkd.hidppd command displays HID preparsed data.
ms.assetid: 049D206D-669D-49F4-81FE-2D8E443F9A9E
keywords: ["hidkd.hidppd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- hidkd.hidppd
api_type:
- NA
ms.localizationpriority: medium
---

# !hidkd.hidppd


The **!hidkd.hidppd** command displays HID preparsed data.

```dbgcmd
!hidkd.hidppd ppd
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______ppd______"></span><span id="_______PPD______"></span> *ppd*   
Address of a **HIDP\_PREPARSED\_DATA** structure. To get the address of a **HIDP\_PREPARSED\_DATA** structure, use [**!hidfdo**](-hidkd-hidfdo.md) or [**!hidpdo**](-hidkd-hidpdo.md).

## <span id="DLL"></span><span id="dll"></span>DLL


Hidkd.dll

Examples
--------

This example shows how to use [**!hidpdo**](-hidkd-hidpdo.md) followed by **!hidppd**. The output of **!hidpdo** shows the address of a **HIDP\_PREPARSED\_DATA** structure.

```dbgcmd

0: kd> !hidpdo 0xffffe000029f6060
## PDO 0xffffe000029f6060  (!devobj/!devstack)

  Collection Num  : 1
  Name            : \Device\_HID00000000#COLLECTION00000001
  ...
  Pre-parsed Data : 0xffffe000029d1010
  ...

0: kd> !hidkd.hidppd 0xffffe000029d1010
Reading preparsed data...
Preparsed Data at 0xffffe000029d1010  

## Summary

  UsagePage             : Vendor-defined (0xFFA0)
  Usage                 : 0x01
  Report Length         : 0x2(Input) 0x2(Output) 0x0(Feature)
  Link Collection Nodes : 2
  Button Caps           : 0(Input) 0(Output) 0(Feature)
  Value Caps            : 1(Input) 1(Output) 0(Feature)
  Data Indices          : 1(Input) 1(Output) 0(Feature)

## Input Value Capability #0

  Report ID         : 0x0
  Usage Page        : Vendor-defined (0xFFA1)
  Bit Size          : 0x8
  Report Count      : 0x1
  ...
```

## <span id="see_also"></span>See also


[HID Extensions](hid-extensions.md)

 

 






