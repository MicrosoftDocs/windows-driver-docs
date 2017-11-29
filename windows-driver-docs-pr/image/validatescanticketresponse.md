---
title: ValidateScanTicketResponse element
description: The required ValidateScanTicketResponse operation notifies the client whether a client's submitted ScanTicket is valid.
ms.assetid: 7eea7d33-45de-45bf-8e89-de06f5710073
keywords: ["ValidateScanTicketResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ValidateScanTicketResponse
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ValidateScanTicketResponse element


The required **ValidateScanTicketResponse** operation notifies the client whether a client's submitted [**ScanTicket**](scanticket.md) is valid.

Usage
-----

``` syntax
<wscn:ValidateScanTicketResponse>
  child elements
</wscn:ValidateScanTicketResponse>
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
<td><p>[<strong>ValidationInfo</strong>](validationinfo.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The client submits the [**ScanTicket**](scanticket.md) element to be checked in the [**ValidateScanTicketRequest**](validatescanticketrequest.md) operation. The WSD Scan Service must respond with a **ValidateScanTicketResponse** element that contains all validation information after successfully processing **ValidateScanTicketRequest**.

Examples
--------

The following code example shows a response to a client when it has submitted a valid scan ticket.

```
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:xop="http://www.w3.org/2003/12/xop/include"
  xmlns:xop-mime="http://www.w3.org/2003/12/xop/mime"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle=&#39;http://www.w3.org/2002/12/soap-encoding&#39; >

  <soap:Header>
    <wsa:To>
      http://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/ValidateScanTicket
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

```
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:xop="http://www.w3.org/2003/12/xop/include"
  xmlns:xop-mime="http://www.w3.org/2003/12/xop/mime"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle=&#39;http://www.w3.org/2002/12/soap-encoding&#39; >

  <soap:Header>
    <wsa:To>
      http://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/ValidateScanTicket
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

## <span id="see_also"></span>See also


[**ScanTicket**](scanticket.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidationInfo**](validationinfo.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ValidateScanTicketResponse%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





