---
title: Supporting Stretch Blit Operations
description: Supporting Stretch Blit Operations
ms.assetid: 1d279e56-41fd-4189-84d2-858e51db281d
keywords:
- blit stretch operations WDK DirectX 9.0
- stretch blit operations WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Stretch Blit Operations


## <span id="ddk_supporting_stretch_blit_operations_gg"></span><span id="DDK_SUPPORTING_STRETCH_BLIT_OPERATIONS_GG"></span>


How a driver performs a stretch blit depends on the platform on which it runs. For Windows 98/Me platforms, when the driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function receives a blit request, the driver can calculate stretch factor from the unclipped rectangular areas in the **rOrigDest** and **rOrigSrc** members of the [**DD\_BLTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550474) structure and factor in the calculation when it performs the blit operation.

For DirectX 9.0 and later on NT-based operating systems, the driver can calculate and record stretch factor when it receives a blit request with the DDBLT\_EXTENDED\_FLAGS and DDBLT\_EXTENDED\_PRESENTATION\_STRETCHFACTOR flags set in the **dwFlags** member of DD\_BLTDATA. The driver calculates the stretch factor from the unclipped source and destination rectangular areas in the **rSrc** and **bltFX** members respectively of DD\_BLTDATA with DDBLT\_EXTENDED\_PRESENTATION\_STRETCHFACTOR set. Note that the driver must obtain the unclipped destination rectangular area from the following members of the DDBLTFX structure in **bltFX**, and not use information in the **rDest** member.

-   Left and top coordinates from the following members of the DDCOLORKEY structure in the **ddckDestColorkey** member of DDBLTFX:
    -   Left coordinate from the **dwColorSpaceLowValue** member of DDCOLORKEY.
    -   Top coordinate from the **dwColorSpaceHighValue** member of DDCOLORKEY.
-   Right and bottom coordinates from the following members of the DDCOLORKEY structure in the **ddckSrcColorkey** member of DDBLTFX:
    -   Right coordinate from the **dwColorSpaceLowValue** member of DDCOLORKEY.
    -   Bottom coordinate from the **dwColorSpaceHighValue** member of DDCOLORKEY.

Note that the driver interprets these coordinates as signed integers rather than DWORDs. Note also that the driver must validate the rectangle that these coordinates form before calculating the stretch factor and programming the stretch factor in the graphics device. For more information about DDBLTFX and DDCOLORKEY, see the latest DirectDraw SDK documentation.

When the driver receives a blit with DDBLT\_EXTENDED\_PRESENTATION\_STRETCHFACTOR set, the driver must not use the unclipped rectangular areas to do any actual blitting.

When the driver subsequently receives blit requests with the DDBLT\_PRESENTATION and DDBLT\_LAST\_PRESENTATION flags set, the driver can factor in this recorded stretch factor in the blit operations. After the driver finishes the final blit with the DDBLT\_LAST\_PRESENTATION flag set, the driver must clear the stretch-factor record to prevent interference with any subsequent blits. For more information about the DDBLT\_PRESENTATION and DDBLT\_LAST\_PRESENTATION flags, see [Presentation](presentation.md).

Because stretch factor is a floating-point calculation, not all graphics devices can support it. Therefore, the driver for such a device is not required to calculate and use stretch factor. However, even if stretch-factor calculations are unsupported, a DirectX 9.0 and later driver on an NT-based operating system must still determine the presence of the DDBLT\_EXTENDED\_PRESENTATION\_STRETCHFACTOR flag because attempting to perform an actual blit operation in which the DDBLT\_EXTENDED\_PRESENTATION\_STRETCHFACTOR flag is set would cause rendering corruption.

For more information about extended blit flags, see [Extended Blt Flags](extended-blt-flags.md).

 

 





