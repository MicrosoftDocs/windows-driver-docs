---
title: OID_WDI_SET_TCP_OFFLOAD_PARAMETERS
description: OID_WDI_SET_TCP_OFFLOAD_PARAMETERS is sent down to the device from the OS to set the TCP offload parameters.
ms.assetid: B615066B-3871-4445-8397-B41CB66EEF35
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_TCP_OFFLOAD_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS


OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS is sent down to the device from the OS to set the TCP offload parameters.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

This command is sent in some cases such as when there is a need to turn off the offloads due to a performance issue.

The lower edge driver (LE) must use the contents of [**WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898071) to update the currently reported TCP offload capabilities. After the update, the LE must report the current task offload capabilities with [NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG](ndis-status-wdi-indication-task-offload-current-config.md). This status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information.

## Set property parameters


| TLV                                                                                        | Multiple TLV instances allowed | Optional | Description                           |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------|
| [**WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898071) |                                |          | The TCP offload parameters to be set. |

 

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

 

 




