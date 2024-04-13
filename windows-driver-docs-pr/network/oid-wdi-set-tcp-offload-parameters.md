---
title: OID_WDI_SET_TCP_OFFLOAD_PARAMETERS
ms.topic: reference
description: OID_WDI_SET_TCP_OFFLOAD_PARAMETERS is sent down to the device from the OS to set the TCP offload parameters.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_TCP_OFFLOAD_PARAMETERS Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS


OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS is sent down to the device from the OS to set the TCP offload parameters.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

This command is sent in some cases such as when there is a need to turn off the offloads due to a performance issue.

The lower edge driver (LE) must use the contents of [**WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS**](./wdi-tlv-tcp-set-offload-parameters.md) to update the currently reported TCP offload capabilities. After the update, the LE must report the current task offload capabilities with [NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG](ndis-status-wdi-indication-task-offload-current-config.md). This status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information.

## Set property parameters


| TLV                                                                                        | Multiple TLV instances allowed | Optional | Description                           |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------|
| [**WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS**](./wdi-tlv-tcp-set-offload-parameters.md) |                                |          | The TCP offload parameters to be set. |

 

## Set property results


No additional data. The data in the header is sufficient.

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

 

