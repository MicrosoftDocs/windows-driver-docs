---
title: SendImageResponse Example
description: SendImageResponse Example
ms.assetid: 6590c00d-7dcf-4d0f-84fe-ec9497631433
keywords: ["SendImageResponse Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 





