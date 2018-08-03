---
title: GetPostScanJobElementsRequest Example
description: GetPostScanJobElementsRequest Example
ms.assetid: 01d4f19d-247c-4f12-bfcb-ea9ab5311b86
keywords: ["GetPostScanJobElementsRequest Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 





