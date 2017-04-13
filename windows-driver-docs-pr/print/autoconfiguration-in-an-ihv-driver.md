---
title: Autoconfiguration in an IHV Driver
author: windows-driver-content
description: Autoconfiguration in an IHV Driver
ms.assetid: 81febae0-6fab-4226-9e98-7705d606caf4
keywords: ["IHV driver autoconfiguration WDK printer", "autoconfiguration WDK printer , IHV drivers", "printer autoconfiguration WDK printer , IHV drivers"]
---

# Autoconfiguration in an IHV Driver


A standalone IHV driver that supports autoconfiguration must meet the following requirements:

1.  Follow the Microsoft [bidi communications schema](https://msdn.microsoft.com/library/windows/hardware/ff545175) and the [bidi communication interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545163) described in the Windows SDK documentation.

2.  Support the PRINTER\_EVENT\_CONFIGURATION\_UPDATE printer event in the [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function.

3.  Be aware of the bidi notification schema's ability to understand received notifications. See [Bidi Communications Schema](bidirectional-communication-schema.md).

**Note**  It is not necessary to create a standalone driver in order to provide support for autoconfiguration. You can, instead, write a GPD or PPD file that takes advantage of one of the Microsoft printer class drivers. For details, see [In-box Support for Autoconfiguration](in-box-support-for-autoconfiguration.md).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfiguration%20in%20an%20IHV%20Driver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


