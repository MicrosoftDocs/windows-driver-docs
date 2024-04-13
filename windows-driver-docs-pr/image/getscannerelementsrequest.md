---
title: GetScannerElementsRequest Element
description: The required GetScannerElementsRequest element enables a client to request information about the scanner.
keywords: ["GetScannerElementsRequest element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn GetScannerElementsRequest
api_type:
- Schema
ms.date: 04/25/2023
---

# GetScannerElementsRequest element

The required **GetScannerElementsRequest** element enables a client to request information about the scanner.

## Usage

```xml
<wscn:GetScannerElementsRequest>
  child elements
</wscn:GetScannerElementsRequest>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**RequestedElements**](requestedelements.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service must support the **GetScannerElementsRequest** operation.

A client can call **GetScannerElementsRequest** to discover standard and vendor-extended elements of the Scan Service's schema. The information that is available to a client includes any part of scanner data that is accessible at the device root level. This information includes the description, configuration, status, default scan ticket, and any vendor extensions to the Scan Service.

If the Scan Service successfully processes **GetScannerElementsRequest**, it returns a [**GetScannerElementsResponse**](getscannerelementsresponse.md) operation with the requested information. Otherwise, the Scan Service should return the appropriate error code.

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

## Examples

In the following code example, the client specifies a single QName value (wscn:ScannerDescription) to query for the scanner's description.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>AddressofScannerService</wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/GetScannerElements
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetScannerElementsRequest>
      <wscn:RequestedElements>
        <wscn:Name>wscn:ScannerDescription</wscn:Name>
      </wscn:RequestedElements>
    </wscn:GetScannerElementsRequest>
  </soap:Body>
</soap:Envelope>
```

The following code example shows a client's request for the scanner's status.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>AddressofScannerService</wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/GetScannerElements
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetScannerElementsRequest>
      <wscn:RequestedElements>
        <wscn:Name>wscn:ScannerStatus</wscn:Name>
      </wscn:RequestedElements>
    </wscn:GetScannerElementsRequest>
  </soap:Body>
</soap:Envelope>
```

In the following code example, a client specifies two QName values. The first QName is wscn:ScannerConfiguration, and the second QName is invalid.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  xmlns:ihv="https://www.example.com/extension"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>AddressofScannerService</wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/GetScannerElements
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetScannerElementsRequest>
      <wscn:RequestedElements>
        <wscn:Name>wscn:ScannerConfiguration</wscn:Name>
        <wscn:Name>ihv:InvalidRequestEntry</wscn:Name>
      </wscn:RequestedElements>
    </wscn:GetScannerElementsRequest>
  </soap:Body>
</soap:Envelope>
```

## See also

[**GetScannerElementsResponse**](getscannerelementsresponse.md)

[**RequestedElements**](requestedelements.md)
