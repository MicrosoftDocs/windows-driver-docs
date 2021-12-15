---
title: DXVA-HD DDI
description: DXVA-HD DDI
keywords:
- DXVA-HD DDI WDK Windows 7 display
- DXVA-HD DDI WDK Server 2008 R2 display
- high-definition video WDK Windows 7 display , DXVA-HD DDI
- high-definition video WDK Server 2008 R2 display , DXVA-HD DDI
ms.date: 04/20/2017
---

# DXVA-HD DDI


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The DXVA-HD DDI is an extension to the [Direct3D version 9 DDI](/windows-hardware/drivers/ddi/d3dumddi/index) to handle the processing of high-definition video. The DXVA-HD DDI consists of the following entry points:

-   The following [**D3DDDICAPS\_TYPE**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddicaps_type) values are used by the Direct3D runtime to retrieve information about the high-definition video processing capabilities that the user-mode display driver supports. The runtime sets these **D3DDDICAPS\_TYPE** values in the **Type** member of the [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) structure that the *pData* parameter of the driver's [**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) function points to when the runtime calls *GetCaps*.

    <span id="D3DDDICAPS_DXVAHD_GETVPDEVCAPS"></span><span id="d3dddicaps_dxvahd_getvpdevcaps"></span>D3DDDICAPS\_DXVAHD\_GETVPDEVCAPS  
    The driver provides a pointer to a [**DXVAHDDDI\_VPDEVCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_vpdevcaps) structure for the video processor capabilities that the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_device_desc) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps)) supports.

    <span id="D3DDDICAPS_DXVAHD_GETVPOUTPUTFORMATS"></span><span id="d3dddicaps_dxvahd_getvpoutputformats"></span>D3DDDICAPS\_DXVAHD\_GETVPOUTPUTFORMATS  
    The driver provides an array of [**D3DDDIFORMAT**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddiformat) enumeration types that represent the output formats for the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_device_desc) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps)).

    <span id="D3DDDICAPS_DXVAHD_GETVPINPUTFORMATS"></span><span id="d3dddicaps_dxvahd_getvpinputformats"></span>D3DDDICAPS\_DXVAHD\_GETVPINPUTFORMATS  
    The driver provides an array of [**D3DDDIFORMAT**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddiformat) enumeration types that represent the input formats for the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_device_desc) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps)).

    <span id="D3DDDICAPS_DXVAHD_GETVPCAPS"></span><span id="d3dddicaps_dxvahd_getvpcaps"></span>D3DDDICAPS\_DXVAHD\_GETVPCAPS  
    The driver provides an array of [**DXVAHDDDI\_VPCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_vpcaps) structures for the capabilities for each video processor that the decode device (which is specified in a [**DXVAHDDDI\_DEVICE\_DESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_device_desc) structure that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps)) supports.

    <span id="D3DDDICAPS_DXVAHD_GETVPCUSTOMRATES"></span><span id="d3dddicaps_dxvahd_getvpcustomrates"></span>D3DDDICAPS\_DXVAHD\_GETVPCUSTOMRATES  
    The driver provides an array of [**DXVAHDDDI\_CUSTOM\_RATE\_DATA**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_custom_rate_data) structures for the custom frame rates that a video processor (which is specified by a CONST\_GUID that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps)) supports.

    <span id="D3DDDICAPS_DXVAHD_GETVPFILTERRANGE"></span><span id="d3dddicaps_dxvahd_getvpfilterrange"></span>D3DDDICAPS\_DXVAHD\_GETVPFILTERRANGE  
    The driver provides a pointer to a [**DXVAHDDDI\_FILTER\_RANGE\_DATA**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_filter_range_data) structure for the range that the filter (which is specified by a [**DXVAHDDDI\_FILTER**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_dxvahdddi_filter) enumeration value that is pointed to by the **pInfo** member of [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps)) supports.

-   The [**CreateVideoProcessor**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_dxvahd_createvideoprocessor) function creates a video processor that can process high-definition video.

-   The [**SetVideoProcessBltState**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_dxvahd_setvideoprocessbltstate) function sets the state of a bit-block transfer (bitblt) for a video processor.

-   The [**GetVideoProcessBltStatePrivate**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_dxvahd_getvideoprocessbltstateprivate) function retrieves the state data of a private bitblt for a video processor.

-   The [**SetVideoProcessStreamState**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_dxvahd_setvideoprocessstreamstate) function sets the state of a stream for a video processor.

-   The [**GetVideoProcessStreamStatePrivate**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_dxvahd_getvideoprocessstreamstateprivate) function retrieves the private stream-state data for a video processor.

-   The [**VideoProcessBltHD**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_dxvahd_videoprocessblthd) function processes video input streams and composes to an output surface.

-   The [**DestroyVideoProcessor**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_dxvahd_destroyvideoprocessor) function releases resources for a previously created video processor.

 

