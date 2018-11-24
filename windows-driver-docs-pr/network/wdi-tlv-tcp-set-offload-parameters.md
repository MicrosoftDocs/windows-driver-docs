---
title: WDI_TLV_TCP_SET_OFFLOAD_PARAMETERS
description: WDI_TLV_TCP_SET_OFFLOAD_PARAMETERS is a TLV that contains TCP offload capabilities of a miniport adapter for OID_WDI_SET_TCP_OFFLOAD_PARAMETERS.
ms.assetid: 1DE1114A-E718-473F-B0EB-92AEFA4E7F13
ms.date: 07/18/2017
keywords:
 - WDI_TLV_TCP_SET_OFFLOAD_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS


WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS is a TLV that contains TCP offload capabilities of a miniport adapter for [OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/dn925945).

## TLV Type


0xF2

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
<td>UINT8</td>
<td>The IPv4 checksum setting of the miniport adapter.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_DISABLED</strong> - Disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_ENABLED_RX_DISABLED</strong> - Enabled for transmit and disabled for receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RX_ENABLED_TX_DISABLED</strong> - Enabled for receive and disabled for transmit.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_ENABLED</strong> - Enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The IPv4 checksum setting for TCP packets.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_DISABLED</strong> - Disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_ENABLED_RX_DISABLED</strong> - Enabled for transmit and disabled for receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RX_ENABLED_TX_DISABLED</strong> - Enabled for receive and disabled for transmit.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_ENABLED</strong> - Enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The IPv4 checksum setting for UDP packets.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_DISABLED</strong> - Disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_ENABLED_RX_DISABLED</strong> - Enabled for transmit and disabled for receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RX_ENABLED_TX_DISABLED</strong> - Enabled for receive and disabled for transmit.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_ENABLED</strong> - Enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The IPv6 checksum setting for TCP packets.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_DISABLED</strong> - Disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_ENABLED_RX_DISABLED</strong> - Enabled for transmit and disabled for receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RX_ENABLED_TX_DISABLED</strong> - Enabled for receive and disabled for transmit.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_ENABLED</strong> - Enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The IPv6 checksum setting for UDP packets.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_DISABLED</strong> - Disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_ENABLED_RX_DISABLED</strong> - Enabled for transmit and disabled for receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RX_ENABLED_TX_DISABLED</strong> - Enabled for receive and disabled for transmit.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_TX_RX_ENABLED</strong> - Enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The Large Send Offload version 1 (LSOV1) setting.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_LSOV1_ENABLED</strong> - LSOV1 is enabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_LSOV1_DISABLED</strong> - LSOV1 is disabled.</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The Internet Protocol Security (IPsec) offload setting.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV1_DISABLED</strong> - IPsec offload is disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV1_AH_ENABLED</strong> - The IPsec offload Authentication Header (AH) feature should be enabled for transmit and receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV1_ESP_ENABLED</strong> - The IPsec offload Encapsulating Security Payload (ESP) feature should be enabled for transmit and receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV1_AH_AND_ESP_ENABLED</strong> - The IPsec offload AH and ESP features are enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The IPv4 Large Send Offload version 2 (LSOV2) setting.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_LSOV2_ENABLED</strong> - LSOV2 for IPv4 is enabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_LSOV2_DISABLED</strong> - LSOV2 for IPv4 is disabled.</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The IPv6 Large Send Offload version 2 (LSOV2) setting.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_LSOV2_ENABLED</strong> - LSOV2 for IPv6 is enabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_LSOV2_DISABLED</strong> - LSOV2 for IPv6 is disabled.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The IPv4 connection offload setting.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The IPv6 connection offload setting.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Indicates Receive Segment Coalescing state for IPv4.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The RSC state is unchanged.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RSC_ENABLED</strong> - The RSC state is enabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RSC_DISABLED</strong> - The RSC state is disabled.</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Indicates Receive Segment Coalescing state for IPv6.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The RSC state is unchanged.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RSC_ENABLED</strong> - The RSC state is enabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_RSC_DISABLED</strong> - The RSC state is disabled.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The value is a bitwise OR of flags. This must be set to 0. There are no flags currently defined.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The Internet protocol security (IPsec) offload version 2 setting of a miniport adapter that supports both IPv6 and IPv4. This specifies the setting for both IPv6 and IPv4 support.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_DISABLED</strong> - IPsec offload version 2 is disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_ENABLED</strong> - The IPsec offload version 2 Authentication Header (AH) feature should be enabled for transmit and receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_ESP_ENABLED</strong> - The IPsec offload version 2 Encapsulating Security Payload (ESP) feature should be enabled for transmit and receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_AND_ESP_ENABLED</strong> - The IPsec offload version 2 AH and ESP features are enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The Internet protocol security (IPsec) offload version 2 setting of a miniport adapter that supports IPv4 and does not support IPv6. If the miniport driver supports IPv6, the IPsecV2 member specifies the IPv4 setting and this member is not used.
<p>Valid values are:</p>
<ul>
<li><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong> - The miniport driver should not change the current setting.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_DISABLED</strong> - IPsec offload version 2 is disabled.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_ENABLED</strong> - The IPsec offload version 2 Authentication Header (AH) feature should be enabled for transmit and receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_ESP_ENABLED</strong> - The IPsec offload version 2 Encapsulating Security Payload (ESP) feature should be enabled for transmit and receive.</li>
<li><strong>NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_AND_ESP_ENABLED</strong> - The IPsec offload version 2 AH and ESP features are enabled for transmit and receive.</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Encapsulated Packet Task Offload. A protocol driver sets this field to one of the following values.
<p></p>
<ul>
<li><strong>NDIS_OFFLOAD_SET_NO_CHANGE</strong> (0) - The NVGRE task offload state is unchanged.</li>
<li><strong>NDIS_OFFLOAD_SET_ON</strong> (1) - Enables NVGRE task offloads.</li>
<li><strong>NDIS_OFFLOAD_SET_OFF</strong> (2) - Disables NVGRE task offloads.</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Encapsulation types. This field is effective only when the Encapsulated Packet Task Offload is set to <strong>NDIS_OFFLOAD_SET_ON</strong>. If the Encapsulated Packet Task Offload member is not set to <strong>NDIS_OFFLOAD_SET_ON</strong>, this member is zero. A protocol driver must set Encapsulation Types to the bitwise OR of the flags corresponding to encapsulation types that it requires. It can select from the following flags.
<p></p>
<ul>
<li><strong>NDIS_ENCAPSULATION_TYPE_GRE_MAC</strong> (0x00000001) - Specifies GRE MAC encapsulation (NVGRE).</li>
</ul></td>
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

## See also


[**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706)

[OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/dn925945)

 

 




