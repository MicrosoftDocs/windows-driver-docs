---
title: Platen element
description: The optional Platen element describes the capabilities of the flatbed platen that is available on the scanner.
ms.assetid: bda5aa6d-ac19-4af2-9b21-64b29d726e80
keywords: ["Platen element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Platen
api_type:
- Schema
---

# Platen element


The optional **Platen** element describes the capabilities of the flatbed platen that is available on the scanner.

Usage
-----

``` syntax
<wscn:Platen>
  child elements
</wscn:Platen>
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
<td><p>[<strong>PlatenColor</strong>](platencolor.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>PlatenMaximumSize</strong>](platenmaximumsize.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PlatenMinimumSize</strong>](platenminimumsize.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>PlatenOpticalResolution</strong>](platenopticalresolution.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PlatenResolutions</strong>](platenresolutions.md)</p></td>
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
<td><p>[<strong>ScannerConfiguration</strong>](scannerconfiguration.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the scan device has a flatbed platen, the WSD Scan Service must provide configuration information for all **Platen** child elements.

## <span id="see_also"></span>See also


[**PlatenColor**](platencolor.md)

[**PlatenMaximumSize**](platenmaximumsize.md)

[**PlatenMinimumSize**](platenminimumsize.md)

[**PlatenOpticalResolution**](platenopticalresolution.md)

[**PlatenResolutions**](platenresolutions.md)

[**ScannerConfiguration**](scannerconfiguration.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Platen%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





