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
---

# RetrieveImageResponse element


The required **RetrieveImageResponse** operation element returns the scan data to the client.

Usage
-----

``` syntax
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
<td><p>[<strong>ScanData</strong>](scandata.md)</p></td>
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

```
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
  soap:encodingStyle=&#39;http://www.w3.org/2002/12/soap-encoding&#39; >

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

## <span id="see_also"></span>See also


[**Format**](format.md)

[**ImagesToTransfer**](imagestotransfer.md)

[**JobStateReason**](jobstatereason.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

[**ScanData**](scandata.md)

[**ScanTicket**](scanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20RetrieveImageResponse%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





