---
title: ScannerStatusConditionClearedEvent Element
description: The required ScannerStatusConditionClearedEvent element informs the client that a previously reported DeviceCondition condition has been cleared at the scanner.
keywords: ["ScannerStatusConditionClearedEvent element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerStatusConditionClearedEvent
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerStatusConditionClearedEvent element

The required **ScannerStatusConditionClearedEvent** element informs the client that a previously reported [**DeviceCondition**](devicecondition.md) condition has been cleared at the scanner.

## Usage

```xml
<wscn:ScannerStatusConditionClearedEvent>
  child elements
</wscn:ScannerStatusConditionClearedEvent>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**DeviceConditionCleared**](deviceconditioncleared.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service sends a **ScannerStatusConditionClearedEvent** element when a device condition that is identified in [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md) has been cleared. **ScannerStatusConditionClearedEvent** contains a [**DeviceConditionCleared**](deviceconditioncleared.md) element that contains the cleared condition and the time at which it was cleared.

## Examples

The following code example shows how the device notifies a client that the previous condition that ConditionId 1543 identified has cleared:

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
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/ScannerStatusConditionClearedEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:ScannerStatusConditionClearedEvent>
      <wscn:DeviceConditionCleared>
        <wscn:ConditionId>1543</wscn:ConditionId>
        <wscn:ConditionClearTime>
          2006-01-21T17:22:35.8345Z
        </wscn:ConditionClearTime>
      </wscn:DeviceConditionCleared>
    </wscn:ScannerStatusConditionClearedEvent>
  </soap:Body
</soap:Envelope>
```

## See also

[**ConditionId**](conditionid.md)

[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)
