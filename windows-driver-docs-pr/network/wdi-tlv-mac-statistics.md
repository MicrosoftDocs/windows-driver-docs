---
title: WDI\_TLV\_MAC\_STATISTICS
description: WDI\_TLV\_MAC\_STATISTICS is a TLV that contains per-peer MAC statistics for OID\_WDI\_GET\_STATISTICS.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 47ABF170-76D7-4F17-BA92-56E1FEFF729D
keywords: ["WDI_TLV_MAC_STATISTICS Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_MAC_STATISTICS
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_MAC\_STATISTICS


WDI\_TLV\_MAC\_STATISTICS is a TLV that contains per-peer MAC statistics for [OID\_WDI\_GET\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/dn925850).

## TLV Type


0xA6

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>WDI_MAC_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926071)</td>
<td>The MAC address of the peer that these counts are set for. For multicast and broadcast packets, this value is set to FF-FF-FF-FF-FF-FF-FF.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the IEEE MAC layer of the 802.11 station successfully transmitted.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the IEEE MAC layer of the 802.11 station successfully received. This member should not be incremented for received packets that failed cipher decryption or MIC validation.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of unencrypted received MPDU frames that the MAC layer discarded when the IEEE 802.11 dot11ExcludeUnencrypted management information base (MIB) object is enabled.
<p>For more information about this MIB object, see [OID_DOT11_EXCLUDE_UNENCRYPTED](https://msdn.microsoft.com/library/windows/hardware/ff569365). MPDU frames are considered unencrypted when the Protected Frame subfield of the Frame Control field in the IEEE 802.11 MAC header is set to zero.</p></td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of received MSDU packets that the 802.11 station discarded because of MIC failures.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of received MPDU frames that the 802.11 station discarded because of the TKIP replay protection procedure.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of encrypted MPDU frames that the 802.11 station failed to decrypt because of a TKIP ICV error.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of received MPDU frames that the 802.11 discarded because of an invalid AES-CCMP format.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of received MPDU frames that the 802.11 station discarded because of the AES-CCMP replay protection procedure.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of received MPDU frames that the 802.11 station discarded because of errors detected by the AES-CCMP decryption algorithm.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of encrypted MPDU frames received for which a WEP decryption key was not available on the 802.11 station.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of encrypted MPDU frames that the 802.11 station failed to decrypt because of a WEP ICV error.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of received encrypted packets that the 802.11 station successfully decrypted.
<p>For the WEP and TKIP cipher algorithms, the port must increment this counter for each received encrypted MPDU that was successfully decrypted. For the AES-CCMP cipher algorithm, the port must increment this counter on each received encrypted MSDU packet that was successfully decrypted.</p></td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of encrypted packets that the 802.11 station failed to decrypt.
<p>For the WEP and TKIP cipher algorithms, the port must increment this counter for each received encrypted MPDU that was not successfully decrypted. For the AES-CCMP cipher algorithm, the port must increment this counter on each received encrypted MSDU packet that was not successfully decrypted. The port must not increment this counter for packets that are decrypted successfully, but are discarded for other reasons. For example, the port must not increment this counter for packets that are discarded because of TKIP MIC failures or TKIP/CCMP replays.</p></td>
</tr>
</tbody>
</table>

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_MAC_STATISTICS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




