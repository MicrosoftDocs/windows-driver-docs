---
title: OID_WDI_TCP_RSC_STATISTICS
ms.topic: reference
description: OID_WDI_TCP_RSC_STATISTICS is a get command that queries the RSC statistics of the hardware.
ms.date: 03/02/2023
keywords:
 - OID_WDI_TCP_RSC_STATISTICS Network Drivers Starting with Windows Vista
---

# OID\_WDI\_TCP\_RSC\_STATISTICS


OID\_WDI\_TCP\_RSC\_STATISTICS is a get command that queries the RSC statistics of the hardware.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                                                              | Multiple TLV instances allowed | Optional | Description                         |
|--------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------|
| [**WDI\_TLV\_TCP\_RSC\_STATISTICS\_PARAMETERS**](./wdi-tlv-tcp-rsc-statistics-parameters.md) |                                |          | TCP RSC statistics of the hardware. |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

