---
title: DXVA-HD DDI Programming Considerations
description: DXVA-HD DDI Programming Considerations
ms.assetid: 84576a8d-67e1-480a-9323-ef34b0900d22
keywords:
- DXVA-HD DDI WDK Windows 7 display , programming considerations
- DXVA-HD DDI WDK Server 2008 R2 display , programming considerations
- high-definition video WDK Windows 7 display , DXVA-HD DDI, programming considerations
- high-definition video WDK Server 2008 R2 display , DXVA-HD DDI, programming considerations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DXVA-HD DDI Programming Considerations


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

When you implement the [DXVA-HD DDI](dxva-hd-ddi.md) in your user-mode display driver, you should consider the following programming tips:

-   The driver must set the D3DCAPS3\_DXVAHD (0x00000400L) bit in the **Caps3** member of [D3DCAPS9](http://go.microsoft.com/fwlink/p/?linkid=122122) structure to indicate that it supports the DXVA-HD DDI, otherwise the Direct3D runtime fails to call the [**CreateVideoProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff540732) function to create a DXVA-HD device. The D3DCAPS9 structure is described in the DirectX 9.0 SDK documentation. The driver sets the D3DCAPS3\_DXVAHD bit in response to a call to its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function in which the D3DDDICAPS\_GETD3D9CAPS value is set in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter points to.

-   The DXVAHD\_SURFACE\_TYPE\_VIDEO\_INPUT\_PRIVATE value of the application-level DXVAHD\_SURFACE\_TYPE enumeration has no corresponding DDI value. An application sets the DXVAHD\_SURFACE\_TYPE\_VIDEO\_INPUT\_PRIVATE value for an off-screen plain surface that is allocated in different format type for the CPU or a shader-base video processor plug-in.

-   The DXVAHD\_SURFACE\_TYPE\_VIDEO\_OUTPUT value of the application-level DXVAHD\_SURFACE\_TYPE enumeration corresponds to the **VideoProcessRenderTarget** bit-field flag of the [**D3DDDI\_RESOURCEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544644) structure. The Direct3D runtime sets **VideoProcessRenderTarget** in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure when the runtime calls the driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function to create a video processing render target.

-   The Direct3D runtime maintains both bit-block transfer (bitblt) and stream states. The runtime returns to the application when the runtime is queried.

-   The application-level **IDXVAHD\_VideoProcessor::GetVideoProcessBltState** method has no corresponding DDI function. However, when an application calls **IDXVAHD\_VideoProcessor::GetVideoProcessBltState** to retrieve the private bitblt state data for a video processor, the Direct3D runtime calls the driver's [**GetVideoProcessBltStatePrivate**](https://msdn.microsoft.com/library/windows/hardware/ff566812) function.

-   The application-level **IDXVAHD\_VideoProcessor::GetVideoProcessStreamState** method has no corresponding DDI function. However, when an application calls **IDXVAHD\_VideoProcessor::GetVideoProcessBltState** to retrieve the private stream state data for a video processor, the Direct3D runtime calls the driver's [**GetVideoProcessStreamStatePrivate**](https://msdn.microsoft.com/library/windows/hardware/ff566815) function.

-   The DXVAHD\_STREAM\_STATE\_D3DFORMAT value of the application-level DXVAHD\_STREAM\_STATE enumeration has no corresponding DDI value in the [**DXVAHDDDI\_STREAM\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff563068) enumeration. The video processor plug-in uses the DXVAHD\_STREAM\_STATE\_D3DFORMAT value for a surface that is allocated with the DXVAHD\_SURFACE\_TYPE\_VIDEO\_INPUT\_PRIVATE value of the application-level DXVAHD\_SURFACE\_TYPE enumeration.

-   The DXVAHD\_DEVICE\_TYPE enumeration has no corresponding DDI enumeration (for example, no DXVAHDDDI\_DEVICE\_TYPE). The first member of the [**DXVAHDDDI\_VPDEVCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff563113) structure is reserved whereas the first member of the application-level DXVAHD\_VPDEVCAPS structure is set to a DXVAHD\_DEVICE\_TYPE value in the **DeviceType** member. The **DeviceType** member is set by the runtime or the video processor plug-in, which always reports the driver as DXVAHD\_DEVICE\_TYPE\_HARDWARE.

-   The **Multiplier** member of the [**DXVAHDDDI\_FILTER\_RANGE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff563055) structure is a floating-point value. The driver should use a value that can be represented exactly as a base 2 fraction. For example, 0.25 can be represented exactly as a base 2 fraction but 0.1 cannot.

-   Any [DXVA-HD DDI](dxva-hd-ddi.md) function should return S\_OK, E\_INVALIDARG or E\_OUTOFMEMORY.

 

 





