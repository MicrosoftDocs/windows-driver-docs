---
title: /fastdetect
description: The /fastdetect parameter disables NTDETECT serial and parallel port device detection at the specified communications ports. If you do not specify a communications port, this parameter disables detection on all serial and parallel ports.
ms.assetid: 74af68eb-ca43-42c2-8fa3-08e7432a244f
keywords: ["/fastdetect Driver Development Tools"]
topic_type:
- apiref
api_name:
- /fastdetect
api_type:
- NA
---

/fastdetect
===========

The **/fastdetect** parameter disables NTDETECT serial and parallel port device detection at the specified communications ports. If you do not specify a communications port, this parameter disables detection on all serial and parallel ports.

``` syntax
    /fastdetect[=COMx | =COMx,y,z...] 

   
```

## Subparameters


<a href="" id="-------comx--y--z"></a> **COM***x*, *y*, *z*  
Limits the **/fastdetect** parameter only to the specified ports. The *x*, *y*, and *z* subparameter represent one or more communication ports on the computer.

### Comments

Because the **/fastdetect** parameter permits Plug and Play (PnP) to detect devices on these ports and prevents detection of unsupported devices, it typically results in a faster, more reliable boot.

Setup adds the **/fastdetect** parameter (without specified ports) to the boot entries that it creates for Windows Server 2003, Windows XP, and Windows 2000.

You can omit the **/fastdetect** parameter when using devices known only to the BIOS (not to Windows). For example, you should omit **/fastdetect** to test a port that is hidden from PnP.

This boot parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000.

### Examples

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect

multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect=COM2
```

### Bootcfg Commands

```
bootcfg /raw "/fastdetect" /A /ID 1
bootcfg /raw "/fastdetect=COM2" /A /ID 2
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/fastdetect%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




