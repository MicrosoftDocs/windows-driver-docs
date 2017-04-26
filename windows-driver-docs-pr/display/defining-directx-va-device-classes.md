---
title: Defining DirectX VA Device Classes
description: Defining DirectX VA Device Classes
ms.assetid: a4b2ee88-747a-48c3-ba1d-2d605c46db58
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , defining device classes
- device classes WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Defining DirectX VA Device Classes


## <span id="ddk_defining_directx_va_device_classes_gg"></span><span id="DDK_DEFINING_DIRECTX_VA_DEVICE_CLASSES_GG"></span>


Use the example code in this section to define device classes for the deinterlace container device, ProcAmp control device, deinterlace mode device (for example, [bob](bob-deinterlacing.md)), and COPP device. These device classes contain declarations for member functions that comprise the [ProcAmp Control DDI](https://msdn.microsoft.com/library/windows/hardware/ff569186) and [Deinterlace DDI](https://msdn.microsoft.com/library/windows/hardware/ff552701). These device class definitions can be declared in a driver-supplied header file.

Use the following example code to define each device type and a base class that applies to each device type:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Defining%20DirectX%20VA%20Device%20Classes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




