---
title: ScanRegion element
description: The optional ScanRegion element specifies the area to scan within the input document boundaries.
ms.assetid: 29b94df7-503d-4bbd-99a8-9092140c6629
keywords: ["ScanRegion element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanRegion
api_type:
- Schema
---

# ScanRegion element


The optional **ScanRegion** element specifies the area to scan within the input document boundaries.

Usage
-----

``` syntax
<wscn:ScanRegion>
  child elements
</wscn:ScanRegion>
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
<td><p>[<strong>ScanRegionHeight</strong>](scanregionheight.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanRegionWidth</strong>](scanregionwidth.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScanRegionXOffset</strong>](scanregionxoffset.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanRegionYOffset</strong>](scanregionyoffset.md)</p></td>
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
<td><p>[<strong>MediaBack</strong>](mediaback.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>MediaFront</strong>](mediafront.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

All **ScanRegion** values represent one-thousandths (1/1000) of an inch.

If the requested scan region of a scan job would fall completely outside the supported acquisition area of the scan device, the scan operation should be rejected.

[**ScanRegionXOffset**](scanregionxoffset.md) + [**ScanRegionWidth**](scanregionwidth.md) must be equal or less than the [**InputSize**](inputsize.md) width.

[**ScanRegionYOffset**](scanregionyoffset.md) + [**ScanRegionHeight**](scanregionheight.md) must be equal or less than the **InputSize** height.

The WSD Scan Service can adjust a requested scan region if it cannot fulfill the specified dimensions. Any changes to the scan region should be reported in the [**DocumentFinalParameters**](documentfinalparameters.md) elements in the scan job.

## <span id="see_also"></span>See also


[**DocumentFinalParameters**](documentfinalparameters.md)

[**InputSize**](inputsize.md)

[**MediaBack**](mediaback.md)

[**MediaFront**](mediafront.md)

[**ScanRegionHeight**](scanregionheight.md)

[**ScanRegionWidth**](scanregionwidth.md)

[**ScanRegionXOffset**](scanregionxoffset.md)

[**ScanRegionYOffset**](scanregionyoffset.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScanRegion%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





