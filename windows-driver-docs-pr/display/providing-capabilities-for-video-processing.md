---
title: Providing Capabilities for Video Processing
description: Providing Capabilities for Video Processing
ms.assetid: 27507971-1545-44d9-885a-295b9357bdfe
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing Capabilities for Video Processing


When its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function is called, the user-mode display driver provides the following video processing capabilities based on the request type (which is specified in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter points to):

<span id="D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT_and_D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS_request_types"></span><span id="d3dddicaps_getvideoprocessordeviceguidcount_and_d3dddicaps_getvideoprocessordeviceguids_request_types"></span><span id="D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT_AND_D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS_REQUEST_TYPES"></span>D3DDDICAPS\_GETVIDEOPROCESSORDEVICEGUIDCOUNT and D3DDDICAPS\_GETVIDEOPROCESSORDEVICEGUIDS request types  
The user-mode display driver returns the number and a list of the following GUIDs that it supports for video processing. The Microsoft Direct3D runtime specifies the [**DXVADDI\_VIDEODESC**](https://msdn.microsoft.com/library/windows/hardware/ff562944) structure for a particular video stream to process in a variable that the **pInfo** member of D3DDDIARG\_GETCAPS points to. The runtime first requests the number of supported GUIDs followed by a request for the list of supported GUIDs.

```cpp
DEFINE_GUID(DXVADDI_VideoProcProgressiveDevice,  0x5a54a0c9,0xc7ec,0x4bd9,0x8e,0xde,0xf3,0xc7,0x5d,0xc4,0x39,0x3b);
DEFINE_GUID(DXVADDI_VideoProcBobDevice,  0x335aa36e,0x7884,0x43a4,0x9c,0x91,0x7f,0x87,0xfa,0xf3,0xe3,0x7e);
```

<span id="D3DDDICAPS_GETVIDEOPROCESSORCAPS_request_type"></span><span id="d3dddicaps_getvideoprocessorcaps_request_type"></span><span id="D3DDDICAPS_GETVIDEOPROCESSORCAPS_REQUEST_TYPE"></span>D3DDDICAPS\_GETVIDEOPROCESSORCAPS request type  
Each video-processor mode that the user-mode display driver supports can have unique capabilities. The user-mode display driver returns those capabilities when the D3DDDICAPS\_GETVIDEOPROCESSORCAPS request type is passed. The Direct3D runtime specifies a [**DXVADDI\_VIDEOPROCESSORINPUT**](https://msdn.microsoft.com/library/windows/hardware/ff562956) structure for the video-processing mode to retrieve capabilities for in a variable that the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) points to. The user-mode display driver returns capabilities for the video-processing mode in a [**DXVADDI\_VIDEOPROCESSORCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562953) structure that the **pData** member of D3DDDIARG\_GETCAPS points to.

<span id="D3DDDICAPS_GETPROCAMPRANGE_request_type_"></span><span id="d3dddicaps_getprocamprange_request_type_"></span><span id="D3DDDICAPS_GETPROCAMPRANGE_REQUEST_TYPE_"></span>D3DDDICAPS\_GETPROCAMPRANGE request type   
The user-mode display driver returns a pointer to a [**DXVADDI\_VALUERANGE**](https://msdn.microsoft.com/library/windows/hardware/ff562939) structure that contains the range of allowed values for a particular ProcAmp control property on a particular video stream. The Direct3D runtime specifies a [**DXVADDI\_QUERYPROCAMPINPUT**](https://msdn.microsoft.com/library/windows/hardware/ff562935) structure for the ProcAmp control property on a particular video stream in a variable that the **pInfo** member of D3DDDIARG\_GETCAPS points to.

<span id="D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT_and_D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS_request_types"></span><span id="d3dddicaps_getvideoprocessorrtformatcount_and_d3dddicaps_getvideoprocessorrtformats_request_types"></span><span id="D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT_AND_D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS_REQUEST_TYPES"></span>D3DDDICAPS\_GETVIDEOPROCESSORRTFORMATCOUNT and D3DDDICAPS\_GETVIDEOPROCESSORRTFORMATS request types  
The user-mode display driver returns the number and a list of render target formats that it supports for a particular video processing mode. The Direct3D runtime specifies a [**DXVADDI\_VIDEOPROCESSORINPUT**](https://msdn.microsoft.com/library/windows/hardware/ff562956) structure for the video-processor mode in a variable that the **pInfo** member of D3DDDIARG\_GETCAPS points to. The user-mode display driver returns render target formats that it supports in an array of [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312)-typed values that the **pData** member of D3DDDIARG\_GETCAPS specifies.

<span id="D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT_and_D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS_request_types"></span><span id="d3dddicaps_getvideoprocessorrtsubstreamformatcount_and_d3dddicaps_getvideoprocessorrtsubstreamformats_request_types"></span><span id="D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT_AND_D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS_REQUEST_TYPES"></span>D3DDDICAPS\_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT and D3DDDICAPS\_GETVIDEOPROCESSORRTSUBSTREAMFORMATS request types  
The user-mode display driver returns the number and a list of sub-stream formats that it supports for a particular video processing mode. The Direct3D runtime specifies a [**DXVADDI\_VIDEOPROCESSORINPUT**](https://msdn.microsoft.com/library/windows/hardware/ff562956) structure for the video-processor mode in a variable that the **pInfo** member of D3DDDIARG\_GETCAPS points to. The user-mode display driver returns sub-stream formats that it supports in an array of [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312)-typed values that the **pData** member of D3DDDIARG\_GETCAPS specifies.

<span id="D3DDDICAPS_FILTERPROPERTYRANGE_request_type_"></span><span id="d3dddicaps_filterpropertyrange_request_type_"></span><span id="D3DDDICAPS_FILTERPROPERTYRANGE_REQUEST_TYPE_"></span>D3DDDICAPS\_FILTERPROPERTYRANGE request type   
The user-mode display driver returns a pointer to a [**DXVADDI\_VALUERANGE**](https://msdn.microsoft.com/library/windows/hardware/ff562939) structure that contains the range of allowed values for a particular filter setting on a particular video stream when the D3DDDICAPS\_FILTERPROPERTYRANGE request type is passed. The Direct3D runtime specifies a [**DXVADDI\_QUERYFILTERPROPERTYRANGEINPUT**](https://msdn.microsoft.com/library/windows/hardware/ff562930) structure for the filter setting on a particular video stream in a variable that the **pInfo** member of D3DDDIARG\_GETCAPS points to.

 

 





