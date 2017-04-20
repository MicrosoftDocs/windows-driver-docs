---
title: Providing Capabilities for DirectX VA 2.0 Extension Modes
description: Providing Capabilities for DirectX VA 2.0 Extension Modes
ms.assetid: 86283ac8-a56c-4da9-a3ef-6f4d694130a7
keywords:
- DirectX Video Acceleration WDK display , extended support
- Video Acceleration WDK DirectX , extended support
- VA WDK DirectX , extended support
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Providing Capabilities for DirectX VA 2.0 Extension Modes


When its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function is called, the user-mode display driver provides the following capabilities for DirectX VA 2.0 extension modes based on the request type (which is specified in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter points to):

<span id="D3DDDICAPS_GETEXTENSIONGUIDCOUNT_and_D3DDDICAPS_GETEXTENSIONGUIDS_request_types"></span><span id="d3dddicaps_getextensionguidcount_and_d3dddicaps_getextensionguids_request_types"></span><span id="D3DDDICAPS_GETEXTENSIONGUIDCOUNT_AND_D3DDDICAPS_GETEXTENSIONGUIDS_REQUEST_TYPES"></span>D3DDDICAPS\_GETEXTENSIONGUIDCOUNT and D3DDDICAPS\_GETEXTENSIONGUIDS request types  
The user-mode display driver returns the number and a list of the GUIDs that it supports for extension modes. The runtime first requests the number of supported GUIDs followed by a request for the list of supported GUIDs.

<span id="D3DDDICAPS_GETEXTENSIONCAPS_request_type"></span><span id="d3dddicaps_getextensioncaps_request_type"></span><span id="D3DDDICAPS_GETEXTENSIONCAPS_REQUEST_TYPE"></span>D3DDDICAPS\_GETEXTENSIONCAPS request type  
Each extension mode that the user-mode display driver supports can have unique capabilities. The user-mode display driver returns those capabilities when the D3DDDICAPS\_GETEXTENSIONCAPS request type is passed. The Direct3D runtime specifies a [**DXVADDI\_QUERYEXTENSIONCAPSINPUT**](https://msdn.microsoft.com/library/windows/hardware/ff562926) structure for the extension GUID to retrieve capabilities for in a variable that the **pInfo** member of [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) points to. The user-mode display driver returns capabilities for the extension GUID in a private structure that the **pData** member of D3DDDIARG\_GETCAPS points to.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Providing%20Capabilities%20for%20DirectX%20VA%202.0%20Extension%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




