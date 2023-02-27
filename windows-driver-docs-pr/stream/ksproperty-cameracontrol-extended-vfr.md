---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR is a property ID that will be used to specify whether variable frame rate is desired on the driver.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_VFR Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_VFR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR

KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VFR is a property ID that will be used to specify whether variable frame rate is desired on the driver. This is a pin level control for video pin only. For preview and photo, the frame rate variability is entirely up to the driver and is not controllable by the client.

## Usage summary table

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

```cpp
#define KSCAMERA_EXTENDEDPROP_VFR_OFF   0x0000000000000000  
#define KSCAMERA_EXTENDEDPROP_VFR_ON    0x0000000000000001
```
If set to VFR\_OFF, driver shall deliver fixed frame rate for the video pin.

If set to VFR\_ON, the frame rate is automatically determined by the driver and can vary based on the capture condition and scenario for the video pin. When VFR\_ON is set, the maximum frame rate allowed is further determined by the fixed frame rate embedded in the media type selected for video recording.

If the driver does not support variable frame rate for video, the driver should not implement this control, and variable frame rate will be implied.

This control has no effect during the video recording for the driver that doesn’t support on the fly toggling of the VFR settings. The driver shall ignore the control received during an active video recording in that case.

This is a synchronous control and not cancelable. There are no capabilities defined for this control.

The following table contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

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

## Requirements

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
