---
title: SendImageRequest Example
description: SendImageRequest Example
ms.assetid: bf14727b-3c03-4d80-8780-32806bd680f5
keywords: ["SendImageRequest Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SendImageRequest Example


The following is an example of a SOAP message from a DSM device that contains a **SendImageRequest** element:

```
mime-version: 1.0
Content-Type: Multipart/Related;
        boundary=e1ac1c8d-11be-4313-999f-a8b0857d5360-3c31c1fe-39ef-4c34-8efd-918cf79f6;
        type="application/xop+xml";
        start="<xml@example.org>";
        start-info="application/soap+xml"
 
--e1ac1c8d-11be-4313-999f-a8b0857d5360-3c31c1fe-39ef-4c34-8efd-918cf79f6
Content-Type: application/xop+xml; type=application/soap+xml
                                   charset=UTF-8
Content-Transfer-Encoding: binary
Content-ID: <xml@example.org>
 
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
     xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
     xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
     xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing"
     xmlns:xop="http://www.w3.org/2004/08/xop/include">
  <soap:Header>
    <wsa:To>DestinationAddress</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/SendImage
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>
  <soap:Body>
    <dsp:SendImageRequest>
      <dsp:JobToken>264a19bf-3604-4603-b59d-b47e0f669a1e</dsp:JobToken>
       <dsp:DocumentDescription>
        <dsp:DocumentId>9</dsp:DocumentId>
        <dsp:Format>png</dsp:Format>
      </dsp:DocumentDescription>
      <dsp:ImageData>
        <xop:Include href="cid:1c696bd7-005a-48d9-9ee9-9adca11f8892@uuid"/>
      </dsp:ImageData>
    </dsp:SendImageRequest>
  </soap:Body>
</soap:Envelope>
 
--e1ac1c8d-11be-4313-999f-a8b0857d5360-3c31c1fe-39ef-4c34-8efd-918cf79f6
Content-Type: application/octet-stream;
Content-Transfer-Encoding: binary
Content-ID: <1c696bd7-005a-48d9-9ee9-9adca11f8892@uuid>
 
Document PDL Data
--e1ac1c8d-11be-4313-999f-a8b0857d5360-3c31c1fe-39ef-4c34-8efd-918cf79f6--
 
 
```

 

 





