---
title: ValidateScanTicketResponse Element
description: The required ValidateScanTicketResponse operation notifies the client whether a client's submitted ScanTicket is valid.
keywords: ["ValidateScanTicketResponse element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ValidateScanTicketResponse
api_type:
- Schema
ms.date: 05/02/2023
---

# ValidateScanTicketResponse element

The required **ValidateScanTicketResponse** operation notifies the client whether a client's submitted [**ScanTicket**](scanticket.md) is valid.

## Usage

```xml
<wscn:ValidateScanTicketResponse>
  child elements
</wscn:ValidateScanTicketResponse>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ValidationInfo**](validationinfo.md) |

## Parent elements

There are no parent elements.

## Remarks

The client submits the [**ScanTicket**](scanticket.md) element to be checked in the [**ValidateScanTicketRequest**](validatescanticketrequest.md) operation. The WSD Scan Service must respond with a **ValidateScanTicketResponse** element that contains all validation information after successfully processing **ValidateScanTicketRequest**.

## Examples

The following code example shows a response to a client when it has submitted a valid scan ticket.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:xop="https://www.w3.org/2003/12/xop/include"
  xmlns:xop-mime="https://www.w3.org/2003/12/xop/mime"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>
      https://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/ValidateScanTicket
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheValidateScanTicketRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:ValidateScanTicketResponse>
      <wscn:ValidationInfo>
        <wscn:ValidTicket>true</wscn:ScanIdentifierValidTicket>
          <wscn:ImageInformation>
          <wscn:MediaFrontImageInfo>
            <wscn:PixelsPerLine>900</wscn:PixelsPerLine>
            <wscn:NumberOfLines>1500</wscn:NumberOfLines>
            <wscn:BytesPerLine>113</wscn:BytesPerLine>
          </wscn:MediaFrontImageInfo>
        </wscn:ImageInformation>
      </wscn:ValidationInfo>
    </wscn:ValidateScanTicketResponse>
  </soap:Body>
</soap:Envelope>
```

The following code example shows a response to a client when it has submitted an invalid scan ticket.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:xop="https://www.w3.org/2003/12/xop/include"
  xmlns:xop-mime="https://www.w3.org/2003/12/xop/mime"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>
      https://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/ValidateScanTicket
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheValidateScanTicketRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:ValidateScanTicketResponse>
      <wscn:ValidationInfo>
        <wscn:ValidTicket>false</wscn:ValidTicket>
        <wscn:ImageInformation>
          <wscn:MediaFrontImageInfo>
            <wscn:PixelsPerLine>0</wscn:PixelsPerLine>
            <wscn:NumberOfLines>0</wscn:NumberOfLines>
            <wscn:BytesPerLine>0</wscn:BytesPerLine>
          </wscn:MediaFrontImageInfo>
        </wscn:ImageInformation>
        <wscn:ValidScanTicket>
          <wscn:JobDescription>
            <wscn:JobName>Photo Scan</wscn:JobName>
            <wscn:JobOriginatingUserName>RogerSmith</JobOriginatingUserName>
          </wscn:JobDescription>
          <wscn:DocumentParameters>
            <wscn:Format>jfif</wscn:Format>
            <wscn:InputSource>Platen</wscn:InputSource>
            <wscn:ContentType>Auto</wscn:ContentType>
            <wscn:InputSize>
              <wscn:DocumentSizeAutoDetect>true</wscn:DocumentSizeAutoDetect>
            </wscn:InputSize>
            <wscn:Scaling>
              <wscn:ScalingWidth>1000</wscn:ScalingWidth>
              <wscn:ScalingHeight>1000</wscn:ScalingHeight>
            </wscn:Scaling>
            <wscn:MediaSides>
              <wscn:MediaFront>
                <wscn:Resolution>
                  <wscn:Width>300</wscn:Width>
                  <wscn:Height>300</wscn:Height>
                </wscn:Resolution>
              </wscn:MediaFront>
            </wscn:MediaSides>
          </wscn:DocumentParameters>
        </wscn:ValidScanTicket>
      </wscn:ValidationInfo>
    </wscn:ValidateScanTicketResponse>
  </soap:Body>
</soap:Envelope>
```

## See also

[**ScanTicket**](scanticket.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidationInfo**](validationinfo.md)
