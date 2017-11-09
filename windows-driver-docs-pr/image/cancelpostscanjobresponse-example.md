---
title: CancelPostScanJobResponse Example
description: CancelPostScanJobResponse Example
MS-HAID:
- 'dsm\_ref\_dsp\_0165f7d8-b71b-4231-83de-946a03c46de4.xml'
- 'image.cancelpostscanjobresponse\_example'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6562896c-d718-4d19-948a-028f533cf886
keywords: ["CancelPostScanJobResponse Example"]
---

# CancelPostScanJobResponse Example


The following is an example of a SOAP message from a DSM scan server that contains a **CancelPostScanJobResponse** element:

```
<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
        xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
  <soap:Header>
    <wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To>
    <wsa:Action>http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/CancelPostScanJobResponse</wsa:Action>
    <wsa:MessageID>urn:uuid:d6d94676-39bf-4ed9-abc1-61d652f38a39</wsa:MessageID>
    <wsa:RelatesTo>urn:uuid:851d1de6-2bf1-4cc3-af55-dc8b462c505e</wsa:RelatesTo>
  </soap:Header>
  <soap:Body>
    <dsp:CancelPostScanJobResponse/>
  </soap:Body>
</soap:Envelope>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CancelPostScanJobResponse%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




