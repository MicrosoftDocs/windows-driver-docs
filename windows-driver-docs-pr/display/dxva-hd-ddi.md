---
title: DXVA-HD DDI
description: DXVA-HD DDI
ms.assetid: 8b44a5b7-dc86-46eb-83e1-39caa72ffa34
keywords:
- DXVA-HD DDI WDK Windows 7 display
- DXVA-HD DDI WDK Server 2008 R2 display
- high-definition video WDK Windows 7 display , DXVA-HD DDI
- high-definition video WDK Server 2008 R2 display , DXVA-HD DDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DXVA-HD DDI


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The DXVA-HD DDI is an extension to the [Direct3D version 9 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552927) to handle the processing of high-definition video. The DXVA-HD DDI consists of the following entry points:

-   The following [**D3DDDICAPS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff544132) values are used by the Direct3D runtime to retrieve information about the high-definition video processing capabilities that the user-mode display driver supports. The runtime sets these **D3DDDICAPS\_TYPE** values in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter of the driver's [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function points to when the runtime calls *GetCaps*.

    <span id="D3DDDICAPS_DXVAHD_GETVPDEVCAPS"></span><span id="d3dddicaps_dxvahd_getvpdevcaps"></span>D3DDDICAPS\_DXVAHD\_GETVPDEVCAPS  
    The driver provides a pointer to a [**DXVAHDDDI\_VPDEVCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff563113) structure for the video processor capabilities that the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff563048) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148)) supports.

    <span id="D3DDDICAPS_DXVAHD_GETVPOUTPUTFORMATS"></span><span id="d3dddicaps_dxvahd_getvpoutputformats"></span>D3DDDICAPS\_DXVAHD\_GETVPOUTPUTFORMATS  
    The driver provides an array of [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration types that represent the output formats for the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff563048) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148)).

    <span id="D3DDDICAPS_DXVAHD_GETVPINPUTFORMATS"></span><span id="d3dddicaps_dxvahd_getvpinputformats"></span>D3DDDICAPS\_DXVAHD\_GETVPINPUTFORMATS  
    The driver provides an array of [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration types that represent the input formats for the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff563048) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148)).

    <span id="D3DDDICAPS_DXVAHD_GETVPCAPS"></span><span id="d3dddicaps_dxvahd_getvpcaps"></span>D3DDDICAPS\_DXVAHD\_GETVPCAPS  
    The driver provides an array of [**DXVAHDDDI\_VPCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff563109) structures for the capabilities for each video processor that the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff563048) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148)) supports.

    <span id="D3DDDICAPS_DXVAHD_GETVPCUSTOMRATES"></span><span id="d3dddicaps_dxvahd_getvpcustomrates"></span>D3DDDICAPS\_DXVAHD\_GETVPCUSTOMRATES  
    The driver provides an array of [**DXVAHDDDI\_CUSTOM\_RATE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff563045) structures for the custom frame rates that a video processor (which is specified by a CONST\_GUID that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148)) supports.

    <span id="D3DDDICAPS_DXVAHD_GETVPFILTERRANGE"></span><span id="d3dddicaps_dxvahd_getvpfilterrange"></span>D3DDDICAPS\_DXVAHD\_GETVPFILTERRANGE  
    The driver provides a pointer to a [**DXVAHDDDI\_FILTER\_RANGE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff563055) structure for the range that the filter (which is specified by a [**DXVAHDDDI\_FILTER**](https://msdn.microsoft.com/library/windows/hardware/ff563052) enumeration value that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148)) supports.

-   The [**CreateVideoProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff540732) function creates a video processor that can process high-definition video.

-   The [**SetVideoProcessBltState**](https://msdn.microsoft.com/library/windows/hardware/ff569694) function sets the state of a bit-block transfer (bitblt) for a video processor.

-   The [**GetVideoProcessBltStatePrivate**](https://msdn.microsoft.com/library/windows/hardware/ff566812) function retrieves the state data of a private bitblt for a video processor.

-   The [**SetVideoProcessStreamState**](https://msdn.microsoft.com/library/windows/hardware/ff569696) function sets the state of a stream for a video processor.

-   The [**GetVideoProcessStreamStatePrivate**](https://msdn.microsoft.com/library/windows/hardware/ff566815) function retrieves the private stream-state data for a video processor.

-   The [**VideoProcessBltHD**](https://msdn.microsoft.com/library/windows/hardware/ff570496) function processes video input streams and composes to an output surface.

-   The [**DestroyVideoProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff552817) function releases resources for a previously created video processor.

 

 





