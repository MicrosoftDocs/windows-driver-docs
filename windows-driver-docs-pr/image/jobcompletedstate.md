---
title: JobCompletedState element
description: The required JobCompletedState element specifies a job's final job state.
ms.assetid: 41dc029b-2315-465a-8490-1f4e50db0188
keywords: ["JobCompletedState element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCompletedState
api_type:
- Schema
---

# JobCompletedState element


The required **JobCompletedState** element specifies a job's final job state.

Usage
-----

``` syntax
<wscn:JobCompletedState>
  text
</wscn:JobCompletedState>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values from the [**JobState**](jobstate.md) element:

-   Aborted
-   Canceled
-   Completed
-   Terminating

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
</tbody>
</table>

Remarks
-------

The WSD Scan Service sends a **JobCompletedState** element to the client within the [**JobEndStateEvent**](jobendstateevent.md) event element.

## <span id="see_also"></span>See also


[**JobEndState**](jobendstate.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobState**](jobstate.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobCompletedState%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





