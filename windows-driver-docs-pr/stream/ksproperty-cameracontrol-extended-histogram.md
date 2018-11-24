---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM is a property ID that will be used to control the histogram metadata produced by the driver. This is a pin level control for the preview pin only.
ms.assetid: 638AA1AA-F8E5-4FD7-9283-CF1F23266474
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM


**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM** is a property ID that will be used to control the histogram metadata produced by the driver. This is a pin level control for the preview pin only.

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

 

The following flags can be placed in the **KSCAMERA\_EXTENDEDPROP\_HEADER.Flags** field to control the histogram metadata in driver. The default is **HISTOGRAM\_OFF**.

```cpp
#define KSCAMERA_EXTENDEDPROP_HISTOGRAM_OFF      0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_HISTOGRAM_ON       0x0000000000000001
```

This control must be used before the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA**](ksproperty-cameracontrol-extended-metadata.md) control to ensure the proper sized metadata buffer is allocated.

If set to **HISTOGRAM\_OFF**, the driver shall not deliver the histogram metadata on the preview pin. The driver should not include the histogram metadata size in its metadata buffer size requirement.

If set to **HISTOGRAM\_ON**, the driver shall deliver the histogram metadata on the preview pin. The driver must include the histogram metadata size in its metadata buffer size requirement.

If the driver does not have the capability to produce histogram metadata, the driver should not implement this control. If the driver supports this control, it must also support [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA**](ksproperty-cameracontrol-extended-metadata.md) control.

The **SET** call of this control has no effect when the preview pin is in any state higher than the KSSTATE\_STOP state. The driver shall reject the **SET** call received if preview is not in the stop state and returns **STATUS\_INVALID\_DEVICE\_STATE**. In a **GET** call, driver should return the current settings in **Flags** field.

The following table contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

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
<td><p>Must be the Pin ID associated with the preview pin.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>) + sizeof(<a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_VALUE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)"><strong>KSCAMERA_EXTENDEDPROP_VALUE</strong></a>).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last <strong>SET</strong> operation. If no <strong>SET</strong> operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>Must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the <strong>KSCAMERA_EXTENDEDPROP_HISTOGRAM_*</strong> flags defined above.</p></td>
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
