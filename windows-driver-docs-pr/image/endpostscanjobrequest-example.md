---
title: EndPostScanJobRequest Example
description: EndPostScanJobRequest Example
MS-HAID:
- 'dsm\_ref\_dsp\_9c5c7084-bef8-450d-9961-78b9f4bf2e3b.xml'
- 'image.endpostscanjobrequest\_example'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 90e8d9a7-e219-469e-84a2-aa11999993b0
keywords: ["EndPostScanJobRequest Example"]
---

# EndPostScanJobRequest Example


The following is an example of a SOAP message from a DSM device that contains an **EndPostScanJobRequest** element:

```
<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
        xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
  <soap:Header>
    <wsa:To>DestinationAddress</wsa:To>
    <wsa:Action>http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/EndPostScanJob</wsa:Action>
    <wsa:MessageID>urn:uuid:5eb4f990-bc55-459d-8d3f-9794f586fc32</wsa:MessageID>
    <wsa:ReplyTo>
      <wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
    </wsa:ReplyTo>
  </soap:Header>
  <soap:Body>
    <dsp:EndPostScanJobRequest>
      <dsp:JobToken>264a19bf-3604-4603-b59d-b47e0f669a1e</dsp:JobToken>
    </dsp:EndPostScanJobRequest>
  </soap:Body>
</soap:Envelope>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20EndPostScanJobRequest%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




