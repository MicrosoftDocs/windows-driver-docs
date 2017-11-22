---
title: KSPROPERTY\_NUM\_SOURCES
description: The KSPROPERTY\_NUM\_SOURCES property specifies the number of input pins on the selector unit.
MS-HAID:
- 'vidcapprop\_1ab5b371-9923-4393-b6d1-597870411917.xml'
- 'stream.ksproperty\_num\_sources'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 94d0f926-0551-4fe2-aa7f-2898e04c4b36
keywords: ["KSPROPERTY_NUM_SOURCES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_NUM_SOURCES
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_NUM\_SOURCES


The KSPROPERTY\_NUM\_SOURCES property specifies the number of input pins on the selector unit.

## <span id="ddk_ksproperty_num_sources_ks"></span><span id="DDK_KSPROPERTY_NUM_SOURCES_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_SELECTOR_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565219) or [<strong>KSPROPERTY_SELECTOR_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565217)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When making a get request, the client receives the number of available source pins in the **Value** member of the property descriptor structure.

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
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_NUM_SOURCES%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




