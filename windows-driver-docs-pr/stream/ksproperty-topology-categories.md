---
title: KSPROPERTY\_TOPOLOGY\_CATEGORIES
description: The KSPROPERTY\_TOPOLOGY\_CATEGORIES property queries for the array of functional categories that a driver supports.
ms.assetid: 35a293a1-f8fe-44da-a50b-a4429e369567
keywords: ["KSPROPERTY_TOPOLOGY_CATEGORIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TOPOLOGY_CATEGORIES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TOPOLOGY\_CATEGORIES


The KSPROPERTY\_TOPOLOGY\_CATEGORIES property queries for the array of functional categories that a driver supports.

## <span id="ddk_ksproperty_topology_categories_ks"></span><span id="DDK_KSPROPERTY_TOPOLOGY_CATEGORIES_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563441" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563441)"><strong>KSMULTIPLE_ITEM</strong></a>, followed by a sequence of GUIDs</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441) structure, followed by a sequence of GUIDs representing the possible functional categories the KS filter supports. Microsoft provides standard categories in *ks.h* and *ksmedia.h*. The following is a list of the functional categories that are not technology-specific:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Functional category</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSCATEGORY_BRIDGE</p></td>
<td><p>Bridge to outside the kernel streaming subsystem.</p></td>
</tr>
<tr class="even">
<td><p>KSCATEGORY_CAPTURE</p></td>
<td><p>Captures.</p></td>
</tr>
<tr class="odd">
<td><p></p>
KSCATEGORY_
COMMUNICATIONSTRANSFORM</td>
<td><p>Communication transform device.</p></td>
</tr>
<tr class="even">
<td><p>KSCATEGORY_DATACOMPRESSOR</p></td>
<td><p>Compresses a data stream.</p></td>
</tr>
<tr class="odd">
<td><p>KSCATEGORY_DATADECOMPRESSOR</p></td>
<td><p>Decompresses a data stream.</p></td>
</tr>
<tr class="even">
<td><p>KSCATEGORY_DATATRANSFORM</p></td>
<td><p>Transforms a data stream.</p></td>
</tr>
<tr class="odd">
<td><p>KSCATEGORY_FILESYSTEM</p></td>
<td><p>Moves a data stream into or out of the file system.</p></td>
</tr>
<tr class="even">
<td><p>KSCATEGORY_INTERFACETRANSFORM</p></td>
<td><p>Transforms the interface type being used.</p></td>
</tr>
<tr class="odd">
<td><p>KSCATEGORY_MEDIUMTRANSFORM</p></td>
<td><p>Transforms the medium type being used.</p></td>
</tr>
<tr class="even">
<td><p>KSCATEGORY_MIXER</p></td>
<td><p>Mixes multiple data streams.</p></td>
</tr>
<tr class="odd">
<td><p>KSCATEGORY_RENDER</p></td>
<td><p>Renderer.</p></td>
</tr>
<tr class="even">
<td><p>KSCATEGORY_SPLITTER</p></td>
<td><p>Splits a data stream.</p></td>
</tr>
</tbody>
</table>

 

Topology categories correspond to device interface classes.

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
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSTOPOLOGY**](https://msdn.microsoft.com/library/windows/hardware/ff567146)

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

 

 






