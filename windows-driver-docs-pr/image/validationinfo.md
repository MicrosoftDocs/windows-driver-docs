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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 






