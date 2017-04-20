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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Providing Capabilities for Video Processing


When its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function is called, the user-mode display driver provides the following video processing capabilities based on the request type (which is specified in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter points to):

<span id="D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT_and_D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS_request_types"></span><span id="d3dddicaps_getvideoprocessordeviceguidcount_and_d3dddicaps_getvideoprocessordeviceguids_request_types"></span><span id="D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT_AND_D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS_REQUEST_TYPES"></span>D3DDDICAPS\_GETVIDEOPROCESSORDEVICEGUIDCOUNT and D3DDDICAPS\_GETVIDEOPROCESSORDEVICEGUIDS request types  
The user-mode display driver returns the number and a list of the following GUIDs that it supports for video processing. The Microsoft Direct3D runtime specifies the [**DXVADDI\_VIDEODESC**](https://msdn.microsoft.com/library/windows/hardware/ff562944) structure for a particular video stream to process in a variable that the **pInfo** member of D3DDDIARG\_GETCAPS points to. The runtime first requests the number of supported GUIDs followed by a request for the list of supported GUIDs.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Providing%20Capabilities%20for%20Video%20Processing%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




