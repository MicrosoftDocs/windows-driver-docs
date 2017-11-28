---
title: CreatePostScanJobResponse Example
description: CreatePostScanJobResponse Example
ms.assetid: 3af44534-2609-419c-836e-294b60de64e4
keywords: ["CreatePostScanJobResponse Example"]
---

# CreatePostScanJobResponse Example


The following is an example of a SOAP message from a DSM scan server that contains a **CreatePostScanJobResponse** element:

```
<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
        xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
  <soap:Header>
    <wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To>
    <wsa:Action>http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/CreatePostScanJobResponse</wsa:Action>
    <wsa:MessageID>urn:uuid:fb5ab95c-08ef-4cc2-8ec0-c4be667b1862</wsa:MessageID>
    <wsa:RelatesTo>urn:uuid:c7a18640-1e15-48ac-8326-0026a5719d98</wsa:RelatesTo>
  </soap:Header>
  <soap:Body>
    <dsp:CreatePostScanJobResponse>
      <dsp:JobToken>264a19bf-3604-4603-b59d-b47e0f669a1e</dsp:JobToken>
    </dsp:CreatePostScanJobResponse>
  </soap:Body>
</soap:Envelope>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CreatePostScanJobResponse%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




