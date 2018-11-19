---
title: OID_WDI_SET_ENCAPSULATION_OFFLOAD
description: OID_WDI_SET_ENCAPSULATION_OFFLOAD is sent by the OS to indicate that the lower edge driver (LE) should start doing the TCP Checksum/LSO offloads.
ms.assetid: 1095DBE0-2C6B-40F4-8E01-39F4BBA2FDBC
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_ENCAPSULATION_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_ENCAPSULATION\_OFFLOAD


OID\_WDI\_SET\_ENCAPSULATION\_OFFLOAD is sent by the OS to indicate that the lower edge driver (LE) should start doing the TCP Checksum/LSO offloads.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

When this message is received, the LE should indicate its current encapsulation offload configuration with [NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG](ndis-status-wdi-indication-task-offload-current-config.md). For receive operations, the LE should not start the checksum offload until after it receives the OID\_WDI\_SET\_ENCAPSULATION\_OFFLOAD message.

## Set property parameters


| TLV                                                                                                                   | Multiple TLV instances allowed | Optional | Description                                     |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------|
| [**WDI\_TLV\_SET\_ENCAPSULATION\_OFFLOAD\_V4\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898058) |                                |          | Specifies if IPv4 offloading should be started. |
| [**WDI\_TLV\_SET\_ENCAPSULATION\_OFFLOAD\_V6\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898059) |                                |          | Specifies if IPv6 offloading should be started. |

 

## Set property results


No additional data. The data in the header is sufficient.
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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




