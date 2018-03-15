---
title: ScannerStatusConditionClearedEvent Example
description: ScannerStatusConditionClearedEvent Example
ms.assetid: 54a51c31-c629-413e-842f-2ae1acf966ee
keywords: ["ScannerStatusConditionClearedEvent Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ScannerStatusConditionClearedEvent Example


In the following example, the scanner notifies the control point that the condition number 1543 has cleared.

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
      http://schemas.microsoft.com/windows/2006/08/wdp/scan/ScannerStatusConditionClearedEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>
  <soap:Body>
    <dsd:ScannerStatusConditionClearedEvent>
      <dsd:DeviceConditionCleared>
        <wscn:ConditionId>1543</wscn:ConditionId>
        <wscn:ConditionClearTime>2006-01-21T17:22:35.8345Z</wscn:ConditionClearTime>
      </dsd:DeviceConditionCleared>
    </dsd:ScannerStatusConditionClearedEvent>
  </soap:Body>
</soap:Envelope>
```

 

 





