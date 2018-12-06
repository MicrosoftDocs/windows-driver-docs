---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to set and get the photo confirmation settings in the driver.
ms.assetid: 3EF6FF15-6805-4D91-B053-1BF6C5D5BEF2
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION

The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn917962) enumeration is used to set and get the photo confirmation settings in the driver.

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
<td><p>Filter</p></td>
<td><p>Synchronous</p></td>
</tr>
</tbody>
</table>

For the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header), the following flag values are used to turn photo confirmation on or off. By default, the driver should have **KSPROPERTY\_PHOTOCONFIRMATION\_ON** set. The flag values are defined as follows.

```cpp
#define KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_OFF     0x0000000000000000 
#define KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_ON      0x0000000000000001
```

If the photo confirmation is set to **KSCAMERA\_EXTENDEDPROP\_PHOTOCONFIRMATION\_OFF**, the driver preview pin must not produce a photo frame or produce the [**KSCAMERA\_METADATA\_PHOTOCONFIRMATION**](https://msdn.microsoft.com/library/windows/hardware/dn925187) structure that contains photo confirmation metadata. If the photo confirmation is set to **KSCAMERA\_EXTENDEDPROP\_PHOTOCONFIRMATION\_ON**, the driver preview pin must produce a photo frame and produce the **KSCAMERA\_METADATA\_PHOTOCONFIRMATION** structure that contains photo confirmation metadata.

The table below contains the descriptions and requirements for the **KSCAMERA\_EXTENDEDPROP\_HEADER** structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION** property.

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
<td><p>This must be <strong>KSCAMERA_EXTENDEDPROP_FILTERSCOPE</strong> (0xFFFFFFFF),</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>)+sizeof(<a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_VALUE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)"><strong>KSCAMERA_EXTENDEDPROP_VALUE</strong></a>).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This contains the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any of the <strong>KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_Xxx</strong> flags defined above.</p></td>
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
