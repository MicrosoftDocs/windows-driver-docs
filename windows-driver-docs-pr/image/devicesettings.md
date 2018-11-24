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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DeviceSettings element


The required **DeviceSettings** element describes the basic capabilities of the scan device.

Usage
-----

```xml
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
<td><p><a href="autoexposuresupported.md" data-raw-source="[&lt;strong&gt;AutoExposureSupported&lt;/strong&gt;](autoexposuresupported.md)"><strong>AutoExposureSupported</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="brightnesssupported.md" data-raw-source="[&lt;strong&gt;BrightnessSupported&lt;/strong&gt;](brightnesssupported.md)"><strong>BrightnessSupported</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="compressionqualityfactorsupported.md" data-raw-source="[&lt;strong&gt;CompressionQualityFactorSupported&lt;/strong&gt;](compressionqualityfactorsupported.md)"><strong>CompressionQualityFactorSupported</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="contenttypessupported.md" data-raw-source="[&lt;strong&gt;ContentTypesSupported&lt;/strong&gt;](contenttypessupported.md)"><strong>ContentTypesSupported</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="contrastsupported.md" data-raw-source="[&lt;strong&gt;ContrastSupported&lt;/strong&gt;](contrastsupported.md)"><strong>ContrastSupported</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="documentsizeautodetectsupported.md" data-raw-source="[&lt;strong&gt;DocumentSizeAutoDetectSupported&lt;/strong&gt;](documentsizeautodetectsupported.md)"><strong>DocumentSizeAutoDetectSupported</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="formatssupported.md" data-raw-source="[&lt;strong&gt;FormatsSupported&lt;/strong&gt;](formatssupported.md)"><strong>FormatsSupported</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="rotationssupported.md" data-raw-source="[&lt;strong&gt;RotationsSupported&lt;/strong&gt;](rotationssupported.md)"><strong>RotationsSupported</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scalingrangesupported.md" data-raw-source="[&lt;strong&gt;ScalingRangeSupported&lt;/strong&gt;](scalingrangesupported.md)"><strong>ScalingRangeSupported</strong></a></p></td>
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
<td><p><a href="scannerconfiguration.md" data-raw-source="[&lt;strong&gt;ScannerConfiguration&lt;/strong&gt;](scannerconfiguration.md)"><strong>ScannerConfiguration</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DeviceSettings** element contains the supported values for many of the imaging options that can be set in a [**ScanTicket**](scanticket.md) element for a scan operation. A client can use the values that are returned in **DeviceSettings** to create valid **ScanTicket** elements.

## See also


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

 

 






