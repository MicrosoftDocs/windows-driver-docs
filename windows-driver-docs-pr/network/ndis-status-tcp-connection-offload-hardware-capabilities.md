---
title: NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES
description: MUX intermediate drivers use the NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES CAPABILITIES status indication to notify NDIS and overlying drivers that there has been change in the connection offload characteristics of the underlying hardware.
ms.assetid: 694cc0c4-0987-4095-8490-14ddfc9eaedb
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES


MUX intermediate drivers use the NDIS\_STATUS\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES CAPABILITIES status indication to notify NDIS and overlying drivers that there has been change in the connection offload characteristics of the underlying hardware.

Remarks
-------

If an underlying NIC is added or deleted, the overall set of hardware capabilities that is associated with a MUX intermediate driver can change.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains an [**NDIS\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567875) structure. NDIS\_TCP\_CONNECTION\_OFFLOAD specifies the task offload hardware capabilities.

For more information about task offload hardware capabilities, see [OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803).

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


[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567875)

[OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803)

 

 




