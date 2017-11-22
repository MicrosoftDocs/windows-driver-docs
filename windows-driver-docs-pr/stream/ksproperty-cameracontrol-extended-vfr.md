---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR is a property ID that will be used to specify whether variable frame rate is desired on the driver.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9B528421-B5AA-4092-9F7B-71A18732ABA8
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_VFR Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_VFR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR


KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR is a property ID that will be used to specify whether variable frame rate is desired on the driver. This is a pin level control for video pin only. For preview and photo, the frame rate variability is entirely up to the driver and is not controllable by the client.

## <span id="Usage_summary_table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage summary table


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Scope</th>
<th>Control</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version 1</p></td>
<td><p>Pin</p></td>
<td><p>Synchronous</p></td>
</tr>
</tbody>
</table>

 

The following flags can be placed in the **KSCAMERA\_EXTENDEDPROP\_HEADER.Flags** field, which are used to turn on and off variable frame rate for video. The default is up to the driver.

``` syntax
#define KSCAMERA_EXTENDEDPROP_VFR_OFF               0x0000000000000000  
#define KSCAMERA_EXTENDEDPROP_VFR_ON                0x0000000000000001
```

If set to VFR\_OFF, driver shall deliver fixed frame rate for the video pin.

If set to VFR\_ON, the frame rate is automatically determined by the driver and can vary based on the capture condition and scenario for the video pin. When VFR\_ON is set, the maximum frame rate allowed is further determined by the fixed frame rate embedded in the media type selected for video recording.

If the driver does not support variable frame rate for video, the driver should not implement this control, and fixed frame rate will be implied.

This control has no effect during the video recording for the driver that doesn’t support on the fly toggling of the VFR settings. The driver shall ignore the control received during an active video recording in that case.

This is a synchronous control. There are no capabilities defined for this control.

The following table contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure fields when using the control.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>This must be 1.</p></td>
</tr>
<tr class="even">
<td><p>PinId</p></td>
<td><p>This must be the Pin ID associated with the video pin.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER)+ sizeof(KSCAMERA_EXTENDEDPROP_VALUE).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the flags defined above.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_VFR%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




