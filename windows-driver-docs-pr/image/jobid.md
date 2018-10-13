---
title: JobId element
description: The required JobId element uniquely identifies a job within a scanner.
ms.assetid: ae9199c1-c45a-4147-b4f0-f37a9a0f1b22
keywords: ["JobId element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobId
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# JobId element


The required **JobId** element uniquely identifies a job within a scanner.

Usage
-----

```xml
<wscn:JobId>
  text
</wscn:JobId>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value from 1 through 2147483648.

## Child elements


There are no child elements.

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
<td><p>[<strong>CancelJobRequest</strong>](canceljobrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CreateScanJobResponse</strong>](createscanjobresponse.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>GetJobElementsRequest</strong>](getjobelementsrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobEndState</strong>](jobendstate.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobSummary</strong>](jobsummary.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>RetrieveImageRequest</strong>](retrieveimagerequest.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service returns a **JobId** element to a client through a [**CreateScanJobResponse**](createscanjobresponse.md) operation element. The client uses the returned **JobId** when it initiates a scan request through the [**RetrieveImageRequest**](retrieveimagerequest.md) operation element.

**JobId** does not need to be globally unique. The WSD Scan Service should not reuse a recently assigned value so that a client does not confuse a current scan job with an older job.

You cannot extend the allowed values for the **JobId** element.

## See also


[**CancelJobRequest**](canceljobrequest.md)

[**CreateScanJobResponse**](createscanjobresponse.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

 

 






