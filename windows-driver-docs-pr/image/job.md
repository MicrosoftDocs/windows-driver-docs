---
title: Job element
description: The required Job element contains all elements that are associated with a scan job.
ms.assetid: c5622ea6-c57a-4c80-a6ef-e6b9014b2b59
keywords: ["Job element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Job
api_type:
- Schema
---

# Job element


The required **Job** element contains all elements that are associated with a scan job.

Usage
-----

``` syntax
<wscn:Job>
  child elements
</wscn:Job>
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
<td><p>[<strong>Documents</strong>](documents.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScanTicket</strong>](scanticket.md)</p></td>
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
<td><p>[<strong>ActiveJobs</strong>](activejobs.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A scan job (which the **Job** element represents) can contain one or more documents. The WSD Scan Service's processing instructions for both a job and its documents are executed at the **Job** level.

## <span id="see_also"></span>See also


[**ActiveJobs**](activejobs.md)

[**Documents**](documents.md)

[**JobStatus**](jobstatus.md)

[**ScanTicket**](scanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Job%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





