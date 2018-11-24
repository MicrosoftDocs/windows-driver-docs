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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MPEG and Progressive Content


## <span id="ddk_mpeg_and_progressive_content_gg"></span><span id="DDK_MPEG_AND_PROGRESSIVE_CONTENT_GG"></span>


MPEG-2 syntax provides the information necessary to identify progressive content and 3:2 pulldown. This information is stored in the header for each frame in the following 1-bit flags:

-   PROGRESSIVE\_FRAME: When **TRUE**, this indicates that the two fields (of the frame) are actually from the same time instant (progressive film). When **FALSE**, this indicates that the fields might be one-half of a frame time apart (interlaced video).

-   TOP\_FIELD\_FIRST: Indicates which field comes first in time.

-   REPEAT\_FIRST\_FIELD: Indicates whether a field should be repeated for 3:2 pulldown.

With VPE and DirectDraw under the latest DirectX release, video can always be displayed with the best-possible quality if these flags or a signal derived from these flags can be conveyed to the system on a per-field basis. Interlaced video can also be supported by DirectShow, with new flags in the media sample to indicate whether an uncompressed video media sample is either a full frame or a field, plus any other information. As described in the [Displaying Interleaved Video with VPE](displaying-interleaved-video-with-vpe.md) section, DirectShow can be instructed to switch between display modes on a per-frame basis by using either frame-based media samples or field-based media samples.

 

 





