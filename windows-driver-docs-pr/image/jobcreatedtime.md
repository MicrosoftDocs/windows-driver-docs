---
title: JobCreatedTime element
description: The optional JobCreatedTime element specifies the time at which the job was created.
ms.assetid: 34107c3a-d02a-4b86-be1e-cd91e2887479
keywords: ["JobCreatedTime element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCreatedTime
api_type:
- Schema
---

# JobCreatedTime element


The optional **JobCreatedTime** element specifies the time at which the job was created.

Usage
-----

``` syntax
<wscn:JobCreatedTime>
  text
</wscn:JobCreatedTime>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid value for the dateTime type. For more information about dateTime, see XML Schema Part 2: Datatypes Second Edition.**dateTimedateTime**

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
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A job is *created* when the job is submitted to the system.

The specified time refers to the internal clock of the scan device and does not need to be a real time clock.

## <span id="see_also"></span>See also


[**JobStatus**](jobstatus.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobCreatedTime%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





