---
title: ScannerStatusSummaryEvent Element
description: The required ScannerStatusSummaryEvent element informs the client that the scan device's status has changed.
keywords: ["ScannerStatusSummaryEvent element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerStatusSummaryEvent
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerStatusSummaryEvent element

The required **ScannerStatusSummaryEvent** element informs the client that the scan device's status has changed.

## Usage

```xml
<wscn:ScannerStatusSummaryEvent>
  child elements
</wscn:ScannerStatusSummaryEvent>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**StatusSummary**](statussummary.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service should send a **ScannerStatusSummaryEvent** element to the client whenever the scan device's status changes.

The body of **ScannerStatusSummaryEvent** must contain a [**StatusSummary**](statussummary.md) element that describes the changes to the scanner's status.

## Examples

The following code example indicates that the scan device is stopped because of a jam in the media feed path.

```xml
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2004/08/addressing"
  xmlns:wse="https://schemas.xmlsoap.org/ws/2004/08/eventing"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding'>

  <soap:Header>
    <wsa:To>AddressofEventSink</wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/ScannerStatusSummaryEvent
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
