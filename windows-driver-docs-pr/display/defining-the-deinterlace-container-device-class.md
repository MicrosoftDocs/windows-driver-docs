---
title: Defining the Deinterlace Container Device Class
description: Defining the Deinterlace Container Device Class
keywords:
- deinterlace container device WDK DirectX VA
- container device WDK DirectX VA
ms.date: 04/20/2017
---

# Defining the Deinterlace Container Device Class


## <span id="ddk_defining_the_deinterlace_container_device_class_gg"></span><span id="DDK_DEFINING_THE_DEINTERLACE_CONTAINER_DEVICE_CLASS_GG"></span>


Use the following example code to define the deinterlace container device class:

```cpp
// Deinterlace container device class.
struct DXVA_DeinterlaceContainerDeviceClass : public DXVA_DeviceBaseClass
{
    // Uses the base class's constructor.
    DXVA_DeinterlaceContainerDeviceClass(const GUID& guid, DXVA_DeviceType Type) :
        DXVA_DeviceBaseClass(guid, Type)
    {}
     // Part of the Deinterlace DDI.
    HRESULT DeinterlaceQueryAvailableModes(
        LPDXVA_VideoDesc lpVideoDescription,
        LPDWORD lpdwNumModesSupported,
        LPGUID pGuidsDeinterlaceModes
        );
    // Part of the Deinterlace DDI.
    HRESULT DeinterlaceQueryModeCaps(
        LPGUID pGuidDeinterlaceMode,
        LPDXVA_VideoDesc lpVideoDescription,
        LPDXVA_DeinterlaceCaps lpDeinterlaceCaps
        );
     // Part of the ProcAmp Control DDI.
    HRESULT ProcAmpControlQueryCaps(
        LPDXVA_VideoDesc lpVideoDescription,
        LPDXVA_ProcAmpControlCaps lpProcAmpControlCaps
        );
    // Part of the ProcAmp Control DDI.
    HRESULT ProcAmpControlQueryRange(
        DWORD VideoProperty,
        LPDXVA_VideoDesc lpVideoDescription,
        LPDXVA_VideoPropertyRange lpProcAmpControlRange
        );
};
```

 

 





