---
title: hidkd.hidppd HID extension
description: The hidkd.hidppd command displays HID preparsed data.
ms.assetid: 049D206D-669D-49F4-81FE-2D8E443F9A9E
keywords: ["hidkd.hidppd Windows Debugging"]
topic_type:
- apiref
api_name:
- hidkd.hidppd
api_type:
- NA
---

# !hidkd.hidppd


The **!hidkd.hidppd** command displays HID preparsed data.

``` syntax
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

``` syntax

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!hidkd.hidppd%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





