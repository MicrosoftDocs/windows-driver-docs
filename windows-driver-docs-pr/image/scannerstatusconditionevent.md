---
title: ScannerStatusConditionEvent Element
description: The required ScannerStatusConditionEvent element provides the client with detailed information about a single status change in the scan device.
keywords: ["ScannerStatusConditionEvent element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerStatusConditionEvent
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerStatusConditionEvent element

The required **ScannerStatusConditionEvent** element provides the client with detailed information about a single status change in the scan device.

## Usage

```xml
<wscn:ScannerStatusConditionEvent>
  child elements
</wscn:ScannerStatusConditionEvent>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**DeviceCondition**](devicecondition.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service sends a **ScannerStatusConditionEvent** element to a client when a [**DeviceCondition**](devicecondition.md) element is added or changed in the [**ActiveConditions**](activeconditions.md) element table. The body of **ScannerStatusConditionEvent** contains the new or changed **DeviceCondition** element.

The WSD Scan Service should send a [**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md) element to the client when the reported **DeviceCondition** has been cleared.

## Examples

The following code example shows how the scan device notifies the client about a scan lamp failure.

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
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/ScannerStatusConditionEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:ScannerStatusConditionEvent>
      <wscn:DeviceCondition wscn:Id="1543">
        <wscn:Time>2006-01-21T17:22:27.5242689Z</wscn:Time>
        <wscn:Name>LampError</wscn:Name>
        <wscn:Component>Platen</wscn:Component>
        <wscn:Severity>Critical</wscn:Severity>
      </wscn:DeviceCondition>
    </wscn:ScannerStatusConditionEvent>
  </soap:Body
</soap:Envelope>
```

## See also

[**ActiveConditions**](activeconditions.md)

[**DeviceCondition**](devicecondition.md)

[**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md)
