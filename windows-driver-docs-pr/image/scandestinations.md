---
title: ScanDestinations element
description: The required ScanDestinations element is a collection of all of the scan destinations that a client wants to register with the scan device.
ms.assetid: 50f87269-4d95-4653-ba93-aa752bdc9168
keywords: ["ScanDestinations element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanDestinations
api_type:
- Schema
---

# ScanDestinations element


The required **ScanDestinations** element is a collection of all of the scan destinations that a client wants to register with the scan device.

Usage
-----

``` syntax
<wscn:ScanDestinations>
  child elements
</wscn:ScanDestinations>
```

Attributes
----------

There are no attributes.

Text value
----------

None

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
<td><p>[<strong>ScanDestination</strong>](scandestination.md)</p></td>
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
<td><p>&lt;wse:Subscribe&gt;</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client must send the **ScanDestinations** element in the **&lt;wse:Subscribe&gt;** request operation element to register one or more scan destinations with the WSD Scan Service. The client subscribes during client setup before obtaining scan ticket information from the WSD Scan Service. The **&lt;wse:Subscribe&gt;** element is defined in the specification.

The **ScanDestinations** element give clients the flexibility to register for multiple unique scan destinations at once.

## <span id="see_also"></span>See also


[**ScanDestination**](scandestination.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScanDestinations%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





