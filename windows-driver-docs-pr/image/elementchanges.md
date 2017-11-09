---
title: ElementChanges element
description: The required ElementChanges element contains the changes to the ScannerDescription, ScannerConfiguration, DefaultScanTicket, and vendor-extended elements.
MS-HAID:
- 'wsdss\_events\_d1273f76-8174-4c74-aeae-fb6305132aa6.xml'
- 'image.elementchanges'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d6f1d188-beb6-4ea3-a362-de64d8d8dacb
keywords: ["ElementChanges element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ElementChanges
api_type:
- Schema
---

# ElementChanges element


The required **ElementChanges** element contains the changes to the [**ScannerDescription**](scannerdescription.md), [**ScannerConfiguration**](scannerconfiguration.md), [**DefaultScanTicket**](defaultscanticket.md), and vendor-extended elements.

Usage
-----

``` syntax
<wscn:ElementChanges>
  child elements
</wscn:ElementChanges>
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
<td><p>[<strong>DefaultScanTicket</strong>](defaultscanticket.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScannerConfiguration</strong>](scannerconfiguration.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScannerDescription</strong>](scannerdescription.md)</p></td>
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
<td><p>[<strong>ScannerElementsChangeEvent</strong>](scannerelementschangeevent.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service must include an **ElementChanges** element when it generates a [**ScannerElementsChangeEvent**](scannerelementschangeevent.md) element. Each child element of **ElementChanges** must contain all of its required child elements. If an optional element is missing from the returned XML, the WSD Scan Service is indicating to the client that the service no longer supports that element.

## <span id="see_also"></span>See also


[**DefaultScanTicket**](defaultscanticket.md)

[**ScannerConfiguration**](scannerconfiguration.md)

[**ScannerDescription**](scannerdescription.md)

[**ScannerElementsChangeEvent**](scannerelementschangeevent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ElementChanges%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





