---
title: MPEG and Progressive Content
description: MPEG and Progressive Content
ms.assetid: 6973011a-dcee-4411-9382-8c0af2bd85b1
keywords:
- MPEG WDK video port extensions
- progressive content identification WDK video port extensions
- PROGRESSIVE_FRAME
- TOP_FIELD_FIRST
- REPEAT_FIRST_FIELD
- DirectX VPE support WDK DirectDraw , progressive content identification
- drawing VPEs WDK DirectDraw , progressive content identification
- DirectDraw VPEs WDK Windows 2000 display , progressive content identification
- video port extensions WDK DirectDraw , progressive content identification
- VPEs WDK DirectDraw , progressive content identification
- 3 2 pulldown WDK video port extensions
- identifying progressive content
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MPEG and Progressive Content


## <span id="ddk_mpeg_and_progressive_content_gg"></span><span id="DDK_MPEG_AND_PROGRESSIVE_CONTENT_GG"></span>


MPEG-2 syntax provides the information necessary to identify progressive content and 3:2 pulldown. This information is stored in the header for each frame in the following 1-bit flags:

-   PROGRESSIVE\_FRAME: When **TRUE**, this indicates that the two fields (of the frame) are actually from the same time instant (progressive film). When **FALSE**, this indicates that the fields might be one-half of a frame time apart (interlaced video).

-   TOP\_FIELD\_FIRST: Indicates which field comes first in time.

-   REPEAT\_FIRST\_FIELD: Indicates whether a field should be repeated for 3:2 pulldown.

With VPE and DirectDraw under the latest DirectX release, video can always be displayed with the best-possible quality if these flags or a signal derived from these flags can be conveyed to the system on a per-field basis. Interlaced video can also be supported by DirectShow, with new flags in the media sample to indicate whether an uncompressed video media sample is either a full frame or a field, plus any other information. As described in the [Displaying Interleaved Video with VPE](displaying-interleaved-video-with-vpe.md) section, DirectShow can be instructed to switch between display modes on a per-frame basis by using either frame-based media samples or field-based media samples.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20MPEG%20and%20Progressive%20Content%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




