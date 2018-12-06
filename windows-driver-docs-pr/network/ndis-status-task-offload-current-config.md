---
title: NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG
description: Miniport drivers use the NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG status indication to notify NDIS and overlying drivers that there has been a change in the task offload configuration of a NIC.
ms.assetid: 8a098dff-409e-4168-a3aa-372851aa999d
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG


Miniport drivers use the **NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG** status indication to notify NDIS and overlying drivers that there has been a change in the task offload configuration of a NIC.

Remarks
-------

Miniport drivers must report the current capabilities with the **NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG** status indication when current capabilities change. This status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information. Miniport drivers are required to issue this status indication in the following cases:

1.  When a miniport driver receives an [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) set request, it must use the contents of the [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure to update the currently-enabled task offload capabilities.
2.  When a miniport driver receives an [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) set request, it must use the contents of the [**NDIS\_OFFLOAD\_ENCAPSULATION**](https://msdn.microsoft.com/library/windows/hardware/ff566702) structure to update the currently-enabled task offload capabilities.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains an [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure. When issuing the **NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG** status indication, a miniport driver must use the **NDIS\_OFFLOAD** structure to report the current task offload configuration of the NIC.

**Note**  The contents of the [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure reflect only the NIC's current task offload configuration, not its actual hardware capabilities.

 

For more information about the current task offload configuration, see [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805).

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

[**NDIS\_OFFLOAD\_ENCAPSULATION**](https://msdn.microsoft.com/library/windows/hardware/ff566702)

[**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_STATUS\_TASK\_OFFLOAD\_HARDWARE\_CAPABILITIES**](ndis-status-task-offload-hardware-capabilities.md)

[OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762)

[OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805)

[OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807)

 

 




