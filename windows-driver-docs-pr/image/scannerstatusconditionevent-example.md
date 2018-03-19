---
title: ScannerStatusConditionEvent Example
description: ScannerStatusConditionEvent Example
ms.assetid: 925aa3d6-2218-4095-8d78-de1ebd1adeee
keywords: ["ScannerStatusConditionEvent Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ScannerStatusConditionEvent Example


In the following example, the scanner notifies the control point of a scan lamp failure.

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
      http://schemas.microsoft.com/windows/2006/08/wdp/scan/ScannerStatusConditionEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>
  <soap:Body>
    <dsd:ScannerStatusConditionEvent>
      <dsd:DeviceCondition Id="1543">
        <wscn:Time>2006-01-21T17:22:27.5242689Z</wscn:Time>
        <wscn:Name>LampError</wscn:Name>
        <wscn:Component>Platen</wscn:Component>
        <wscn:Severity>Critical</wscn:Severity>
      </dsd:DeviceCondition>
    </dsd:ScannerStatusConditionEvent>
  </soap:Body>
</soap:Envelope
```

 

 





