---
title: KSPROPERTY\_CAMERACONTROL\_EXPOSURE\_RELATIVE
description: The KSPROPERTY\_CAMERACONTROL\_EXPOSURE\_RELATIVE property specifies the electronic shutter speed.
ms.assetid: a4003fcd-9dc8-4889-9ce0-e4f09273d152
keywords: ["KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXPOSURE\_RELATIVE


The KSPROPERTY\_CAMERACONTROL\_EXPOSURE\_RELATIVE property specifies the electronic shutter speed.

## <span id="ddk_ksproperty_cameracontrol_exposure_relative_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564439" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564439)"><strong>KSPROPERTY_CAMERACONTROL_S</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564420" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_NODE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564420)"><strong>KSPROPERTY_CAMERACONTROL_NODE_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's relative exposure setting. Step size is hardware-dependent. To determine the step size, you can make a get request on the [**KSPROPERTY\_CAMERACONTROL\_EXPOSURE**](ksproperty-cameracontrol-exposure.md) property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>Set the exposure time to the implementation-specific default value.</p></td>
</tr>
<tr class="even">
<td><p>Positive value</p></td>
<td><p>Increment the exposure time by one step.</p></td>
</tr>
<tr class="odd">
<td><p>Negative value</p></td>
<td><p>Decrement the exposure time by one step.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When making a set request, you should provide one of the values in the preceding table in the **Value** member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure.

When making a get request, the client receives one of the values in the preceding table in the Value member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure. The value indicates the current exposure time setting for the camera.

Set requests will fail if the Auto-Exposure mode control is in Auto mode or Aperture Priority mode.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available for Windows Vista and later versions of the Windows operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420)

 

 






