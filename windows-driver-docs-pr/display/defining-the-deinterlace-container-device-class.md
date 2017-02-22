---
title: Defining the Deinterlace Container Device Class
description: Defining the Deinterlace Container Device Class
ms.assetid: 683c8d89-33d5-4b2a-b24a-4e316c3fa64b
keywords: ["deinterlace container device WDK DirectX VA", "container device WDK DirectX VA"]
---

# Defining the Deinterlace Container Device Class


## <span id="ddk_defining_the_deinterlace_container_device_class_gg"></span><span id="DDK_DEFINING_THE_DEINTERLACE_CONTAINER_DEVICE_CLASS_GG"></span>


Use the following example code to define the deinterlace container device class:

```
// Deinterlace container device class.
struct DXVA_DeinterlaceContainerDeviceClass : public DXVA_DeviceBaseClass
{
    // Uses the base class&#39;s constructor.
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Defining%20the%20Deinterlace%20Container%20Device%20Class%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




