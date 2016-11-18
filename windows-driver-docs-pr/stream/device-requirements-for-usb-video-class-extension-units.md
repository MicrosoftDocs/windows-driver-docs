---
title: Device Requirements for USB Video Class Extension Units
author: windows-driver-content
description: Device Requirements for USB Video Class Extension Units
MS-HAID:
- 'uvcds\_7CD70909-0244-4D09-B285-5D19A4AB3290.xml'
- 'stream.device\_requirements\_for\_usb\_video\_class\_extension\_units'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4678c3a4-9ca7-4518-afe8-99a9e61f3dcd
keywords: ["extension units WDK USB Video Class , device requirements", "Extension Unit descriptor WDK USB Video Class", "descriptors WDK USB Video Class", "Extension Unit controls WDK USB Video Class", "controls WDK USB Video Class"]
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Device%20Requirements%20for%20USB%20Video%20Class%20Extension%20Units%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


