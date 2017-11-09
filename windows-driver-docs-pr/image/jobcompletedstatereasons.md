---
title: JobCompletedStateReasons element
description: The required JobCompletedStateReasons element is a collection of all additional information about how and why a scan job completed.
MS-HAID:
- 'wsdss\_events\_fca889e9-8c74-4f8d-a6ac-9bff915dde29.xml'
- 'image.jobcompletedstatereasons'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 678384b4-a023-4c79-a68a-4a2cc3a04a0e
keywords: ["JobCompletedStateReasons element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCompletedStateReasons
api_type:
- Schema
---

# JobCompletedStateReasons element


The required **JobCompletedStateReasons** element is a collection of all additional information about how and why a scan job completed.

Usage
-----

``` syntax
<wscn:JobCompletedStateReasons>
  child elements
</wscn:JobCompletedStateReasons>
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
<td><p>[<strong>JobStateReason</strong>](jobstatereason.md)</p></td>
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
<td><p>[<strong>JobEndState</strong>](jobendstate.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobCompletedStateReasons** element contains zero or more [**JobStateReason**](jobstatereason.md) elements, each of which contains a reason for how or why the scan job completed. The WSD Scan Service sends the **JobCompletedStateReasons** element to the client through the [**JobEndStateEvent**](jobendstateevent.md) event element.

## <span id="see_also"></span>See also


[**JobEndState**](jobendstate.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobStateReason**](jobstatereason.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobCompletedStateReasons%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





