---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA
description: This extended property control is used by the client to query the driver for the metadata buffer requirements.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA


This extended property control is used by the client to query the driver for the metadata buffer requirements. It is sent to the driver along with a standard [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure followed by a [**KSCAMERA\_EXTENDEDPROP\_METADATAINFO**](https://msdn.microsoft.com/library/windows/hardware/dn925144) structure.

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

 

The following are metadata flags that can be placed in the **KSCAMERA\_EXTENDEDPROP\_HEADER.Flags** field.

``` syntax
#define KSCAMERA_EXTENDEDPROP_METADATA_SYSTEMMEMORY                     0x0000000000000001  
#define KSCAMERA_EXTENDEDPROP_METADATA_ALIGNMENTREQUIRED                0x0000000000000100
```

In a **Get** call, the driver does the following:

1.  Fills **KSCAMERA\_EXTENDEDPROP\_HEADER.Capability** with 0.

2.  Fill KSCAMERA\_EXTENDEDPROP\_HEADER.Flags with a combination of any of the above KSCAMERA\_EXTENDEDPROP\_METADATA\_*XXX* flags to indicate the metadata memory requirements.

3.  Fill KSCAMERA\_EXTENDEDPROP\_METADATAINFO.BufferAlignment with the desired memory alignment (KSCAMERA\_EXTENDEDPROP\_MetadataAlignment\_*Xxx*). See the [**KSCAMERA\_EXTENDEDPROP\_MetadataAlignment**](https://msdn.microsoft.com/library/windows/hardware/dn925140) for possible values.

4.  Fill **KSCAMERA\_EXTENDEDPROP\_METADATAINFO.MaxMetadataBufferSize** with the required metadata buffer size in bytes.

The table below contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure fields when using the metadata control.

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
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>)+sizeof([<strong>KSCAMERA_EXTENDEDPROP_METADATAINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/dn925144)),</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_METADATA%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




