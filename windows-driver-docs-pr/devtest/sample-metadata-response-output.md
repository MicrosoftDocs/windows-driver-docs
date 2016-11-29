---
title: Sample Metadata Response Output
description: Sample Metadata Response Output
ms.assetid: e31cdc1f-21eb-4121-9618-2d8e3d6775dc
keywords: ["WSDBIT tool WDK , sample", "WSDAPI Basic Interoperability Tool WDK , sample"]
---

# Sample Metadata Response Output


If wsdbit\_client was used with wsdbit\_server, the following code example shows what the metadata response output on the client side would look like.

**Note**   The host address endpoints will be different every time that the server is run.

 

```
-Dialect:       http://schemas.xmlsoap.org/ws/2006/02/devprof/ThisDevice
Device Metadata
        -FriendlyName [-----]: WSDAPI Basic Interop Server
        -FirmwareVersion:      alpha
        -SerialNumber:         1
        -Any:                  (absent)
End Device Metadata
-Dialect:       http://schemas.xmlsoap.org/ws/2006/02/devprof/ThisModel
Model Metadata
        -Manufacturer [-----]: Microsoft
        -ManufacturerURL:      http://www.microsoft.com/
        -ModelName [-----]:    WSDAPI Interop device
        -ModelNumber:          0.1
        -ModelUrl:             http://www.microsoft.com/
        -PresentationUrl:      http://www.microsoft.com/
        -Any:                  (absent)
End Model Metadata
-Dialect:       http://schemas.xmlsoap.org/ws/2006/02/devprof/Relationship
Relationship Metadata
        -Type:        http://schemas.xmlsoap.org/ws/2006/02/devprof/host
        -Host:
         -Address:     urn:uuid:697f393a-c45f-4bd7-9a57-0990344e4037
         -ServiceId:   http://testdevice.interop/SimpleDevice
         -Type: http://schemas.example.org/SimpleService:SimpleDeviceType
         -Any:         (absent)
        -Hosted[0]:
         -Address:     http://[::1]:5357/697f393a-c45f-4bd7-9a57-0990344e4037
         -Address:     http://127.0.0.1:5357/697f393a-c45f-4bd7-9a57-0990344e4037
         -ServiceId:   http://testdevice.interop/SimpleService1
         -Type: http://schemas.example.org/SimpleService:SimpleService
         -Any:         (absent)
        -Hosted[1]:
         -Address:     http://[::1]:5357/697f393a-c45f-4bd7-9a57-0990344e4037
         -Address:     http://127.0.0.1:5357/697f393a-c45f-4bd7-9a57-0990344e4037
         -ServiceId:   http://testdevice.interop/AttachmentService1
         -Type: http://schemas.example.org/AttachmentService:AttachmentService
         -Any:         (absent)
        -Hosted[2]:
         -Address:     http://[::1]:5357/697f393a-c45f-4bd7-9a57-0990344e4037
         -Address:     http://127.0.0.1:5357/697f393a-c45f-4bd7-9a57-0990344e4037
         -ServiceId:   http://testdevice.interop/EventingService1
         -Type: http://schemas.example.org/EventingService:EventingService
         -Any:         (absent)
End Relationship Metadata
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Sample%20Metadata%20Response%20Output%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




