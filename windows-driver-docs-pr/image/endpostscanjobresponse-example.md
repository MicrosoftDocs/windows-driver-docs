---
title: EndPostScanJobResponse Example
description: EndPostScanJobResponse Example
ms.assetid: 698afa58-bbe0-4c65-88cc-ed42256e23ec
keywords: ["EndPostScanJobResponse Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# EndPostScanJobResponse Example


The following is an example of a SOAP message from a DSM scan server that contains an **EndPostScanJobResponse** element:

```
<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
        xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
  <soap:Header>
    <wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To>
    <wsa:Action>http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/EndPostScanJobResponse</wsa:Action>
    <wsa:MessageID>urn:uuid:d9067ca0-a1af-4345-9576-2f1f73b4f35d</wsa:MessageID>
    <wsa:RelatesTo>urn:uuid:5eb4f990-bc55-459d-8d3f-9794f586fc32</wsa:RelatesTo>
  </soap:Header>
  <soap:Body>
    <dsp:EndPostScanJobResponse/>
  </soap:Body>
</soap:Envelope>
```

 

 





