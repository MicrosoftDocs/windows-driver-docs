---
title: NDIS\_STATUS\_WAN\_LINE\_UP
description: The NDIS\_STATUS\_WAN\_LINE\_UP status indicates that a WAN-capable miniport driver has established a connection with a remote node.
MS-HAID:
- 'ndis\_status\_indications\_ref\_d364a457-0e95-47be-a529-e5d32ba64856.xml'
- 'netvista.ndis\_status\_wan\_line\_up'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1eb9d934-871a-4d95-b04f-d0b174716c98
keywords: ["NDIS_STATUS_WAN_LINE_UP Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_WAN_LINE_UP
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NDIS\_STATUS\_WAN\_LINE\_UP


The NDIS\_STATUS\_WAN\_LINE\_UP status indicates that a WAN-capable miniport driver has established a connection with a remote node.

Remarks
-------

NDIS 4.*x* and earlier NDIS WAN miniport drivers use this status indication. NDIS 5.0 and later WAN miniport drivers must use the CoNDIS WAN interface. For more information about the CoNDIS WAN interface, see [Implementing CoNDIS WAN Miniport Drivers (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff546752).

The *StatusBuffer* parameter of the [**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538) function contains a pointer to an [**NDIS\_MAC\_LINE\_UP**](https://msdn.microsoft.com/library/windows/hardware/ff557058) structure.

For more information about NDIS\_STATUS\_WAN\_LINE\_UP, see [Line-Up Indication (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff549189) and [Indicating NDIS WAN Miniport Driver Status (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff546867).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Not supported for NDIS 6.0 drivers or NDIS 5.1 drivers in Windows Vista or Windows XP. Supported for NDIS 4.x drivers.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_MAC\_LINE\_UP**](https://msdn.microsoft.com/library/windows/hardware/ff557058)

[**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WAN_LINE_UP%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





