---
title: OID\_WDI\_GET\_BSS\_ENTRY\_LIST
description: OID\_WDI\_GET\_BSS\_ENTRY\_LIST is used to ask the adapter to indicate the list of BSS networks that have been cached by the port.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0eaa2b3a-6a1f-49e1-9556-81691892e666
keywords: ["OID_WDI_GET_BSS_ENTRY_LIST Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- OID_WDI_GET_BSS_ENTRY_LIST
api_location:
- dot11wdi.h
api_type:
- HeaderDef
---

# OID\_WDI\_GET\_BSS\_ENTRY\_LIST


OID\_WDI\_GET\_BSS\_ENTRY\_LIST is used to ask the adapter to indicate the list of BSS networks that have been cached by the port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Set not supported        | 1                               |

 

This is only used for an adapter that perform BSS list caching. When acting as a client, the port must report the BSS entry for the access point. In addition, if the port is performing background scans, it should report BSS entries that it has discovered in its scan.

When this request is received by the adapter, it must send [NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md) indications to the Microsoft component. These indications must contain the BSS entries that match the Get parameters. The adapter can send one or more NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST indications, but they must be completed before the property completes.

The Microsoft component uses the list of indicated entries to report the BSS list to the operation system. It is also used to populate parameters for roam and connect tasks.

## Get property parameters


| TLV                                         | Multiple TLV instances allowed | Optional | Description                                           |
|---------------------------------------------|--------------------------------|----------|-------------------------------------------------------|
| [**WDI\_TLV\_SSID**](https://msdn.microsoft.com/library/windows/hardware/dn898064) |                                |          | The SSID that the host needs the BSS list update for. |

 

## Get property results


No additional data. The data in the header is sufficient.
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md)
Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_GET_BSS_ENTRY_LIST%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




