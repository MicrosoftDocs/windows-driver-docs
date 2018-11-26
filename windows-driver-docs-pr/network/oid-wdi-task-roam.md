---
title: OID_WDI_TASK_ROAM
description: OID_WDI_TASK_ROAM requests that the adapter tries to roam from the currently connected AP to a new one.
ms.assetid: 22976d21-9212-4915-ab7a-fcc15d228db1
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_ROAM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_ROAM


OID\_WDI\_TASK\_ROAM requests that the adapter tries to roam from the currently connected AP to a new one.

| Object | Abort capable                                                               | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|-----------------------------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. If aborted after disassociation, it must be followed by a dot11 reset. | 4                                     | 10                              |

 

The Microsoft component provides the list of preferred BSS entries that the adapter should consider for roaming.

When this command issued, if its currently associated, the adapter would need to disassociate from the currently connected AP and then roam to the new AP. In this case it would first indicate disassociation for the old AP, then indicate association result for the new AP and then complete the task.

It can also determine not to perform the roam and stay connected to the current AP. In this case it would only complete the task without any association or disassociation indications.

The scan and AP selection requirements for this task are same as for [OID\_WDI\_TASK\_CONNECT](oid-wdi-task-connect.md).

## Task parameters


| TLV                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_CONNECT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926266) |                                |          | Connection parameters.                                                                                                                                                                                                                                                                                                                                                                                              |
| [**WDI\_TLV\_CONNECT\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn926264)  | X                              |          | The preferred list of candidate connect BSS entries. The port should attempt to connect to these BSS entries until the list is exhausted, or the connection completed successfully. The port can reprioritize the entries if needed. If the adapter has set the Connect BSS Selection Override bit, then it can pick a BSS that is not in this list as long as it follows the Allowed/Disallowed list requirements. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_ROAM\_COMPLETE](ndis-status-wdi-indication-roam-complete.md)
## Unsolicited indications


[NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT](ndis-status-wdi-indication-association-result.md)
[NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION](ndis-status-wdi-indication-disassociation.md)
[NDIS\_STATUS\_WDI\_INDICATION\_FT\_ASSOC\_PARAMS\_NEEDED](ndis-status-wdi-indication-ft-assoc-params-needed.md)
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

 

 




