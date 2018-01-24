---
title: /noguiboot
description: The /noguiboot parameter suppresses all bit-mapped graphics during the boot process, including the splash screen and progress bar that precede the logon prompt and the blue background of a bug check screen.
ms.assetid: 0c528866-864f-451a-80e5-7d2aef01c8aa
keywords: ["/noguiboot Driver Development Tools"]
topic_type:
- apiref
api_name:
- /noguiboot
api_type:
- NA
---

/noguiboot
==========

The **/noguiboot** parameter suppresses all bit-mapped graphics during the boot process, including the splash screen and progress bar that precede the logon prompt and the blue background of a bug check screen.

``` syntax
    /noguiboot 

   
```

### Comments

This boot parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000.

The **/noguiboot** option is supported only on Windows Server 2003 with SP1 and Windows XP with SP2.

OnWindows Vista and later, use the **quietboot** option with BCDEdit. The **quietboot** option controls the display of a high-resolution bitmap in place of the Windows boot screen display and animation.

When **/noguiboot** is used, the system does not initialize bootvid.dll, the software component that provides basic video support before the computer's graphics drivers are loaded. Because bootvid.dll is not operating, the computer cannot display bit-mapped graphics during the boot process.

You can use this parameter to investigate problems with video devices.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /noguiboot
```

### Bootcfg command

```
bootcfg /addsw /NG /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/noguiboot%20%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




