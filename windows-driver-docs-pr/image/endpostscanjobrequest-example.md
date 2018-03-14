---
title: EndPostScanJobRequest Example
description: EndPostScanJobRequest Example
ms.assetid: 90e8d9a7-e219-469e-84a2-aa11999993b0
keywords: ["EndPostScanJobRequest Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





