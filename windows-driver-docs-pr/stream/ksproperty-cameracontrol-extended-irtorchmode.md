---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_IRTORCHMODE
description: This extended property control is used by the client to control an IR camera's infrared torch's power level and duty cycle.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_IRTORCHMODE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_IRTORCHMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 04/03/2019
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_IRTORCHMODE

This extended property control is used by the client to control an IR camera's infrared torch's power level and duty cycle. It is sent to the driver along with a standard [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure followed by a [KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) structure.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
| --- | --- | --- | --- | --- |
| Yes | Yes | Filter | [KSPROPERTY](./ksproperty-structure.md) | [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)|

## Remarks

The property request contains a [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) structure.

The total property data size is sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING). The **Size** member of [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The following are flags that can be placed in the **KSCAMERA_EXTENDEDPROP_HEADER.Flags** and **KSCAMERA_EXTENDEDPROP_HEADER.Capability** fields.  They define the IR torch's operating mode(s).

| Torch mode                                                       | Description                        |
|------------------------------------------------------------------|------------------------------------|
| KSCAMERA_EXTENDEDPROP_IRTORCHMODE_OFF                            | Off                                |
| KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALWAYS_ON                      | Always on                          |
| KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALTERNATING_FRAME_ILLUMINATION | On for every other frame           |

KSCAMERA_EXTENDEDPROP_IRTORCHMODE is always a synchronous control.  The control has no defined behavior when the camera is not streaming.

For a GET request, a driver sets the following fields:

- **KSCAMERA_EXTENDEDPROP_HEADER.Capability** with a bitmask of the above KSCAMERA_EXTENDEDPROP_IRTORCHMODE_*XXX* flags representing the operating modes supported by the camera.
- **KSCAMERA_EXTENDEDPROP_HEADER.Flags** to one of the above KSCAMERA_EXTENDEDPROP_IRTORCHMODE_*XXX* flags to indicate the current operating mode.
- **KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING.Mode** to 0.
- **KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING.Min** to the minimum power level available.
- **KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING.Max** to the maximum power level available.
- **KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING.Step** to the minimum increment between power levels.
- **KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING.VideoProc.ul** to the current power level. This value should default to the same power level normally used by the face authentication control.

For a SET request, a driver uses the following fields:

- **KSCAMERA_EXTENDEDPROP_HEADER.Flags** to set an operating mode.
- **KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING.VideoProc.ul** to set a power level.  This value has no effect on KSCAMERA_EXTENDEDPROP_IRTORCHMODE_OFF.

The table below contains the descriptions and requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the metadata control.

<table>
<colgroup>
<col width="30%" />
<col width="70%" />
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
<td><p>KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF).</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER)+sizeof([KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting)),</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This value is ignored for synchronous controls.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>May be any combination of <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_OFF</strong>, <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALWAYS_ON</strong> or <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALTERNATIVE_FRAME_ILLUMINATION</strong>.  
This field must report at least one capability.  The field must report either <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALWAYS_ON</strong> or <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALTERNATIVE_FRAME_ILLUMINATION</strong> or both. The value <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_OFF</strong> is optional.
</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>Must be one of the flags reported in Capability.  The default must value must be either <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALWAYS_ON</strong> or <strong>KSCAMERA_EXTENDEDPROP_IRTORCHMODE_ALTERNATIVE_FRAME_ILLUMINATION</strong>.</p></td>
</tr>
</tbody>
</table>

The table below contains the descriptions and requirements for the [KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) structure fields when using the IR torch mode control.

<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Mode</p></td>
<td><p>Unused.  Must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Min/Max/Step</p></td>
<td><p>The Min/Max/Step contains the minimum/maximum/increment of the IR power settings.  Driver must return these for GET operations.  (Max – Min) must be evenly divisible by Step.  Step may not be zero (0).</p></td>
</tr>
<tr class="odd">
<td><p>VideoProc</p></td>
<td><p>For SET operations, the VideoProc.Value.ul must specify the power level within the range described by the Min/Max/Step parameter.  For GET operations, the driver must return the current power level.</p></td>
</tr>
<tr class="even">
<td><p>Reserved</p></td>
<td><p>Unused.  Must be ignored by the driver.</p></td>
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