---
title: JobEndState element
description: The required JobEndState element describes the final state of the current scan job.
MS-HAID:
- 'wsdss\_events\_69cb54df-611c-4544-92a0-fd7d7c004f98.xml'
- 'image.jobendstate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c69b5988-ca0d-441f-9b65-e5692a17ccb3
keywords: ["JobEndState element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobEndState
api_type:
- Schema
---

# JobEndState element


The required **JobEndState** element describes the final state of the current scan job.

Usage
-----

``` syntax
<wscn:JobEndState>
  child elements
</wscn:JobEndState>
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
<td><p>[<strong>JobCompletedState</strong>](jobcompletedstate.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobCompletedStateReasons</strong>](jobcompletedstatereasons.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobCompletedTime</strong>](jobcompletedtime.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobName</strong>](jobname.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobOriginatingUserName</strong>](joboriginatingusername.md)</p></td>
</tr>
<tr class="odd">
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
<td><p>[<strong>JobEndStateEvent</strong>](jobendstateevent.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobEndState** element contains child elements that describe various aspects about the end state of a scan job. The WSD Scan Service sends a **JobEndState** element to a client through the [**JobEndStateEvent**](jobendstateevent.md) element.

## <span id="see_also"></span>See also


[**JobCompletedState**](jobcompletedstate.md)

[**JobCompletedStateReasons**](jobcompletedstatereasons.md)

[**JobCompletedTime**](jobcompletedtime.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobId**](jobid.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**ScansCompleted**](scanscompleted.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobEndState%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





