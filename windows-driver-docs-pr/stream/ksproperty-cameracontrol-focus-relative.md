---
title: KSPROPERTY\_CAMERACONTROL\_FOCUS\_RELATIVE
description: The KSPROPERTY\_CAMERACONTROL\_FOCUS\_RELATIVE property specifies the focus setting of the camera.
MS-HAID:
- 'vidcapprop\_6fab42f5-45ef-4fd3-9602-947f1a75db45.xml'
- 'stream.ksproperty\_cameracontrol\_focus\_relative'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8282c703-5ff7-437e-87f9-e05f504d6f2c
keywords: ["KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_FOCUS\_RELATIVE


The KSPROPERTY\_CAMERACONTROL\_FOCUS\_RELATIVE property specifies the focus setting of the camera.

## <span id="ddk_ksproperty_cameracontrol_focus_relative_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE_KS"></span>


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

 

The property value (operation data) is a LONG that specifies a camera's relative focus setting. The size of the value represents the speed at which the focal point changes; a higher value represents a higher speed.

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
<td><p>Stop focus motion.</p></td>
</tr>
<tr class="even">
<td><p>Positive value</p></td>
<td><p>Start moving the focus closer to the object.</p></td>
</tr>
<tr class="odd">
<td><p>Negative value</p></td>
<td><p>Start moving the focus farther away from the object.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When making a set request, provide one of the values in the preceding table in the **Value** member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure.

When making a get request, the client receives one of the values in the preceding table in the **Value** member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure. The value indicates the current focus setting for the camera.

Note that a particular device might support only a certain speed range. To determine the range of speeds supported by the device, an application can issue a KSPROPERTY\_TYPE\_BASICSUPPORT request. You can specify KSPROPERTY\_TYPE\_BASICSUPPORT in the **Flags** member of the [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176) structure.

Some devices support only a single focus speed. In this case, the sign of the **Value** member simply indicates whether the lens should shorten its focus or lengthen it.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





