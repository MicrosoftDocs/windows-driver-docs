---
title: WDI_TLV_TCP_OFFLOAD_CAPABILITIES
description: WDI_TLV_TCP_OFFLOAD_CAPABILITIES is a TLV that contains TCP/IP offload capabilities.
ms.assetid: 9B3428CC-C9B4-4769-BD97-F25920C4AAF2
ms.date: 07/18/2017
keywords:
 - WDI_TLV_TCP_OFFLOAD_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_TCP\_OFFLOAD\_CAPABILITIES


WDI\_TLV\_TCP\_OFFLOAD\_CAPABILITIES is a TLV that contains TCP/IP offload capabilities.

Capability values are reported as documented in [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567878). Use NDIS\_OFFLOAD\_NOT\_SUPPORTED and NDIS\_OFFLOAD\_SUPPORTED when indicating capabilities through [OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/dn925838). For a connection with FIPS mode, offloads are turned OFF by the UE.

## TLV Type


0xCA

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                        | Multiple TLV instances allowed | Optional | Description                         |
|-------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------|
| [**WDI\_TLV\_CHECKSUM\_OFFLOAD\_CAPABILITIES**](wdi-tlv-checksum-offload-capabilities.md)                  |                                |          | Checksum offload capabilities.      |
| [**WDI\_TLV\_LSO\_V1\_CAPABILITIES**](wdi-tlv-lso-v1-capabilities.md)                                      |                                |          | Large Send Offload V1 capabilities. |
| [**WDI\_TLV\_LSO\_V2\_CAPABILITIES**](wdi-tlv-lso-v2-capabilities.md)                                      |                                |          | Large Send Offload V2 capabilities. |
| [**WDI\_TLV\_RECEIVE\_COALESCE\_OFFLOAD\_CAPABILITIES**](wdi-tlv-receive-coalesce-offload-capabilities.md) |                                |          | Receive Offload capabilities.       |
| [**WDI_TLV_OFFLOAD_SCOPE**](wdi-tlv-offload-scope.md) |   |   | Indicates whether offloads apply to the STA port only or on all ports. Currently applicable to 802.11ad adapters only. |

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

 

 




