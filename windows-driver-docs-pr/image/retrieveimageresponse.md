---
title: RetrieveImageResponse element
description: The required RetrieveImageResponse operation element returns the scan data to the client.
ms.assetid: f63398c4-bbae-42ca-94c5-059b066c65cb
keywords: ["RetrieveImageResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn RetrieveImageResponse
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# RetrieveImageResponse element


The required **RetrieveImageResponse** operation element returns the scan data to the client.

Usage
-----

```xml
<wscn:RetrieveImageResponse>
  child elements
</wscn:RetrieveImageResponse>
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
<td><p><a href="scandata.md" data-raw-source="[&lt;strong&gt;ScanData&lt;/strong&gt;](scandata.md)"><strong>ScanData</strong></a></p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **RetrieveImageResponse** operation element. The Scan Service sends this element when a client successful sends a [**RetrieveImageRequest**](retrieveimagerequest.md) element.

The Scan Service returns the scan data as a binary attachment with the **RetrieveImageResponse** packet. The response must be packaged as a MIME Multipart-Related content type and make use of the SOAP Message Transmission Optimization Mechanism \[MTOM\] to efficiently send the binary image data.

The number of images that the Scan Service returns in the resultant file depends on the combination of the [**ImagesToTransfer**](imagestotransfer.md) element of the [**ScanTicket**](scanticket.md) and the image file [**Format**](format.md) element as follows:

-   If **Format** specifies a single image format, the returned file will always contain a single image.
-   If **Format** specifies a multi-page format, the returned file will contain as many images as the input source can scan up to the value of **ImagesToTransfer**.

If [**Format**](format.md) specifies a single image format and the value of [**ImagesToTransfer**](imagestotransfer.md) is 0 or greater than 1, the client will send repeated [**RetrieveImageRequest**](retrieveimagerequest.md) operation elements until the Scan Service replies with a **ClientErrorNoImagesAvailable** fault or until the **ImagesToTransfer** value is met.

The Scan Service should abort the job with a [**JobStateReason**](jobstatereason.md) of **ImageTransferError** if there is a communication error during the transfer of the image data.

Examples
--------

The following code example shows how the WSD Scan Service sends image data to the client.

```xml
mime-version: 1.0
Content-Type: multipart/related;
    type=application/xop+xml;
    boundary=4aa7d814-adc1-47a2-8e1c-07585b9892a4;
    start="<14629f74-2047-436c-8046-5cac76d280fc@uuid>";
    startinfo=application/soap+xml


--4aa7d814-adc1-47a2-8e1c-07585b9892a4
Content-Type: application/xop+xml; type="application/soap+xml"
                                   charset=UTF-8
Content-Transfer-Encoding: binary
Content-ID: <14629f74-2047-436c-8046-5cac76d280fc@uuid>

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:xop="http://www.w3.org/2003/12/xop/include"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='http://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>http://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/RetrieveImage
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheRetrieveImageRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:RetrieveImageResponse>
      <wscn:ScanData>
        <xop:Include href="cid:1c696bd7-005a-48d9-9ee9-9adca11f8892@uuid" />
      </wscn:ScanData>
    </wscn:RetrieveImageResponse>
  </soap:Body>
</soap:Envelope>

--4aa7d814-adc1-47a2-8e1c-07585b9892a4

Content-Type: image/jpeg;
Content-Transfer-Encoding: binary
Content-ID: <1c696bd7-005a-48d9-9ee9-9adca11f8892@uuid >

Binary Scan Data
--4aa7d814-adc1-47a2-8e1c-07585b9892a4--
```

## See also

[**Format**](format.md)

[**ImagesToTransfer**](imagestotransfer.md)

[**JobStateReason**](jobstatereason.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

[**ScanData**](scandata.md)

[**ScanTicket**](scanticket.md)
