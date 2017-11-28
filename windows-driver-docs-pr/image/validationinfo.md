---
title: ValidationInfo element
description: The required ValidationInfo element contains all ScanTicket validation information in response to a client's ValidateScanTicketRequest.
ms.assetid: c727cbd7-6da0-4750-b36e-3b65e56015fa
keywords: ["ValidationInfo element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ValidationInfo
api_type:
- Schema
---

# ValidationInfo element


The required **ValidationInfo** element contains all [**ScanTicket**](scanticket.md) validation information in response to a client's [**ValidateScanTicketRequest**](validatescanticketrequest.md).

Usage
-----

``` syntax
<wscn:ValidationInfo>
  child elements
</wscn:ValidationInfo>
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
<td><p>[<strong>ImageInformation</strong>](imageinformation.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ValidScanTicket</strong>](validscanticket.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ValidTicket</strong>](validticket.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


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
<td><p>[<strong>ValidateScanTicketResponse</strong>](validatescanticketresponse.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ValidationInfo** element contains elements that define whether the client's [**ScanTicket**](scanticket.md) is valid and, if not, what data the WSD Scan Service changed to make the ticket valid. The Scan Service returns this information in its [**ValidateScanTicketResponse**](validatescanticketresponse.md) operation.

## <span id="see_also"></span>See also


[**ImageInformation**](imageinformation.md)

[**ScanTicket**](scanticket.md)

[**ValidScanTicket**](validscanticket.md)

[**ValidTicket**](validticket.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidateScanTicketResponse**](validatescanticketresponse.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ValidationInfo%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





