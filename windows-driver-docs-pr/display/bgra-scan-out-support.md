---
title: BGRA Scan-Out Support
description: BGRA Scan-Out Support
ms.assetid: 88ef5de7-59cc-4a8a-aaf7-74489a7ac0ab
keywords: ["Direct3D version 10.1 WDK Windows 7 display , BGRA scan-out support", "BGRA scan-out support WDK Windows 7 display", "scan-out support WDK Windows 7 display"]
---

# BGRA Scan-Out Support


This section applies only to Windows 7 and later operating systems.

The scan-out bit is turned on for the DXGI\_FORMAT\_B8G8R8A8\_UNORM and DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB formats. Therefore, the user-mode display driver should be able to perform the following operations:

-   Handle requests for the primary surface that are in these formats.

-   Handle calls to its [**SetDisplayMode**](https://msdn.microsoft.com/library/windows/hardware/ff569535) function for resources that are created with these formats.

-   Handle calls to its [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) function to present these formats through both bit-block transfer (bitblt) and flip operations.

-   Handle calls to its [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function to copy these formats through stretch, rotate, and resolve (in fact, all the bitblt operations that are expected for the RGBA variants).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20BGRA%20Scan-Out%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




