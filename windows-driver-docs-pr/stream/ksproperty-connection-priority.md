---
title: KSPROPERTY\_CONNECTION\_PRIORITY
description: Clients use the KSPROPERTY\_CONNECTION\_PRIORITY property to get or set the priority of a connection.
ms.assetid: 2037fe95-e176-4714-ad36-65a0e25b29e0
keywords: ["KSPROPERTY_CONNECTION_PRIORITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_PRIORITY
api_location:
- ks.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CONNECTION\_PRIORITY


Clients use the KSPROPERTY\_CONNECTION\_PRIORITY property to get or set the priority of a connection.

## <span id="ddk_ksproperty_connection_priority_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_PRIORITY_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSPRIORITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564250)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a structure of type [**KSPRIORITY**](https://msdn.microsoft.com/library/windows/hardware/ff564250) that contains a priority class and subclass.

One priority is greater than another if the **PriorityClass** member is greater, or if the **PriorityClass** members are identical and the **PrioritySubClass** member is greater.

The following predefined values of **PriorityClass** are available: KSPRIORITY\_LOW, KSPRIORITY\_NORMAL, KSPRIORITY\_HIGH, and KSPRIORITY\_EXCLUSIVE. Priority defaults to KSPRIORITY\_NORMAL. KSPRIORITY\_EXCLUSIVE indicates the connection has exclusive access to resources used by a pin.

The priority values have global significance: a client can use the reported values to set priorities between two different pins on two unrelated kernel streaming filters.

KSPROPERTY\_CONNECTION\_PRIORITY is optional. Clients treat pins that do not support it as having priority KSPRIORITY\_NORMAL.

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

## <span id="see_also"></span>See also


[**KSPRIORITY**](https://msdn.microsoft.com/library/windows/hardware/ff564250)

[**KSPIN\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff563531)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CONNECTION_PRIORITY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





