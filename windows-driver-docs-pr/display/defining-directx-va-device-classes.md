---
title: Defining DirectX VA Device Classes
description: Defining DirectX VA Device Classes
ms.assetid: a4b2ee88-747a-48c3-ba1d-2d605c46db58
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , defining device classes
- device classes WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining DirectX VA Device Classes


## <span id="ddk_defining_directx_va_device_classes_gg"></span><span id="DDK_DEFINING_DIRECTX_VA_DEVICE_CLASSES_GG"></span>


Use the example code in this section to define device classes for the deinterlace container device, ProcAmp control device, deinterlace mode device (for example, [bob](bob-deinterlacing.md)), and COPP device. These device classes contain declarations for member functions that comprise the [ProcAmp Control DDI](https://msdn.microsoft.com/library/windows/hardware/ff569186) and [Deinterlace DDI](https://msdn.microsoft.com/library/windows/hardware/ff552701). These device class definitions can be declared in a driver-supplied header file.

Use the following example code to define each device type and a base class that applies to each device type:

```cpp
// These enumerated types specify the DirectX VA device class.
enum DXVA_DeviceType {
    DXVA_DeviceContainer        = 0x0001,
    DXVA_DeviceDecoder          = 0x0002,
    DXVA_DeviceDeinterlacer     = 0x0003,
     DXVA_DeviceProcAmpControl   = 0x0004,
    DXVA_DeviceCOPP             = 0x0005
};
// Other DirectX VA device classes inherit from this base class, 
struct DXVA_DeviceBaseClass {
    GUID            m_DeviceGUID;
    DXVA_DeviceType m_DeviceType;

    DXVA_DeviceBaseClass(const GUID& guid, DXVA_DeviceType Type) :
        m_DeviceGUID(guid), m_DeviceType(Type)
    {}
};
```

The following topics contain example code that defines classes for the deinterlace container device, ProcAmp control device, deinterlace bob device, and COPP device:

[Defining the Deinterlace Container Device Class](defining-the-deinterlace-container-device-class.md)

[Defining the ProcAmp Control Device Class](defining-the-procamp-control-device-class.md)

[Defining the Deinterlace Bob Device Class](defining-the-deinterlace-bob-device-class.md)

[Defining the COPP Device Class](defining-the-copp-device-class.md)

 

 





