---
title: JobHistory element
description: The optional JobHistory element contains information about scan jobs that have recently completed processing.
ms.assetid: 7f46044e-ac34-4181-9a35-62dea5ec8c82
keywords: ["JobHistory element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobHistory
api_type:
- Schema
---

# JobHistory element


The optional **JobHistory** element contains information about scan jobs that have recently completed processing.

Usage
-----

``` syntax
<wscn:JobHistory>
  child elements
</wscn:JobHistory>
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
<td><p>[<strong>Job</strong>](job.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobSummary</strong>](jobsummary.md)</p></td>
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
<td><p>[<strong>GetJobHistoryResponse</strong>](getjobhistoryresponse.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobTable</strong>](jobtable.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobHistory** element contains a subset of the most recent jobs that have finished processing. These jobs could have scanned, been aborted, or failed for other reasons. The maximum number of jobs in this list depends on the device.

A client can ask for job history through the [**GetJobHistoryRequest**](getjobhistoryrequest.md) operation element. The WSD Scan Service returns this history in a [**GetJobHistoryResponse**](getjobhistoryresponse.md) operation element.

## <span id="see_also"></span>See also


[**GetJobHistoryRequest**](getjobhistoryrequest.md)

[**GetJobHistoryResponse**](getjobhistoryresponse.md)

[**Job**](job.md)

[**JobSummary**](jobsummary.md)

[**JobTable**](jobtable.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobHistory%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





