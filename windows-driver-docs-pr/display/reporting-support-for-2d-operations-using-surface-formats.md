---
title: Reporting Support for 2D Operations Using Surface Formats
description: Reporting Support for 2D Operations Using Surface Formats
ms.assetid: c7737daf-3342-48dc-a365-f789b7203013
keywords:
- two-dimensional operations WDK DirectX 9.0 , surface formats
- 2D operations WDK DirectX 9.0 , surface formats
- surface formats WDK DirectX 9.0
- surface formats WDK DirectX 9.0 , reporting support for 2D operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Support for 2D Operations Using Surface Formats


## <span id="ddk_reporting_support_for_2d_operations_using_surface_formats_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_2D_OPERATIONS_USING_SURFACE_FORMATS_GG"></span>


The driver specifies flags in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for a surface's format to indicate that it can perform 2D operations using that format.

For example, the driver can indicate that it can copy to or from and color fill to a surface by setting the D3DFORMAT\_OP\_OFFSCREENPLAIN flag.

When the driver uses vendor-supplied codes or codes from the D3DFORMAT enumerated type to set the **dwFourCC** member of DDPIXELFORMAT and assign the format for a surface, the driver can also use the D3DFORMAT\_OP\_CONVERT\_TO\_ARGB and D3DFORMAT\_MEMBEROFGROUP\_ARGB flags to indicate whether color conversion can be performed between source and target surfaces. That is, a target surface that has the D3DFORMAT\_MEMBEROFGROUP\_ARGB flag set indicates that its color format can be converted from any source surface that has the D3DFORMAT\_OP\_CONVERT\_TO\_ARGB flag set.

The driver can only specify the D3DFORMAT\_MEMBEROFGROUP\_ARGB flag for target surface formats with at least 5 bits of color information per channel. That is, the D3DFMT\_A1R5G5B5 format set in the **dwFourCC** member of DDPIXELFORMAT is valid. However, the D3DFMT\_A4R4G4B4 format is invalid. The driver is also constrained to certain source surface formats when specifying the D3DFORMAT\_OP\_CONVERT\_TO\_ARGB flag. Source formats can be any format that is valid for the D3DFORMAT\_MEMBEROFGROUP\_ARGB flag or a [*FOURCC*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc) surface format.

Note that although D3DFORMAT\_OP\_CONVERT\_TO\_ARGB and D3DFORMAT\_MEMBEROFGROUP\_ARGB indicate ARGB formats, the runtime also lets the driver specify surfaces with XRGB formats (for example, D3DFMT\_X1R5G5B5). If the driver specifies D3DFORMAT\_MEMBEROFGROUP\_ARGB or D3DFORMAT\_OP\_CONVERT\_TO\_ARGB with an invalid format, the runtime prevents the Direct3D HAL from loading.

 

 





