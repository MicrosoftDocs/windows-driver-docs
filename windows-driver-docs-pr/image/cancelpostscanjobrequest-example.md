---
title: CancelPostScanJobRequest Example
description: CancelPostScanJobRequest Example
ms.assetid: ce750b7b-0a37-4fbb-baf1-4d699d78c938
keywords: ["CancelPostScanJobRequest Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CancelPostScanJobRequest Example


The following is an example of a SOAP message from a DSM device that contains a **CancelPostScanJobRequest** element:

```
<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
        xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
  <soap:Header>
    <wsa:To>Destination Address</wsa:To>
    <wsa:Action>http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/CancelPostScanJob</wsa:Action>
    <wsa:MessageID>urn:uuid:851d1de6-2bf1-4cc3-af55-dc8b462c505e</wsa:MessageID>
    <wsa:ReplyTo>
      <wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
    </wsa:ReplyTo>
  </soap:Header>
  <soap:Body>
    <dsp:CancelPostScanJobRequest>
      <dsp:JobToken>1ba72b60-c873-4d9d-b523-66616fe03ea9</dsp:JobToken>
    </dsp:CancelPostScanJobRequest>
  </soap:Body>
</soap:Envelope>
```

 

 





