---
title: NDIS\_STATUS\_MEDIA\_DISCONNECT
description: The NDIS\_STATUS\_MEDIA\_DISCONNECT status indicates that the status of a network connection has changed from connected to disconnected.
MS-HAID:
- 'ndis\_status\_indications\_ref\_fbde4da8-ed6c-4d6c-aa20-ea6c37b48664.xml'
- 'netvista.ndis\_status\_media\_disconnect'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 490853ca-c849-4b2b-9639-4be670616101
keywords: ["NDIS_STATUS_MEDIA_DISCONNECT Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_MEDIA_DISCONNECT
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NDIS\_STATUS\_MEDIA\_DISCONNECT


The NDIS\_STATUS\_MEDIA\_DISCONNECT status indicates that the status of a network connection has changed from connected to disconnected. For example, the network device loses the connection because it is out of range (for a wireless device), or the user unplugs the device's network cable.

Remarks
-------

NDIS translates NDIS\_STATUS\_MEDIA\_DISCONNECT status indications to [**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md) status indications for overlying NDIS 6.0 drivers.

NDIS 5.*x* and earlier miniport drivers indicate an [**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md) status when the connection is restored.

For more information about NDIS\_STATUS\_MEDIA\_DISCONNECT, see [Indicating Connection Status (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff546856) and [Media Status Indications for 802.11 Networks](https://msdn.microsoft.com/library/windows/hardware/ff549301).

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
<td><p>Not supported in NDIS 6.0 and later (use [<strong>NDIS_STATUS_LINK_STATE</strong>](ndis-status-link-state.md) instead). Supported only for NDIS 5.1 drivers in Windows Vista and Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md)

[**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_MEDIA_DISCONNECT%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





