---
title: SendImageRequest Example
description: SendImageRequest Example
ms.assetid: bf14727b-3c03-4d80-8780-32806bd680f5
keywords: ["SendImageRequest Example"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20SendImageRequest%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




