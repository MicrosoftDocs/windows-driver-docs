---
title: Defining the ProcAmp Control Device Class
description: Defining the ProcAmp Control Device Class
ms.assetid: 382f5ecf-ce87-4100-adc7-7006cc7dc5ed
keywords:
- ProcAmp WDK DirectX VA , defining device class
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining the ProcAmp Control Device Class


## <span id="ddk_defining_the_procamp_control_device_class_gg"></span><span id="DDK_DEFINING_THE_PROCAMP_CONTROL_DEVICE_CLASS_GG"></span>


Use the following example code to define the ProcAmp control device class:

```cpp
// ProcAmp control device class.
struct DXVA_ProcAmpControlDeviceClass : public DXVA_DeviceBaseClass
{
    DXVA_VideoDesc  m_VideoDesc;
    // Uses the base class&#39;s constructor.
    DXVA_ProcAmpControlDeviceClass(const GUID& guid, DXVA_DeviceType Type) :
        DXVA_DeviceBaseClass(guid, Type)
    {}
    // The following three functions are part of the 
     // ProcAmp Control DDI.
    HRESULT ProcAmpControlOpenStream(LPDXVA_VideoDesc lpVideoDescription);
    HRESULT ProcAmpControlCloseStream();
    HRESULT ProcAmpControlBlt(
                           LPVOID lpDDSDstSurface,
                           LPVOID lpDDSSrcSurface,
                           DXVA_ProcAmpControlBlt* pCcBlt);
};
```

 

 





