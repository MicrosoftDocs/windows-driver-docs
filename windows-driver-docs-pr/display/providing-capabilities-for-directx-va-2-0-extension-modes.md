---
title: Providing Capabilities for DirectX VA 2.0 Extension Modes
description: Providing Capabilities for DirectX VA 2.0 Extension Modes
ms.assetid: 86283ac8-a56c-4da9-a3ef-6f4d694130a7
keywords:
- DirectX Video Acceleration WDK display , extended support
- Video Acceleration WDK DirectX , extended support
- VA WDK DirectX , extended support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing Capabilities for DirectX VA 2.0 Extension Modes


When its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function is called, the user-mode display driver provides the following capabilities for DirectX VA 2.0 extension modes based on the request type (which is specified in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter points to):

<span id="D3DDDICAPS_GETEXTENSIONGUIDCOUNT_and_D3DDDICAPS_GETEXTENSIONGUIDS_request_types"></span><span id="d3dddicaps_getextensionguidcount_and_d3dddicaps_getextensionguids_request_types"></span><span id="D3DDDICAPS_GETEXTENSIONGUIDCOUNT_AND_D3DDDICAPS_GETEXTENSIONGUIDS_REQUEST_TYPES"></span>D3DDDICAPS\_GETEXTENSIONGUIDCOUNT and D3DDDICAPS\_GETEXTENSIONGUIDS request types  
The user-mode display driver returns the number and a list of the GUIDs that it supports for extension modes. The runtime first requests the number of supported GUIDs followed by a request for the list of supported GUIDs.

<span id="D3DDDICAPS_GETEXTENSIONCAPS_request_type"></span><span id="d3dddicaps_getextensioncaps_request_type"></span><span id="D3DDDICAPS_GETEXTENSIONCAPS_REQUEST_TYPE"></span>D3DDDICAPS\_GETEXTENSIONCAPS request type  
Each extension mode that the user-mode display driver supports can have unique capabilities. The user-mode display driver returns those capabilities when the D3DDDICAPS\_GETEXTENSIONCAPS request type is passed. The Direct3D runtime specifies a [**DXVADDI\_QUERYEXTENSIONCAPSINPUT**](https://msdn.microsoft.com/library/windows/hardware/ff562926) structure for the extension GUID to retrieve capabilities for in a variable that the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) points to. The user-mode display driver returns capabilities for the extension GUID in a private structure that the **pData** member of D3DDDIARG\_GETCAPS points to.

 

 





