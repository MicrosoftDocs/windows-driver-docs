---
title: JobSummary element
description: The optional JobSummary element contains a summary about a scan job.
MS-HAID:
- 'wsdss\_ops\_709e8e7b-6031-42d9-85bf-9cb20d6e9a7b.xml'
- 'image.jobsummary'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: db81cad5-d157-403c-b3a4-1e5f91f858da
keywords: ["JobSummary element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobSummary
api_type:
- Schema
---

# JobSummary element


The optional **JobSummary** element contains a summary about a scan job.

Usage
-----

``` syntax
<wscn:JobSummary>
  child elements
</wscn:JobSummary>
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
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobName</strong>](jobname.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobOriginatingUserName</strong>](joboriginatingusername.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobState</strong>](jobstate.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobStateReasons</strong>](jobstatereasons.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScansCompleted</strong>](scanscompleted.md)</p></td>
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
<tr class="even">
<td><p>[<strong>JobHistory</strong>](jobhistory.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the parent element of the **JobSummary** element is [**ActiveJobs**](activejobs.md), **JobSummary** contains a summary of information about one job that is currently active within the scan device.

If the parent element is [**JobHistory**](jobhistory.md), **JobSummary** contains a summary of information about a single, recently completed job within the scan device.

## <span id="see_also"></span>See also


[**ActiveJobs**](activejobs.md)

[**JobHistory**](jobhistory.md)

[**JobId**](jobid.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**JobState**](jobstate.md)

[**JobStateReasons**](jobstatereasons.md)

[**ScansCompleted**](scanscompleted.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobSummary%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





