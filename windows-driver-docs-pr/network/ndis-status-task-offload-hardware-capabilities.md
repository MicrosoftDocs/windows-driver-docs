---
title: NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES
author: windows-driver-content
description: NDIS miniport drivers and MUX intermediate drivers use the NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES status indication to notify NDIS and overlying drivers that there has been change in the task offload hardware capabilities of the underlying NIC.
ms.assetid: 9ac8f4c9-66f4-4889-932b-a51381c54734
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


