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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CAMERACONTROL\_EXPOSURE\_RELATIVE


The KSPROPERTY\_CAMERACONTROL\_EXPOSURE\_RELATIVE property specifies the electronic shutter speed.

## <span id="ddk_ksproperty_cameracontrol_exposure_relative_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564439) or [<strong>KSPROPERTY_CAMERACONTROL_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564420)</p></td>
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

## <span id="see_also"></span>See also


[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





