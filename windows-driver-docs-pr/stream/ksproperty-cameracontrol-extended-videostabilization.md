---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VIDEOSTABILIZATION
description: This extended property control is used to control digital video stabilization in driver\\MFT0.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOSTABILIZATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOSTABILIZATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VIDEOSTABILIZATION

This extended property control is used to control digital video stabilization in driver\\MFT0.

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

The following flags that can be placed in the KSCAMERA\_EXTENDEDPROP\_HEADER.Flags field flags to control digital video stabilization in driver\\MFT0. By default, the driver should have video stabilization off.

```cpp
#define KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_OFF       0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_ON        0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_AUTO      0x0000000000000002
```

If the driver does not support digital video stabilization, the driver should not implement this control.

If the driver supports this control, it must support VIDEOSTABILIZATION\_ON\\OFF.

The SET call of this control has no effect when the video pin is in any state higher than the KSSTATE\_STOP state. The driver shall reject the SET call received if video pin is not in the stop state and returns STATUS\_INVALID\_DEVICE\_STATE. In a GET call, driver should return the current settings in Flags field.

When this control is used in the context of a profile, the profile shall serve as a hint to the driver for the quality mode. The driver can determine whether to optimize for low latency or high quality when video stabilization is turned on based on the profile selected, for example, video conference or high quality video recording.

> [!NOTE]
> PROPSETID\_VIDCAP\_CAMERACONTROL\_VIDEO\_STABILIZATION will be deprecated for Windows 10.

The following table describes the flag capabilities.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_OFF</p></td>
<td><p>This is a mandatory capability. When specified, digital video stabilization is disabled in driver\MFT0.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_ON</p></td>
<td><p>This is a mandatory capability. When specified, the digital video stabilization is enabled in driver\MFT0 and the default overscan padding setting is up to the driver. This flag is mutually exclusive with the AUTO and OFF flags.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_AUTO</p></td>
<td><p>This capability is optional. When specified, the driver that supports such capability will determine whether video stabilization should be performed and how much stabilization to be applied based on the scene analysis and the capture scenario. This flag is mutually exclusive with the ON and OFF flags.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Depending on the implementation, the overscanned buffer may be allocated either by the driver internally or by the pipeline.

If the overscanned buffer is to be allocated by the driver, the driver should advertise both the regular media type and the overscanned media type. The MFT0 should advertise the regular media type. Upon setting the regular media type on the output media type of MFT0, the MFT0 should select the corresponding overscanned media type from the driver advertised media types as its input media type, if the video stabilization is turned on. If the video stabilization is turned off, the MFT0 should select the regular media type as its input media type. The MFT0 should return MF\_E\_INVALIDMEDIATYPE if overscanned media type is set as its output media type when the video stabilization is turned on.

If overscanned buffer is allocated by the driver, both the driver and MFT0 should advertise the regular media types. MFT0 should set the regular media type for both its input media type and output media type.

In order to support effect based video stabilization (i.e., video stabilization done neither in driver nor in MFT0), the driver and MFT0 must additionally advertise the overscanned media type regardless. In this case, both regular and overscanned media types are exposed by the driver and MFT0. The following rules will apply to ensure both effect based and driver\\MFT0 based video stabilization are working correctly.

-   If an overscanned media type is set as the MFT0 output media type while driver\\MFT0 based video stabilization is on, MFT0 should return MF\_E\_INVALIDMEDIATYPE.

-   If a regular media type is set as the MFT0 output media type, the app should return an error in the attempt of turning on the effect based video stabilization if the effect based video stabilization can only take the overscanned media type.

The table below contains the descriptions and requirements for the [KSCAMERA\_EXTENDEDPROP\_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the video stabilization control.

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
<td><p>Must be the Pin ID associated with the video pin.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_XXX flags as defined above.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_XXX flags defined above.</p></td>
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
