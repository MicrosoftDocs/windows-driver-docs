---
title: Supporting Stretch Blit Operations
description: Supporting Stretch Blit Operations
ms.assetid: 1d279e56-41fd-4189-84d2-858e51db281d
keywords:
- blit stretch operations WDK DirectX 9.0
- stretch blit operations WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Stretch%20Blit%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




