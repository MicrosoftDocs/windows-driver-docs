---
title: GetPostScanJobElementsRequest Example
description: GetPostScanJobElementsRequest Example
MS-HAID:
- 'dsm\_ref\_dsp\_369f46e2-fe74-49b5-867e-59e94e26e61c.xml'
- 'image.getpostscanjobelementsrequest\_example'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 01d4f19d-247c-4f12-bfcb-ea9ab5311b86
keywords: ["GetPostScanJobElementsRequest Example"]
---

# GetPostScanJobElementsRequest Example


The following is an example of a SOAP message from a DSM scan server that contains a **GetPostScanJobElementsRequest** element:

```
<soap:Envelope 
 xmlns:soap="http://www.w3.org/2003/05/soap-envelope" 
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
   xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
 <soap:Header>
    <wsa:To>
 https://DSMScanServer.contoso.com:5362/ScanServer/4d15d73c-bbcd-4cba-beae-07e1f8ea9475
 </wsa:To>
    <wsa:Action>
http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/GetPostScanJobElements
 </wsa:Action>
    <wsa:MessageID>urn:uuid:a79fe111-170d-4699-95d8-a896564aa7d6</wsa:MessageID>
    <wsa:ReplyTo>
      <wsa:Address>
 http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous
 </wsa:Address>
    </wsa:ReplyTo>
 </soap:Header>
 <soap:Body>
    <dsp:GetPostScanJobElementsRequest>
      <dsp:JobToken>0c349cb0-59ed-4d02-b6d5-ebc729c73830</dsp:JobToken>
      <dsp:RequestedElements>
        <dsp:Name>dsp:JobStatus</dsp:Name>
        <dsp:Name>dsp:JobDescription</dsp:Name>
      </dsp:RequestedElements>
    </dsp:GetPostScanJobElementsRequest>
 </soap:Body>
</soap:Envelope>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetPostScanJobElementsRequest%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




