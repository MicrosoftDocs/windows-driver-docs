---
title: Indicating Raw 802.11 Packets
description: Indicating Raw 802.11 Packets
ms.assetid: df2295f3-13d6-41d7-9959-c34f19af33ea
keywords:
- raw packets WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Indicating Raw 802.11 Packets


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Usually, when the miniport driver indicates 802.11 packets, the packets are complete media access control (MAC) service data unit (MSDU) or MAC management protocol data unit (MMPDU) packets. In this situation, the 802.11 station has reassembled and decrypted each MAC protocol data unit (MPDU) fragment for the MSDU or MMPDU packet. If a MPDU fails during decryption or verification, the 802.11 station must discard all MPDU fragments and the miniport driver must not make the packet indication through a call to [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).

However, if enabled for raw packet indication, the miniport driver must make the packet indication for every received MPDU fragment of an MSDU or MMPDU packet regardless of whether the MPDU fragment succeeded or failed to decrypt.

The miniport driver must indicate raw 802.11 packets when the current packet filter is set to one of the following:

<a href="" id="ndis-packet-type-802-11-raw-data"></a>NDIS\_PACKET\_TYPE\_802\_11\_RAW\_DATA  
When this packet filter is enabled, the miniport driver must indicate each raw MPDU fragment for an MSDU packet.

<a href="" id="ndis-packet-type-802-11-raw-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_RAW\_MGMT  
When this packet filter is enabled, the miniport driver must indicate each raw MPDU fragment for an MMPDU packet.

For more information about how the current packet filter is set or queried, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

**Note**  It is only valid for the miniport driver to enable the NDIS\_PACKET\_TYPE\_802\_11\_RAW\_DATA or NDIS\_PACKET\_TYPE\_802\_11\_RAW\_MGMT packet filters if the driver is operating in Network Monitor (NetMon) or Extensible Access Point (AP) modes. For more information about these modes, see [Network Monitor Operation Mode](network-monitor-operation-mode.md) and [Extensible Access Point Operation Mode](extensible-access-point-operation-mode.md).

 

The miniport driver must follow these guidelines when indicating raw MPDU fragments.

-   When indicating raw MPDU frames, the miniport driver must set DOT11\_RECV\_FLAG\_RAW\_PACKET in the **uReceiveFlags** member of the DOT11\_EXTSTA\_RECV\_CONTEXT structure. Also, the miniport driver must prepare the DOT11\_EXTSTA\_RECV\_CONTEXT structure for the raw packet indication as described in [Media-Specific OOB Data for Received 802.11 Packets](media-specific-oob-data-for-received-802-11-packets.md).

-   The packet data for the MPDU frame must be unmodified. In this situation, the data must be exactly as received by the 802.11 station. The 802.11 station must neither decrypt the MPDU data nor reassemble the fragment with other received MPDU fragments.

-   All of the MPDU fragments that belong to the same MSDU or MMPDU packet must be indicated in one [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, with one [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure for each raw MPDU fragment.

-   The miniport driver must indicate each received MPDU fragment regardless of any of the following conditions:
    -   The MPDU data eventually fails to decrypt or verify.
    -   The MSDU or MMPDU packet fails to reassemble correctly due to missing MPDU fragments.
    -   The MPDU was received with frame check sequence (FCS) failures. If the 802.11 station is able to receive MPDU packets with FCS errors, the miniport driver must set the DOT11\_RECV\_FLAG\_RAW\_PACKET\_FCS\_FAILURE in the **uReceiveFlags** member.
-   The miniport driver can optionally indicate the decrypted and reassembled MSDU packet or reassembled MMPDU frame following the indication of the raw MPDU fragments. For more information about this process, see [Guidelines for Indicating Received 802.11 Packets](guidelines-for-indicating-received-802-11-packets.md).

-   If the miniport driver is operating in the ExtAP mode, the following requirements apply.

    <table>
    <colgroup>
    <col width="25%" />
    <col width="25%" />
    <col width="25%" />
    <col width="25%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Configuration</th>
    <th align="left">Raw mode</th>
    <th align="left">Raw packets indication</th>
    <th align="left">Non-raw packet indication</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>ExtAP INIT state</p></td>
    <td align="left"><p>Off</p></td>
    <td align="left"><p>Not applicable</p></td>
    <td align="left"><p>Mandatory</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ExtAP INIT state</p></td>
    <td align="left"><p>On</p></td>
    <td align="left"><p>Mandatory</p></td>
    <td align="left"><p>Optional</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ExtAP OP state:</p></td>
    <td align="left"><p>Off</p></td>
    <td align="left"><p>Not applicable</p></td>
    <td align="left"><p>Mandatory</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ExtAP OP state:</p></td>
    <td align="left"><p>On</p></td>
    <td align="left"><p>Optional</p></td>
    <td align="left"><p>Mandatory</p></td>
    </tr>
    </tbody>
    </table>

     

    If the driver indicates both raw and non-raw packets, it might need to duplicate the received packets when raw mode is enabled.

 

 





