---
title: CreatePostScanJobResponse Example
description: CreatePostScanJobResponse Example
ms.assetid: 3af44534-2609-419c-836e-294b60de64e4
keywords: ["CreatePostScanJobResponse Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





