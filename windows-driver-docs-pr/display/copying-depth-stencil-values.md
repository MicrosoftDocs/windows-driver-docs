---
title: Copying Depth-Stencil Values
description: Copying Depth-Stencil Values
ms.assetid: b83d4e6d-5645-49ab-bbb0-c694f1410cba
keywords:
- user-mode display drivers WDK Windows Vista , copying depth-stencil values
- copying depth-stencil values
- depth-stencil values WDK display
- stencil values WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Copying Depth-Stencil Values


The Microsoft Direct3D runtime calls the user-mode display driver's [**Blt**](https://msdn.microsoft.com/library/windows/hardware/ff538251) function to copy depth-stencil values from video memory to system memory, or vice versa. The driver and hardware must perform format conversions from, or to, all driver-supported opaque depth-stencil formats (that is, all formats defined by the [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration type except D3DDDIFMT\_D\*\_LOCKABLE) to, or from, any of the following formats:

-   D3DDDIFMT\_D16\_LOCKABLE

-   D3DDDIFMT\_D32\_LOCKABLE

-   D3DDDIFMT\_D32F\_LOCKABLE

-   D3DDDIFMT\_S8\_LOCKABLE

The driver discards any channel (depth or stencil) present in the source format but not present in the destination format. The runtime does not permit copying between depth-stencil surfaces that do not share any common channel types.

The driver first converts a source depth value to a 32-bit unsigned integer value, and then from the 32-bit unsigned integer value to the destination representation. The following rules apply for both of these conversions:

-   If the source depth value is a floating-point value, a clamp to \[0,1\] is applied and the result is multiplied by \_MAX\_UINT.

-   If the source is integral and the destination is a lower-precision integer, the right-most extra bits are removed.

-   If the source is integral and the destination is a higher-precision integer, the rightmost extra bits are replicated from the left-most significant bits.

-   If the source is integral and the destination is a floating-point value, then the 32-bit integer is converted to a floating-point value and the result is divided by \_MAX\_UINT.

The driver is not required to provide special treatment to nonuniformly distributed depth values.

The driver expands a source stencil value to an 8-bit integer (that is, the driver pads the source stencil value with zeros on the left). If the destination representation uses lower precision, then the driver should discard the most significant bits to perform the conversion.

User-mode display drivers must support depth-stencil copies of arbitrary subrectangles. However, drivers are not required to perform mirror, stretch, or color-key operations during depth-stencil copies. Point sampling is implicitly required during depth-stencil copies.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Copying%20Depth-Stencil%20Values%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




