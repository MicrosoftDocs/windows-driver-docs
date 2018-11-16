---
title: NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES
description: NDIS miniport drivers and MUX intermediate drivers use the NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES status indication to notify NDIS and overlying drivers that there has been change in the task offload hardware capabilities of the underlying NIC.
ms.assetid: 9ac8f4c9-66f4-4889-932b-a51381c54734
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_TASK\_OFFLOAD\_HARDWARE\_CAPABILITIES


NDIS miniport drivers and MUX intermediate drivers use the **NDIS\_STATUS\_TASK\_OFFLOAD\_HARDWARE\_CAPABILITIES** status indication to notify NDIS and overlying drivers that there has been change in the task offload hardware capabilities of the underlying NIC.

Remarks
-------

If an underlying NIC is added or deleted, the overall set of hardware capabilities that is associated with a miniport driver or MUX intermediate driver can change. For example, if a miniport driver issues the **NDIS\_STATUS\_TASK\_OFFLOAD\_HARDWARE\_CAPABILITIES** status indication, specifying that it cannot support Large Send Offload (LSO), the NIC can no longer be configured to support LSO.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains an [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure. This structure specifies the task offload hardware capabilities.

For more information about task offload hardware capabilities, see [OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569806).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](ndis-status-task-offload-current-config.md)

[OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569806)

 

 




