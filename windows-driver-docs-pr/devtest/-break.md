---
title: /break
description: The /break parameter sets a breakpoint at HAL initialization.
ms.assetid: 82b45320-f433-4e47-8281-6daa68e4e887
keywords: ["/break Driver Development Tools"]
topic_type:
- apiref
api_name:
- /break
api_type:
- NA
---

/break
======

The **/break** parameter sets a breakpoint at HAL initialization.

``` syntax
    /break 

   
```

### Comments

The **/break** parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000. On Windows Vista and later versions of Windows, use the **HALBreakPoint** element in BCDEdit.

When the **/break** parameter is used with the [**/debug**](-debug.md) parameter, the HAL waits at the breakpoint indefinitely until a debugger is connected.

When the **/break** parameter is used without the **/debug** parameter, Windows issues [**Bug Check 0x78: PHASE0\_EXCEPTION**](https://msdn.microsoft.com/library/windows/hardware/ff559206) and displays a blue screen when it hits the breakpoint.

This parameter is used primarily in HAL development and debugging.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /break /debug
```

### Bootcfg Command

```
bootcfg /raw "/break /debug" /A /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/break%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




