---
title: 802.11 Payload Encapsulation
description: 802.11 Payload Encapsulation
ms.assetid: 03336b87-22b0-4a2a-aaa9-91c58f329a16
keywords: ["encapsulation WDK Native 802.11", "payload encapsulation WDK Native 802.11", "EtherType encapsulations WDK Native 802.11", "send operations WDK Native 802.11", "receive operations WDK Native 802.11"]
---

# 802.11 Payload Encapsulation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

By default, the operating system performs EtherType encapsulation on all sent or received media access control (MAC) service data unit (MSDU) packets, as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IEEE EtherType</th>
<th align="left">Encapsulation type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>AppleTalk Address Resolution Protocol (0x80F3)</p></td>
<td align="left"><p>IEEE 802.1h</p></td>
</tr>
<tr class="even">
<td align="left"><p>IPX (0x8137)</p></td>
<td align="left"><p>IEEE 802.1h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>All other EtherTypes</p></td>
<td align="left"><p>RFC 1042</p></td>
</tr>
</tbody>
</table>

 

When associating to an access point (AP) in an infrastructure BSS network, the miniport driver must specify its own list of EtherType encapsulations if the BSS association requires additional or different EtherType encapsulations. The miniport driver specifies its EtherType encapsulation list when it makes an [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319) indication.

The operating system performs the encapsulation for the EtherType of a sent or received packet based on the following sequence:

-   If the EtherType is found in the miniport driver's encapsulation list, the operating system performs the specified encapsulation.

-   Otherwise, if the EtherType is found in the default encapsulation table, the operating system performs the specified encapsulation.

The miniport driver formats each entry in its EtherType encapsulation list as a [**DOT11\_ENCAP\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff547685) structure.

The following points apply to the miniport driver's EtherType encapsulation list:

-   The miniport driver must not provide an EtherType encapsulation list through the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319) indication if the IEEE **dot11DesiredBSSType** management information base (MIB) object is set to **dot11\_BSS\_type\_independent**. For more information about this MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569142).

-   The operating system deletes the miniport driver's EtherType encapsulation list from its default encapsulation list when the miniport driver completes a disassociation operation. For more information about this operation, see [Disassociation Operations](disassociation-operations.md).

 

 





