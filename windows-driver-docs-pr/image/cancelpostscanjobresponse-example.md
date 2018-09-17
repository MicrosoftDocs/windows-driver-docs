---
title: CancelPostScanJobResponse Example
description: CancelPostScanJobResponse Example
ms.assetid: 6562896c-d718-4d19-948a-028f533cf886
keywords: ["CancelPostScanJobResponse Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 





