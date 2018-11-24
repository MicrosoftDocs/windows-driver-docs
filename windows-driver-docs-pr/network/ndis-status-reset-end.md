---
title: NDIS_STATUS_RESET_END
description: The NDIS_STATUS_RESET_END status indicates that a miniport adapter reset operation is complete.
ms.assetid: 09ced263-9e4b-45e3-ae5e-db033a03b5b6
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_RESET_END Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_RESET\_END


The NDIS\_STATUS\_RESET\_END status indicates that a miniport adapter reset operation is complete.

Remarks
-------

Miniport drivers should not call the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function to signal the start and finish of each reset operation because NDIS notifies overlying drivers when a reset operation begins and ends.

When a miniport driver starts a reset operation, NDIS notifies the overlying drivers with an [**NDIS\_STATUS\_RESET\_START**](ndis-status-reset-start.md) status indication.

After a bound protocol driver receives an NDIS\_STATUS\_RESET\_END status indication, the protocol driver can resume sending data and making OID requests.

After an overlying filter or intermediate driver receives an NDIS\_STATUS\_RESET\_END status indication, the driver can resume sending data and making OID requests to overlying drivers.

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
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_RESET\_START**](ndis-status-reset-start.md)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

 

 




