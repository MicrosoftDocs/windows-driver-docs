---
title: JobStatusEvent.JobStatus.JobStatusEvent Example
description: JobStatusEvent.JobStatus.JobStatusEvent Example
ms.assetid: eee045c6-1116-4187-b0d6-e907f0699008
keywords: ["JobStatusEvent.JobStatus.JobStatusEvent Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# JobStatusEvent.JobStatus.JobStatusEvent Example


In the following example, the scanner notifies the control point of the current state of job 253.

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
      http://schemas.microsoft.com/windows/2006/08/wdp/scan/JobStatusEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>
  <soap:Body>
    <dsd:JobStatusEvent>
      <dsd:JobStatus>
        <wscn:JobId>253</wscn:JobId>
        <wscn:JobState>Processing</wscn:JobState>
        <wscn:JobStateReasons>
          <wscn:JobStateReason>JobScanning</wscn:JobStateReason>
        </wscn:JobStateReasons>
        <wscn:ScansCompleted>4</wscn:ScansCompleted>
        <wscn:JobCreatedTime>2006-01-24T11:34:35.8345Z</wscn:JobCreatedTime>
      </dsd:JobStatus>
    </dsd:JobStatusEvent>
  </soap:Body>
</soap:Envelope>
```

 

 





