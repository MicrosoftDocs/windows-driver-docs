---
title: WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY
description: WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY is a TLV that contains RSN Rekey protocol offload parameters.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4FDB56EA-444B-4EA2-B8D1-5E740734EEED
keywords: ["WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY is a TLV that contains RSN Rekey protocol offload parameters.

## TLV Type


0x63

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type        | Description                                                                                                                                                                                                                                                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32      | Specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter. |
| UINT64      | Specifies the replay counter.                                                                                                                                                                                                                                                                               |
| UINT8\[16\] | Specifies the IEEE 802.11 key confirmation key (KCK).                                                                                                                                                                                                                                                       |
| UINT8\[16\] | Specifies the IEEE 802.11 key encryption key (KEK).                                                                                                                                                                                                                                                         |

 

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
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




