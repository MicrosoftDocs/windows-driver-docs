---
title: DeviceSettings element
description: The required DeviceSettings element describes the basic capabilities of the scan device.
ms.assetid: d12d25f0-fa94-4840-bb1a-cc1a5352767c
keywords: ["DeviceSettings element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DeviceSettings
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DeviceSettings element


The required **DeviceSettings** element describes the basic capabilities of the scan device.

Usage
-----

``` syntax
<wscn:DeviceSettings>
  child elements
</wscn:DeviceSettings>
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
<td><p>[<strong>AutoExposureSupported</strong>](autoexposuresupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>BrightnessSupported</strong>](brightnesssupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CompressionQualityFactorSupported</strong>](compressionqualityfactorsupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ContentTypesSupported</strong>](contenttypessupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ContrastSupported</strong>](contrastsupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DocumentSizeAutoDetectSupported</strong>](documentsizeautodetectsupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>FormatsSupported</strong>](formatssupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>RotationsSupported</strong>](rotationssupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScalingRangeSupported</strong>](scalingrangesupported.md)</p></td>
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

The **DeviceSettings** element contains the supported values for many of the imaging options that can be set in a [**ScanTicket**](scanticket.md) element for a scan operation. A client can use the values that are returned in **DeviceSettings** to create valid **ScanTicket** elements.

## <span id="see_also"></span>See also


[**AutoExposureSupported**](autoexposuresupported.md)

[**BrightnessSupported**](brightnesssupported.md)

[**CompressionQualityFactorSupported**](compressionqualityfactorsupported.md)

[**ContentTypesSupported**](contenttypessupported.md)

[**ContrastSupported**](contrastsupported.md)

[**DocumentSizeAutoDetectSupported**](documentsizeautodetectsupported.md)

[**FormatsSupported**](formatssupported.md)

[**RotationsSupported**](rotationssupported.md)

[**ScalingRangeSupported**](scalingrangesupported.md)

[**ScanTicket**](scanticket.md)

[**ScannerConfiguration**](scannerconfiguration.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DeviceSettings%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





