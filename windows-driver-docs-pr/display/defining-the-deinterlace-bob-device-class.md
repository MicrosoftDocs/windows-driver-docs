---
title: Defining the Deinterlace Bob Device Class
description: Defining the Deinterlace Bob Device Class
ms.assetid: 1efe0a08-c3aa-4083-a19f-96e5ba94d517
keywords:
- deinterlacing WDK DirectX VA , bob
- bob deinterlacing WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining the Deinterlace Bob Device Class


## <span id="ddk_defining_the_deinterlace_bob_device_class_gg"></span><span id="DDK_DEFINING_THE_DEINTERLACE_BOB_DEVICE_CLASS_GG"></span>


Use the following example code to define the deinterlace bob device class:

```cpp
// Deinterlace bob device class.
struct DXVA_DeinterlaceBobDeviceClass : public DXVA_DeviceBaseClass
{
    DXVA_VideoDesc  m_VideoDesc;
    // Uses the base class&#39;s constructor.
    DXVA_DeinterlaceBobDeviceClass(const GUID& guid, DXVA_DeviceType Type) :
        DXVA_DeviceBaseClass(guid, Type)
    {}
    // The following functions are part of the 
     // Deinterlace DDI.
    HRESULT DeinterlaceOpenStream(LPDXVA_VideoDesc lpVideoDescription);
    HRESULT DeinterlaceCloseStream();
    HRESULT DeinterlaceBlt(
                           REFERENCE_TIME  rtTargetFrame,
                           LPRECT  lprcDstRect,
                           LPDDSURFACE  lpDDSDstSurface,
                           LPRECT  lprcSrcRect,
                           LPDXVA_VideoSample  lpDDSrcSurfaces,
                           DWORD  dwNumSurfaces,
                           FLOAT  fAlpha);
    HRESULT DeinterlaceBltEx(
                           REFERENCE_TIME  rtTargetFrame,
                           LPRECT  lprcTargetRect,
                           DXVA_AYUVsample2  BackgroundColor,
                           DWORD  dwDestinationFormat,
                           DWORD  dwDestinationFlags,
                           LPDDSURFACE  lpDDSDstSurface,
                           LPDXVA_VideoSample2  lpDDSrcSurfaces,
                           DWORD  dwNumSurfaces,
                           FLOAT  fAlpha);
};
```

 

 





