---
title: ScanTicket element
description: The required ScanTicket element defines all of the description and processing parameters of the currently identified scan job.
ms.assetid: d507bd46-8fc4-49d3-9575-2d83fd7ae625
keywords: ["ScanTicket element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanTicket
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ScanTicket element


The required **ScanTicket** element defines all of the description and processing parameters of the currently identified scan job.

Usage
-----

``` syntax
<wscn:ScanTicket>
  child elements
</wscn:ScanTicket>
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
<td><p>[<strong>DocumentParameters</strong>](documentparameters.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobDescription</strong>](jobdescription.md)</p></td>
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
<td><p>[<strong>CreateScanJobRequest</strong>](createscanjobrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Job</strong>](job.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ValidateScanTicketRequest</strong>](validatescanticketrequest.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScanTicket** element contains the values for the scanner settings for the current job that the client selected. The client constructs the **ScanTicket** by using only those values that the scanner supports. The client obtains such values by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation and asking for the scanner's [**DefaultScanTicket**](defaultscanticket.md) element.

The member elements of **ScanTicket** map directly to an instance of a [**Job**](job.md) element, and they are exactly what the client needs to send to the scanner during a [**CreateScanJobRequest**](createscanjobrequest.md) operation.

The client can request the **ScanTicket** element for a particular job by calling.

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DefaultScanTicket**](defaultscanticket.md)

[**DocumentParameters**](documentparameters.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Job**](job.md)

[**JobDescription**](jobdescription.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScanTicket%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





