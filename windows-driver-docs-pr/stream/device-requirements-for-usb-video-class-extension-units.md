---
title: Device Requirements for USB Video Class Extension Units
description: Device Requirements for USB Video Class Extension Units
ms.assetid: 4678c3a4-9ca7-4518-afe8-99a9e61f3dcd
keywords:
- extension units WDK USB Video Class , device requirements
- Extension Unit descriptor WDK USB Video Class
- descriptors WDK USB Video Class
- Extension Unit controls WDK USB Video Class
- controls WDK USB Video Class
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Requirements for USB Video Class Extension Units


This section describes some specific requirements for implementing an Extension Unit in the device. If these requirements are not met, the USB Video Class driver might not work correctly with the Extension Unit.

## Descriptor


The Extension Unit descriptor must contain a valid, unique GUID. This GUID is used by Usbvideo.sys to expose a property set on the corresponding extension node. You should create a unique GUID for the Extension Unit by using a tool named Guidgen.exe that is included with the Microsoft Windows SDK.

Property identifiers on the Extension Unit property set (KSPROPERTY\_EXTENSION\_UNIT) correspond to similarly numbered extension unit control IDs exposed by the USB Video Class firmware. Extension unit controls can be accessed by using standard KSPROPERTY requests through the IKsControl interface.

The controls on the Extension Unit, known as extension unit control IDs, must be numbered continuously from 1 to some maximum value n. If there are gaps, the USB Video Class driver does not expose the controls that lie beyond the gap. The current implementation of the USB Video Class driver limits the number of controls on an Extension Unit to 31.

Use Property ID=0 (KSPROPERTY\_EXTENSION\_UNIT\_INFO) to get part of the extension unit descriptor, the syntax for which is defined by the Universal Serial Bus Device Class Definition for Video Devices Specification. This specification is available at the [USB Implementers Forum](http://go.microsoft.com/fwlink/p/?linkid=8780) website.

Use Property ID=1 and higher to send requests to the corresponding extension unit control.

Be aware that KSPROPERTY\_EXTENSION\_UNIT\_CONTROL (Property ID=1) is not a real property. Instead, it denotes that identifiers 1 and higher refer to actual extension unit control IDs.

KSPROPERTY\_EXTENSION\_UNIT\_PASS\_THROUGH (Property ID=0xffff) is not implemented.

The following code example, taken from the complete sample shown in the Sample Extension Unit Plug-in DLL, shows how to make a KSPROPERTY\_EXTENSION\_UNIT\_INFO request:

```cpp
ExtensionProp.Property.Set = PROPSETID_VIDCAP_EXTENSION_UNIT;
    ExtensionProp.Property.Id = KSPROPERTY_EXTENSION_UNIT_INFO;
    ExtensionProp.Property.Flags = KSPROPERTY_TYPE_GET | 
                                   KSPROPERTY_TYPE_TOPOLOGY;
    ExtensionProp.NodeId = m_dwNodeId;

    hr = m_pKsControl->KsProperty(
        (PKSPROPERTY) &ExtensionProp,
                  sizeof(ExtensionProp),
        (PVOID) pInfo,
        ulSize,
        &ulBytesReturned);

        return hr;
}
```

## Control Requests


The device must support GET\_CUR, GET\_INFO, GET\_LEN, GET\_MIN, GET\_MAX, GET\_DEF, and GET\_RES requests for all Extension Unit controls according to the USB Video Class specification. If your device does not implement these functions, the corresponding properties will not be exposed to user mode.

During device initialization, the driver issues the following control requests to the device: GET\_INFO, GET\_LEN, GET\_MIN and GET\_MAX. If any of these initial requests fail, Usbvideo.sys disables the particular control.

The value returned by GET\_INFO tells the driver which GET and SET requests are valid for a given control. In addition, GET\_INFO tells the driver whether the control is asynchronous. Asynchronous requests are supported by Status Interrupt Endpoints.

 

 




