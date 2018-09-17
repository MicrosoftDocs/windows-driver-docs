---
title: JobEndStateEvent Example
description: JobEndStateEvent Example
ms.assetid: dfd52358-ffa7-4d9a-ab18-99478c46f3b8
keywords: ["JobEndStateEvent Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# JobEndStateEvent Example


In the following example, the scanner notifies the control point of the final state and status of job 253.

```
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:wse="http://schemas.xmlsoap.org/ws/2004/08/eventing"
    xmlns:wscn="http://schemas.microsoft.com/windows/2006/08/wdp/scan" 
    xmlns:dsd="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/device">
  <soap:Header>
    <wsa:To>AddressofEventSink</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/08/wdp/scan/JobEndStateEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>
  <soap:Body>
    <dsd:JobEndStateEvent>
      <dsd:JobEndState>
        <wscn:JobId>253</wscn:JobId>
        <wscn:JobCompletedState>Completed</wscn:JobCompletedState>
        <wscn:JobCompletedStateReasons>
          <wscn:JobStateReason>JobCompletedWithWarnings</wscn:JobStateReason>
        </wscn:JobCompletedStateReasons>
        <wscn:JobName>Scan from Imaging App</wscn:JobName>
        <wscn:JobOriginatingUserName>User</wscn:JobOriginatingUserName>
        <wscn:ScansCompleted>7</wscn:ScansCompleted>
        <wscn:JobCompletedTime>
          2006-01-24T11:37:05.673Z
        </wscn:JobCompletedTime>
      </dsd:JobEndState>
      </dsd:JobEndStateEvent>
    </soap:Body>
</soap:Envelope>
```

 

 





