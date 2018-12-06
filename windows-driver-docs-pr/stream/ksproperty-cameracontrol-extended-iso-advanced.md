---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED is an extended property control that allows more global ISO control with more granularity.
ms.assetid: A9327DB8-422B-410C-8766-D70811BA5C73
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_ISO_ADVANCED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_ISO_ADVANCED
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED

KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED is an extended property control that allows more global ISO control with more granularity.

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
<td><p>Pin (Photo)</p></td>
<td><p>Asynchronous</p></td>
</tr>
</tbody>
</table>

The new KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL flag is defined in ksmedia\_phone.h as follows.

```cpp
#define KSCAMERA_EXTENDEDPROP_ISO_MANUAL          0x0080000000000000
```

The following table contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields for the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED control.

The Windows 8.1 KS\_CAMERACONTROL\_EXTENDED\_ISO remains unchanged without the support of integer manual ISO. The driver should only support the new KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED control. If both of these controls are supported, the pipeline will default to the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED control.

If the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED control is supported, the only capabilities that the driver can advertise are the following.

-   KSCAMERA\_EXTENDEDPROP\_ISO\_AUTO

-   KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL

-   KSCAMERA\_EXTENDEDPROP\_CAPS\_ASYNCCONTROL

If the driver advertises the KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL capability flag, it must also advertise the supported ISO ranges in the Min/Max/Step value of the KSCAMERA\_EXTENDED\_PROP\_VIDEOPROCSETTING property. If the driver advertises a Min value of 0 and a Max value of 0, or a Step value of less than 1, the control is flagged as unusable and is rejected by the pipeline.

If the driver supports both KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED and KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO, the driver must advertise KSCAMERA\_EXTENDEDPROP\_ISO\_AUTO for both KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED and KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO. Otherwise, both ISO controls will be flagged as unusable and rejected by the MF pipeline.

If the driver advertises KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL in KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED and the numeric KSCAMERA\_EXTENDEDPROP\_ISO\_XXX values in KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO, the numeric KSCAMERA\_EXTENDEDPROP\_ISO\_XXX values advertised in KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO should be in the supported manual ISO ranges advertised by KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL. In addition, all the numeric KSCAMERA\_EXTENDEDPROP\_ISO\_XXX values in the supported manual ranges should be advertised by KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO. Otherwise, both ISO controls may be flagged as unusable and rejected by the MF pipeline.

For example, capabilities of any of the following may be treated as a catastrophic failure and the control may be rejected by the MF pipeline.

-   KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL (min= 40, max = 240, step = 20), KSCAMERA\_EXTENDEDPROP\_ISO\_50

-   KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL (min= 40, max = 240, step = 20), KSCAMERA\_EXTENDEDPROP\_ISO\_80

-   KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL (min= 40, max = 240, step = 20), KSCAMERA\_EXTENDEDPROP\_ISO\_400

Capabilities of any of the following are accepted by the MF pipeline.

-   KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL (min= 40, max = 240, step = 20), KSCAMERA\_EXTENDEDPROP\_ISO\_80, KSCAMERA\_EXTENDEDPROP\_ISO\_100, KSCAMERA\_EXTENDEDPROP\_ISO\_200

-   KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL (min= 40, max = 240, step = 20)

-   KSCAMERA\_EXTENDEDPROP\_ISO\_80, KSCAMERA\_EXTENDEDPROP\_ISO\_200

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
<td><p>This must be 1,</p></td>
</tr>
<tr class="even">
<td><p>PinId</p></td>
<td><p>This must be the Pin ID associated with the photo pin.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER)+sizeof(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING),</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This contains the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be a bit wise OR of KSCAMERA_EXTENDEDPROP_ISO_AUTO and\or KSCAMERA_EXTENDEDPROP_ISO_MANUAL, and the KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL flag. This control must be asynchronous.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any of the KSCAMERA_EXTENDEDPROP_ISO_XXX flags defined above.</p></td>
</tr>
</tbody>
</table>

 

The following table contains the descriptions and requirements for the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING structure fields for the ISO DDI. This structure is defined in ksmedia.h.

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
<td><p>Mode</p></td>
<td><p>This is unused and must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Min/Max/Step</p></td>
<td><p>The Min/Max/Step contains the minimum/maximum/increment of the manual ISO speed supported by the camera driver. The driver must return these for GET operations if manual ISO is supported.</p></td>
</tr>
<tr class="odd">
<td><p>VideoProc</p></td>
<td><p>If MANUAL is specified in the Flags field of the KSCAMERA_EXTENDEDPROP_HEADER, the VideoProc.Value.ul must specify the current ISO speed value within the range described by the Min/Max/Step parameter.</p>
<p>If Flags other than Manual is specified, for SET operations, the VideoProc field is ignored. For GET operations, the driver must always return the current ISO speed regardless.</p></td>
</tr>
<tr class="even">
<td><p>Reserved</p></td>
<td><p>This is unused. This must be ignored by the driver.</p></td>
</tr>
</tbody>
</table>

 

**GET call**

The driver must advertise its capability in KSCAMERA\_EXTENDEDPROP\_HEADER.Capability and the current ISO flag at driver in KSCAMERA\_EXTENDEDPROP\_HEADER.Flags.Â  If no SET call has ever been issued before the Get call, driver should return its default in KSCAMERA\_EXTENDEDPROP\_HEADER.Flags.

If the KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL flag is advertised in the Capability field, the driver must further advertise the supported ranges in KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING.Min/Max/Step.

The driver must also report the current ISO speed in use in KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING.VideoProc.Value.ul. If no SET call has ever been issued before the GET call, the driver should return its current ISO speed in KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING.VideoProc.Value.ul.

**SET call**

The KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING.VideoProc.Value.ul contains the desired integer manual ISO speed if KSCAMERA\_EXTENDEDPROP\_ISO\_MANUAL is specified in KSCAMERA\_EXTENDEDPROP\_HEADER.Flags.

If the KSCAMERA\_EXTENDEDPROP\_ISO\_AUTO flag is specified in KSCAMERA\_EXTENDEDPROP\_HEADER.Flags, KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING.VideoProc.Value.ul will be ignored.

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
