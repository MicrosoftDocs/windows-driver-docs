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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScanTicket element


The required **ScanTicket** element defines all of the description and processing parameters of the currently identified scan job.

Usage
-----

```xml
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
<td><p><a href="documentparameters.md" data-raw-source="[&lt;strong&gt;DocumentParameters&lt;/strong&gt;](documentparameters.md)"><strong>DocumentParameters</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobdescription.md" data-raw-source="[&lt;strong&gt;JobDescription&lt;/strong&gt;](jobdescription.md)"><strong>JobDescription</strong></a></p></td>
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
<td><p><a href="createscanjobrequest.md" data-raw-source="[&lt;strong&gt;CreateScanJobRequest&lt;/strong&gt;](createscanjobrequest.md)"><strong>CreateScanJobRequest</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="job.md" data-raw-source="[&lt;strong&gt;Job&lt;/strong&gt;](job.md)"><strong>Job</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="validatescanticketrequest.md" data-raw-source="[&lt;strong&gt;ValidateScanTicketRequest&lt;/strong&gt;](validatescanticketrequest.md)"><strong>ValidateScanTicketRequest</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScanTicket** element contains the values for the scanner settings for the current job that the client selected. The client constructs the **ScanTicket** by using only those values that the scanner supports. The client obtains such values by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation and asking for the scanner's [**DefaultScanTicket**](defaultscanticket.md) element.

The member elements of **ScanTicket** map directly to an instance of a [**Job**](job.md) element, and they are exactly what the client needs to send to the scanner during a [**CreateScanJobRequest**](createscanjobrequest.md) operation.

The client can request the **ScanTicket** element for a particular job by calling.

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DefaultScanTicket**](defaultscanticket.md)

[**DocumentParameters**](documentparameters.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Job**](job.md)

[**JobDescription**](jobdescription.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

 

 






