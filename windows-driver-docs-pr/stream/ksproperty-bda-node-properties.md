---
title: KSPROPERTY\_BDA\_NODE\_PROPERTIES
description: Clients use KSPROPERTY\_BDA\_NODE\_PROPERTIES to retrieve a list of properties supported on a node.
MS-HAID:
- 'bdaref\_f0773162-7234-44f0-bd72-bc97c1694e5a.xml'
- 'stream.ksproperty\_bda\_node\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 36d37844-a69b-4f67-bb8f-e5445ba9a2cb
keywords: ["KSPROPERTY_BDA_NODE_PROPERTIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_NODE_PROPERTIES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_BDA\_NODE\_PROPERTIES


Clients use KSPROPERTY\_BDA\_NODE\_PROPERTIES to retrieve a list of properties supported on a node.

## <span id="ddk_ksproperty_bda_node_properties_ks"></span><span id="DDK_KSPROPERTY_BDA_NODE_PROPERTIES_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>KSPROPERTY</p></td>
<td><p>List of GUIDs</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The list of properties supported by a node is a list of GUIDs.

The network provider will use this property to query the capabilities of each node in the BDA template connection list.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**BdaPropertyNodeProperties**](https://msdn.microsoft.com/library/windows/hardware/ff556496)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_BDA_NODE_PROPERTIES%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





