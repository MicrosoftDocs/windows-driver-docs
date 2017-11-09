---
title: JobCompletedTime element
description: The optional JobCompletedTime element specifies the time at which the scan job was completed.
MS-HAID:
- 'wsdss\_job\_e642f186-6b5f-41d9-9a6f-cfe547b11177.xml'
- 'image.jobcompletedtime'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f29449bd-c618-400f-b37c-3df7d955936b
keywords: ["JobCompletedTime element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCompletedTime
api_type:
- Schema
---

# JobCompletedTime element


The optional **JobCompletedTime** element specifies the time at which the scan job was completed.

Usage
-----

``` syntax
<wscn:JobCompletedTime>
  text
</wscn:JobCompletedTime>
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
<td><p>[<strong>JobEndState</strong>](jobendstate.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A scan job is *complete* when all processing has completed, either because scanning and document transfer completed successfully or because a fatal error was encountered.

The specified time refers to the internal clock of the scan device and does not need to be a real time clock.

## <span id="see_also"></span>See also


[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobCompletedTime%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





