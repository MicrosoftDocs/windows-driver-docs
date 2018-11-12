---
title: ScannerStatusSummaryEvent element
description: The required ScannerStatusSummaryEvent element informs the client that the scan device's status has changed.
ms.assetid: a1297e25-1136-49ef-8b8e-e7c8c62bec13
keywords: ["ScannerStatusSummaryEvent element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerStatusSummaryEvent
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScannerStatusSummaryEvent element


The required **ScannerStatusSummaryEvent** element informs the client that the scan device's status has changed.

Usage
-----

```xml
<wscn:ScannerStatusSummaryEvent>
  child elements
</wscn:ScannerStatusSummaryEvent>
```

Attributes
----------

There are no attributes.

## Child elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="statussummary.md" data-raw-source="[&lt;strong&gt;StatusSummary&lt;/strong&gt;](statussummary.md)"><strong>StatusSummary</strong></a></p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service should send a **ScannerStatusSummaryEvent** element to the client whenever the scan device's status changes.

The body of **ScannerStatusSummaryEvent** must contain a [**StatusSummary**](statussummary.md) element that describes the changes to the scanner's status.

Examples
--------

The following code example indicates that the scan device is stopped because of a jam in the media feed path.

```xml
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
  xmlns:wse="http://schemas.xmlsoap.org/ws/2004/08/eventing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='http://www.w3.org/2002/12/soap-encoding'>

  <soap:Header>
    <wsa:To>AddressofEventSink</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/ScannerStatusSummaryEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:ScannerStatusSummaryEvent>
      <wscn:StatusSummary>
        <wscn:ScannerState>Stopped</wscn:ScannerState>
        <wscn:ScannerStateReasons>
          <wscn:ScannerStateReason>MediaJam</wscn:ScannerStateReason>
        </wscn:ScannerStateReasons>
      </wscn:StatusSummary>
    </wscn:ScannerStatusSummaryEvent>
  </soap:Body
</soap:Envelope>
```

## See also


[**StatusSummary**](statussummary.md)

 

 






