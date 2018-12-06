---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA
description: This extended property control is used by the client to query the driver for the metadata buffer requirements.
ms.assetid: 6196DFF6-050A-4916-A188-70A89B60B5EA
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_METADATA Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_METADATA
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA

This extended property control is used by the client to query the driver for the metadata buffer requirements. It is sent to the driver along with a standard [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure followed by a [**KSCAMERA\_EXTENDEDPROP\_METADATAINFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_metadatainfo) structure.

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

The following are metadata flags that can be placed in the **KSCAMERA\_EXTENDEDPROP\_HEADER.Flags** field.

```cpp
#define KSCAMERA_EXTENDEDPROP_METADATA_SYSTEMMEMORY                     0x0000000000000001  
#define KSCAMERA_EXTENDEDPROP_METADATA_ALIGNMENTREQUIRED                0x0000000000000100
```

In a **Get** call, the driver does the following:

1.  Fills **KSCAMERA\_EXTENDEDPROP\_HEADER.Capability** with 0.

2.  Fill KSCAMERA\_EXTENDEDPROP\_HEADER.Flags with a combination of any of the above KSCAMERA\_EXTENDEDPROP\_METADATA\_*XXX* flags to indicate the metadata memory requirements.

3.  Fill KSCAMERA\_EXTENDEDPROP\_METADATAINFO.BufferAlignment with the desired memory alignment (KSCAMERA\_EXTENDEDPROP\_MetadataAlignment\_*Xxx*). See the [**KSCAMERA\_EXTENDEDPROP\_MetadataAlignment**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-kscamera_extendedprop_metadataalignment) for possible values.

4.  Fill **KSCAMERA\_EXTENDEDPROP\_METADATAINFO.MaxMetadataBufferSize** with the required metadata buffer size in bytes.

The table below contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the metadata control.

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
<td><p>This must be the Pin ID associated with the pin whose frame contains metadata. This can be any of the preview, record, and image pin.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>)+sizeof(<a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_metadatainfo" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_METADATAINFO&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_metadatainfo)"><strong>KSCAMERA_EXTENDEDPROP_METADATAINFO</strong></a>),</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This is unused and must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any combination of <strong>KSCAMERA_EXTENDEDPROP_METADATA_ALIGNMENTREQUIRED</strong> or KSCAMERA_EXTENDEDPROP_METADATA_SYSTEMMEMORY.</p></td>
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
