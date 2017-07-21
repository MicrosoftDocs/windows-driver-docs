---
title: NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG
author: windows-driver-content
description: Miniport drivers use the NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG status indication to notify NDIS and overlying drivers that there has been a change in the task offload configuration of a NIC.
ms.assetid: 8a098dff-409e-4168-a3aa-372851aa999d
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


