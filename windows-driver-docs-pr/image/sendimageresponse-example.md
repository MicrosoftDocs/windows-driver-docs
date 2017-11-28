---
title: SendImageResponse Example
description: SendImageResponse Example
ms.assetid: 6590c00d-7dcf-4d0f-84fe-ec9497631433
keywords: ["SendImageResponse Example"]
---

# SendImageResponse Example


The following is an example of a SOAP message from a DSM scan server that contains a **SendImageResponse** element:

```
<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
        xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
  <soap:Header>
    <wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To>
    <wsa:Action>http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/SendImageResponse</wsa:Action>
    <wsa:MessageID>urn:uuid:a8879038-0bd7-420d-812f-211bfc529415</wsa:MessageID>
    <wsa:RelatesTo>urn:uuid:d4d804f4-4232-484c-b861-a79ac24001cf</wsa:RelatesTo>
  </soap:Header>
  <soap:Body>
    <dsp:SendImageResponse/>
  </soap:Body>
</soap:Envelope>
 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20SendImageResponse%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




