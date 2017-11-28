---
title: KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH
description: The KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH property retrieves focal length information for a camera.
ms.assetid: a7fba5e4-abd1-46ae-b93c-5fede0249771
keywords: ["KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH


The KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH property retrieves focal length information for a camera.

## <span id="ddk_ksproperty_cameracontrol_focal_length_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_KS"></span>


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
<td><p>No</p></td>
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564408) or [<strong>KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564418)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's focal length.

Remarks
-------

You can use this property request to interpret zoom values. The range of zoom should be between **lObjectiveFocalLengthMin**/**lOcularFocalLength** and **lObjectiveFocalLengthMax**/**lOcularFocalLength**. (**lOcularFocalLength**, **lObjectiveFocalLengthMin**, and **lObjectiveFocalLengthMax** are members of the [**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564408) and [**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564418) structures.)

For example, if **lObjectiveFocalLengthMax** = 105 and **lOcularFocalLength** = 35, then this camera is capable of a maximum optical zoom ratio of 105/35, or 3.

Also see the *Optical Zoom* section of the USB Video Class Device Class specification. This specification is available at the [USB Implementers Forum](http://go.microsoft.com/fwlink/p/?linkid=8780) website.

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


[**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564408)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564418)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM**](ksproperty-cameracontrol-zoom.md)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM\_RELATIVE**](ksproperty-cameracontrol-zoom-relative.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





