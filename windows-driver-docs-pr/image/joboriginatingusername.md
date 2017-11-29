---
title: JobOriginatingUserName element
description: The required JobOriginatingUserName element specifies the name of the user who submitted the scan job.
ms.assetid: ba2dd472-1ac0-40bd-816c-02abc093b6ed
keywords: ["JobOriginatingUserName element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobOriginatingUserName
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobOriginatingUserName element


The required **JobOriginatingUserName** element specifies the name of the user who submitted the scan job.

Usage
-----

``` syntax
<wscn:JobOriginatingUserName>
  text
</wscn:JobOriginatingUserName>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid character string.

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
<td><p>[<strong>JobDescription</strong>](jobdescription.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobEndState</strong>](jobendstate.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobSummary</strong>](jobsummary.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client or the security infrastructure, if any, provides the **JobOriginatingUserName** element. A client should supply a value to help users easily distinguish between the jobs that they submitted and jobs that other users submitted.

The WSD Scan Service can provide a default **JobOriginatingUserName** name in its [**DefaultScanTicket**](defaultscanticket.md) element. You can set this name in an implementation-specific manner.

The name of the job is specified in the [**JobName**](jobname.md) element.

## <span id="see_also"></span>See also


[**DefaultScanTicket**](defaultscanticket.md)

[**JobDescription**](jobdescription.md)

[**JobEndState**](jobendstate.md)

[**JobName**](jobname.md)

[**JobSummary**](jobsummary.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobOriginatingUserName%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





