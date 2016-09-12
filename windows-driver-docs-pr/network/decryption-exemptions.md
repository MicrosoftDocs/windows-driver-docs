---
title: Decryption Exemptions
description: Decryption Exemptions
ms.assetid: 2a9eb917-946a-4ab8-ac5e-031705d9b654
keywords: ["decryption WDK Native 802.11", "exemptions WDK Native 802.11", "privacy exemptions WDK Native 802.11"]
---

# Decryption Exemptions


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the miniport driver is operating in Extensible Station (ExtSTA) mode, the following object identifiers (OIDs) set or query the types of exemptions used by the 802.11 station when decrypting received packets.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_EXCLUDE_UNENCRYPTED](https://msdn.microsoft.com/library/windows/hardware/ff569365)</p></td>
<td align="left"><p>Sets or queries the value of the IEEE 802.11 <strong>dot11ExcludeUnencrypted</strong> management information base (MIB) object, which specifies how the 802.11 station handles received packets with unencrypted payload data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_PRIVACY_EXEMPTION_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569404)</p></td>
<td align="left"><p>Sets or queries the list of exemptions for packet decryption.</p></td>
</tr>
</tbody>
</table>

 

The miniport driver, operating in ExtSTA mode, must support a privacy exemption list that stores a minimum of one entry. The miniport driver reports the size of the privacy exemption list when [OID\_DOT11\_EXTSTA\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366) is queried.

Each entry in the privacy exemption list defines actions applied to received packets that match the IEEE EtherType defined for the entry. Exemption actions include:

-   Accept the received packet if the payload data is not encrypted and the IEEE EtherType value is the same as specified for the privacy exemption entry.

-   Reject the received packet if the payload data is encrypted and (after decryption) the IEEE EtherType value is the same as specified for the privacy exemption entry.

-   Reject the received packet if the payload data is not encrypted and an appropriate cipher key is available. For example, this action would apply under the following circumstances:

    One or more default cipher keys exist and a default key identifier (ID) has been defined. For more information about the default key ID, see [OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569120).

    A key-mapping key is available for the source media access control (MAC) address of the received packet.

-   Apply the exemption action to unicast or multicast/broadcast packets, or both packet types.

After the 802.11 station enables cipher operations for the basic service set (BSS) connection, it must follow these guidelines when applying decryption exemptions to received packets:

-   If the 802.11 station receives an encrypted packet, the station must first decrypt the packet as described in [Decryption Guidelines](decryption-guidelines.md).

-   If the packet's EtherType matches an entry within the privacy exemption list, the 802.11 station must apply the rules that are defined for the entry to determine whether to accept or reject the packet.

-   If the packet's EtherType does not match an entry within the privacy exemption list, the 802.11 station must reject the packet if it was received unencrypted and the **dot11ExcludeUnencrypted** MIB object is set to **TRUE**.

    For more information about how the 802.11 station rejects the received packet, see [Packet Decryption](packet-decryption.md).

 

 





