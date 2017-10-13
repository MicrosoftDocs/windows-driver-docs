---
title: Float to XR_BIAS Conversion Rules
description: Float to XR_BIAS Conversion Rules
ms.assetid: 496306d5-7494-4df6-8af7-9acb0e2708f9
keywords:
- Direct3D version 10.1 WDK Windows 7 display , converting float to XR_BIAS
- extended format WDK Windows 7 display , converting float to XR_BIAS
- converting float to XR_BIAS WDK Windows 7 display
- float WDK Windows 7 display
- float WDK Windows 7 display , conversion to XR_BIAS
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Float to XR\_BIAS Conversion Rules


This section applies only to Windows 7 and later operating systems.

The following rules apply for converting float to XR\_BIAS. In these rules, suppose that the starting float value is c.

-   If c is NaN, the result is 0; otherwise, the following rules apply. NaN stands for "not a number," which means a symbolic entity that represents a value not otherwise available in floating-point format.

-   Perform the following operation to convert from float scale to integer scale:

    c = c \* 510

    The preceding operation might induce overflow.

-   Perform the following operation for bias:

    c = c + 384

    The preceding operation might induce overflow.

-   Perform one of the following operations to clamp, depending on the exponent of c:

    If, post bias, the exponent of c is greater than or equal to 2 (&gt;= 2 or c is INF), the result is 0x3ff, which is approximately equivalent to 1.2529.

    If, post bias, the exponent of c is less than 0 (&lt; 0 or c is -INF), the result is 0x0, which represents approximately -0.7529.

-   Re-interpret the most significant 10 bits of the mantissa of c as the result.

The conversion of float to XR\_BIAS is permitted tolerance of 0.6f Unit-Last-Place (ULP) on the XR side. This tolerance means that after converting from float to XR, any value within 0.6f ULP of a represent-capable target format value is permitted to map to that value. Note that 1 ULP of the infinitely precise result means that, for example, an implementation is permitted to truncate results to 32-bit rather than perform round-to-nearest-even, as that would result in an error of at most one unit in the last (least significant) place that is represented in the floating-point number.

The standard Direct3D version 10 requirement for inverting data also applies.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Float%20to%20XR_BIAS%20Conversion%20Rules%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




