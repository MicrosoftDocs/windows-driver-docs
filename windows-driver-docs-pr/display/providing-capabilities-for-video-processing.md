---
title: Providing Capabilities for Video Processing
description: Providing Capabilities for Video Processing
keywords:
- video processing WDK DirectX VA , capabilities provided by request type
- D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT
- D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS
- D3DDDICAPS_GETVIDEOPROCESSORCAPS
- D3DDDICAPS_GETPROCAMPRANGE
- D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT
- D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS
- D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT
- D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS
- D3DDDICAPS_FILTERPROPERTYRANGE
ms.date: 10/22/2021
ms.localizationpriority: medium
---

# Providing video processing capabilities

## How to query capabilities for video processing

When its [**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) function is called, the user-mode display driver (UMD) provides the following video processing capabilities based on the request type specified in the **Type** member of the [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) structure that the *pData* parameter points to:

## D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT and D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS request types

The Direct3D runtime specifies the [**DXVADDI_VIDEODESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_videodesc) structure for a particular video stream to process in a variable that the **pInfo** member of D3DDDIARG_GETCAPS points to. The D3D runtime first requests the number of supported GUIDs followed by a request for the list of supported GUIDs. The UMD returns the number and a list of the following GUIDs that it supports for video processing.

```cpp
DEFINE_GUID(DXVADDI_VideoProcProgressiveDevice,  0x5a54a0c9,0xc7ec,0x4bd9,0x8e,0xde,0xf3,0xc7,0x5d,0xc4,0x39,0x3b);
DEFINE_GUID(DXVADDI_VideoProcBobDevice,  0x335aa36e,0x7884,0x43a4,0x9c,0x91,0x7f,0x87,0xfa,0xf3,0xe3,0x7e);
```

## D3DDDICAPS_GETVIDEOPROCESSORCAPS request type

Each video-processor mode that the UMD supports can have unique capabilities. The UMD returns those capabilities when the D3DDDICAPS_GETVIDEOPROCESSORCAPS request type is passed. The Direct3D runtime specifies a [**DXVADDI_VIDEOPROCESSORINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_videoprocessorinput) structure for the video-processing mode to retrieve capabilities for in a variable that the **pInfo** member of [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) points to. The UMD returns capabilities for the video-processing mode in a [**DXVADDI_VIDEOPROCESSORCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_videoprocessorcaps) structure that the **pData** member of D3DDDIARG_GETCAPS points to.

## D3DDDICAPS_GETPROCAMPRANGE request type

The UMD returns a pointer to a [**DXVADDI_VALUERANGE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_valuerange) structure that contains the range of allowed values for a particular ProcAmp control property on a particular video stream. The Direct3D runtime specifies a [**DXVADDI_QUERYPROCAMPINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_queryprocampinput) structure for the ProcAmp control property on a particular video stream in a variable that the **pInfo** member of D3DDDIARG_GETCAPS points to.

## D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT and D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS request types

The UMD returns the number and a list of render target formats that it supports for a particular video processing mode. The Direct3D runtime specifies a [**DXVADDI_VIDEOPROCESSORINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_videoprocessorinput) structure for the video-processor mode in a variable that the **pInfo** member of D3DDDIARG_GETCAPS points to. The UMD returns render target formats that it supports in an array of [**D3DDDIFORMAT**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddiformat)-typed values that the **pData** member of D3DDDIARG_GETCAPS specifies.

## D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT and D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS request types

The UMD returns the number and a list of sub-stream formats that it supports for a particular video processing mode. The Direct3D runtime specifies a [**DXVADDI_VIDEOPROCESSORINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_videoprocessorinput) structure for the video-processor mode in a variable that the **pInfo** member of D3DDDIARG_GETCAPS points to. The UMD returns sub-stream formats that it supports in an array of [**D3DDDIFORMAT**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddiformat)-typed values that the **pData** member of D3DDDIARG_GETCAPS specifies.

## D3DDDICAPS_FILTERPROPERTYRANGE request type

The UMD returns a pointer to a [**DXVADDI_VALUERANGE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_valuerange) structure that contains the range of allowed values for a particular filter setting on a particular video stream when the D3DDDICAPS_FILTERPROPERTYRANGE request type is passed. The Direct3D runtime specifies a [**DXVADDI_QUERYFILTERPROPERTYRANGEINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_queryfilterpropertyrangeinput) structure for the filter setting on a particular video stream in a variable that the **pInfo** member of D3DDDIARG_GETCAPS points to.
