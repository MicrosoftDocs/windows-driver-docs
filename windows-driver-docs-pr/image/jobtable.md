---
title: JobTable element
description: The required JobTable element contains current and historical information about scan jobs.
MS-HAID:
- 'wsdss\_job\_68974764-400f-4be3-812e-f484e8344932.xml'
- 'image.jobtable'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 349ca443-5296-4200-884d-91fcdb222be4
keywords: ["JobTable element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobTable
api_type:
- Schema
---

# JobTable element


The required **JobTable** element contains current and historical information about scan jobs.

Usage
-----

``` syntax
<wscn:JobTable>
  child elements
</wscn:JobTable>
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
<td><p>[<strong>ActiveJobs</strong>](activejobs.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobHistory</strong>](jobhistory2.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service uses a **JobTable** element to track all current and finished scan jobs that are submitted to the WSD Scan Service. Current jobs are tracked in the [**ActiveJobs**](activejobs.md) child element; finished jobs are optionally tracked in the [**JobHistory**](jobhistory2.md) child element.

## <span id="see_also"></span>See also


[**ActiveJobs**](activejobs.md)

[**JobHistory**](jobhistory2.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobTable%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





