---
title: Reporting Support for 2D Operations Using Surface Formats
description: Reporting Support for 2D Operations Using Surface Formats
ms.assetid: c7737daf-3342-48dc-a365-f789b7203013
keywords:
- two-dimensional operations WDK DirectX 9.0 , surface formats
- 2D operations WDK DirectX 9.0 , surface formats
- surface formats WDK DirectX 9.0
- surface formats WDK DirectX 9.0 , reporting support for 2D operations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support for 2D Operations Using Surface Formats


## <span id="ddk_reporting_support_for_2d_operations_using_surface_formats_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_2D_OPERATIONS_USING_SURFACE_FORMATS_GG"></span>


The driver specifies flags in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for a surface's format to indicate that it can perform 2D operations using that format.

For example, the driver can indicate that it can copy to or from and color fill to a surface by setting the D3DFORMAT\_OP\_OFFSCREENPLAIN flag.

When the driver uses vendor-supplied codes or codes from the D3DFORMAT enumerated type to set the **dwFourCC** member of DDPIXELFORMAT and assign the format for a surface, the driver can also use the D3DFORMAT\_OP\_CONVERT\_TO\_ARGB and D3DFORMAT\_MEMBEROFGROUP\_ARGB flags to indicate whether color conversion can be performed between source and target surfaces. That is, a target surface that has the D3DFORMAT\_MEMBEROFGROUP\_ARGB flag set indicates that its color format can be converted from any source surface that has the D3DFORMAT\_OP\_CONVERT\_TO\_ARGB flag set.

The driver can only specify the D3DFORMAT\_MEMBEROFGROUP\_ARGB flag for target surface formats with at least 5 bits of color information per channel. That is, the D3DFMT\_A1R5G5B5 format set in the **dwFourCC** member of DDPIXELFORMAT is valid. However, the D3DFMT\_A4R4G4B4 format is invalid. The driver is also constrained to certain source surface formats when specifying the D3DFORMAT\_OP\_CONVERT\_TO\_ARGB flag. Source formats can be any format that is valid for the D3DFORMAT\_MEMBEROFGROUP\_ARGB flag or a [*FOURCC*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc) surface format.

Note that although D3DFORMAT\_OP\_CONVERT\_TO\_ARGB and D3DFORMAT\_MEMBEROFGROUP\_ARGB indicate ARGB formats, the runtime also lets the driver specify surfaces with XRGB formats (for example, D3DFMT\_X1R5G5B5). If the driver specifies D3DFORMAT\_MEMBEROFGROUP\_ARGB or D3DFORMAT\_OP\_CONVERT\_TO\_ARGB with an invalid format, the runtime prevents the Direct3D HAL from loading.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%202D%20Operations%20Using%20Surface%20Formats%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




