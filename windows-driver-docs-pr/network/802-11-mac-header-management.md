---
title: 802.11 MAC Header Management
description: 802.11 MAC Header Management
ms.assetid: 20bf0527-35ef-4c61-92d8-042391cb0203
keywords:
- headers WDK Native 802.11
- MAC headers WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# 802.11 MAC Header Management


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Each packet sent by the 802.11 station through calls to the [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function begins with an 802.11 MAC header.

For more information about the format of the 802.11 MAC header, refer to Clause 8.2.1 of the [IEEE 802.11-2012 standard](http://standards.ieee.org/getieee802/download/802.11-2012.pdf).

The following table describes which fields and subfields within the 802.11 MAC header are set by the operating system or 802.11 station.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field name</th>
<th align="left">Subfield name</th>
<th align="left">Set by operating system</th>
<th align="left">Set by 802.11 station</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>Protocol Version</p></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>Type</p></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>Subtype</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="even">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>To DS</p></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>From DS</p></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>More Fragments</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>Retry</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="even">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>Pwr Mgt</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>More Data</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="even">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>Protected Frame</p></td>
<td align="left"></td>
<td align="left"><p>X</p>
†</td>
</tr>
<tr class="odd">
<td align="left"><p>Frame Control</p></td>
<td align="left"><p>Order</p></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Duration/ID</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Address 1</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Address 2</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Address 3</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Sequence Control</p></td>
<td align="left"><p>Fragment Number</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Sequence Control</p></td>
<td align="left"><p>Sequence Number</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address 4</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

**Note**  The following notes apply to the preceding table:
†When operating in safe-mode, miniport drivers should not modify the Protected Frame bit.

 

The following points apply to the Subtype subfield of the 802.11 MAC header.

-   If the Type subfield is set to zero (management), the operating system will set the Subtype subfield. In this situation, the 802.11 station must not change the value of this subfield.

-   If the Type subfield is set to 2 (data), the operating system will set the Subtype subfield. However, the 802.11 station can change the value of this subfield if it is extending the MAC header to support fields not supported by the operating system.
    **Note**  If the original value of the Subtype subfield was 4 (null data) and the 802.11 station changes the subfield, the station must use an equivalent "null data" value.

     

The operating system uses the Address 4 field of the 802.11 MAC header under the following conditions:

-   The 802.11 station has connected to an infrastructure basic service set (BSS) network.

-   After associating with an access point (AP) in the BSS network, the miniport driver makes an [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319) indication with the **bFourAddressSupported** member of the DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS structure set to **TRUE**.

-   The From DS and To DS subfields in the MAC header are set to one.

The 802.11 station must update the MAC header to provide any fields from standards or proprietary protocols not supported by the operating system. For more information about this, see [Extending Packet Data During Send Operations](extending-packet-data-during-send-operations.md).

 

 





