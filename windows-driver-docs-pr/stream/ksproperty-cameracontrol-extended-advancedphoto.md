---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ADVANCEDPHOTO
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ADVANCEDPHOTO is used to control photo HDR, flash no flash, and ultra low light fusion on the driver. This is a pin level control for photo pin only.
ms.assetid: 88C14C9E-8675-42BF-A606-64232ABD4FD1
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_ADVANCEDPHOTO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_ADVANCEDPHOTO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ADVANCEDPHOTO


KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ADVANCEDPHOTO is used to control photo HDR, flash no flash, and ultra low light fusion on the driver. This is a pin level control for photo pin only.

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

 

The following are flags that can be placed in the KSCAMERA\_EXTENDEDPROP\_HEADER.Flags field to control photo HDR, flash no flash, and ultra low light fusion. The default should be KSCAMERA\_EXTENDEDPROP\_ADVANCEDPHOTO\_OFF.

```cpp
#define KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_OFF             0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_AUTO            0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_HDR             0x0000000000000002
#define KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_FNF             0x0000000000000004
#define KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_ULTRALOWLIGHT   0x0000000000000008
```

If the driver supports this control, it must support KSCAMERA\_EXTENDEDPROP\_ADVANCEDPHOTO\_OFF.

If the driver does not support any of the advanced photo captures, the driver should not implement this control.

The SET call of this control has no effect when the photo pin is KSSTATE\_RUN state. The driver shall reject the SET call received if photo pin is in running state and returns STATUS\_INVALID\_DEVICE\_STATE. In a GET call, driver should return the current settings in Flags field.

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
<td><p>KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_OFF</p></td>
<td><p>This is a mandatory capability. When specified, no advanced photo should be performed in the driver.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_AUTO</p></td>
<td><p>This capability is optional. When specified alone, the driver that supports such capability will determine whether photo HDR, Flash no Flash, or ultra low light fusion should be performed based on the scene analysis. This flag is mutually exclusive with the OFF flag and can be used with the other flags.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_HDR</p></td>
<td><p>This capability is optional. When specified alone, the driver that supports such capability will perform photo HDR. This flag is mutually exclusive with the other flags except AUTO. When specified together with AUTO, the driver will determine whether photo HDR should be performed based on the scene analysis.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_FNF</p></td>
<td><p>This capability is optional. When specified alone, the driver that supports such capability will perform flash no flash. This flag is mutually exclusive with the other flags except AUTO. When specified together with AUTO, the driver will determine whether flash no flash should be performed based on the scene analysis.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_ULTRALOWLIGHT</p></td>
<td><p>This capability is optional. When specified alone, the driver that supports such capability will perform ultra low light fusion. This flag is mutually exclusive with the other flags except AUTO. When specified together with AUTO, the driver will determine whether ultra low light fusion should be performed based on the scene analysis.</p></td>
</tr>
</tbody>
</table>

 

The table below contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

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
<td><p>Must be the Pin ID associated with the photo pin.</p></td>
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
<td><p>Must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_* flags defined above.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_* flags defined above.</p></td>
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
