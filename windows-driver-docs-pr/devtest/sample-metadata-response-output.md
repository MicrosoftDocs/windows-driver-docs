---
title: Sample Metadata Response Output
description: Sample Metadata Response Output
ms.assetid: e31cdc1f-21eb-4121-9618-2d8e3d6775dc
keywords:
- WSDBIT tool WDK , sample
- WSDAPI Basic Interoperability Tool WDK , sample
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





