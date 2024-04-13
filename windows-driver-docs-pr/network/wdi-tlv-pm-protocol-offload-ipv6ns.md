---
title: WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv6NS
ms.topic: reference
description: WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv6NS is a TLV that contains IPv6 NS protocol offload parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv6NS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS is a TLV that contains IPv6 NS protocol offload parameters.

## TLV Type


0x62

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32                                            | Specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter.                                                                                                    |
| UINT8\[16\]                                       | Specifies an optional IPv6 address to match with the Source Address field in the IPv6 header of the NS message. If the incoming NS message has a Source Address value that matches this IPv6 address, the network adapter sends a neighbor advertisement (NA) message when it is in a low power state. If this is set to zero, the network adapter should respond to NS messages from any remote IPv6 address. |
| UINT8\[16\]                                       | Specifies the solicited node IPv6 address.                                                                                                                                                                                                                                                                                                                                                                     |
| UINT8\[16\]                                       | Specifies one or two IPv6 addresses to match the Target Address field of an incoming NS message. If there is only one address, that address is stored in Target address 1, and Target address 2 is filled with zeros. If one of these addresses matches the Target Address field of an incoming NS message, the network adapter sends an NA message in response.                                               |
| UINT8\[16\]                                       | See description of Target address 1.                                                                                                                                                                                                                                                                                                                                                                           |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | Specifies the MAC address that the network adapter must use for the target link-layer address (TLLA) field of the NA message that it generates. However, it should use the current MAC address of the network adapter as the source address in the MAC header.                                                                                                                                                 |

 

## Requirements

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

 

