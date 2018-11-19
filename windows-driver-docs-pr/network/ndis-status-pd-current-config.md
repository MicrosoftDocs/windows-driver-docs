---
title: NDIS_STATUS_PD_CURRENT_CONFIG
description: This status indication is a notification that the NDIS_PD_CONFIG structure has changed.
ms.assetid: 0B63E85E-36A8-4DC4-A060-C40DCB6BE454
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_PD_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_PD\_CURRENT\_CONFIG


This status indication is a notification that the [**NDIS\_PD\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/dn931835) structure has changed.

A PacketDirect-capable miniport driver must make an NDIS\_STATUS\_PD\_CURRENT\_CONFIG status indication after an [OID\_PD\_CLOSE\_PROVIDER](https://msdn.microsoft.com/library/windows/hardware/dn931851) or [OID\_PD\_OPEN\_PROVIDER](https://msdn.microsoft.com/library/windows/hardware/dn931852) request.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make the status indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the **NDIS\_STATUS\_INDICATION** structure:

-   **SourceHandle** must be set to the handle that the miniport received in the *MiniportAdapterHandle* parameter of the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

-   **StatusCode** must be set to NDIS\_STATUS\_PD\_CURRENT\_CONFIG.

-   **StatusBuffer** must be set to the address of a ULONG variable, which stores the appropriate NDIS\_STATUS\_xxxx code for the result of the scan operation.

-   **StatusBufferSize** must be set to **sizeof**(ULONG).

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

[OID\_PD\_CLOSE\_PROVIDER](https://msdn.microsoft.com/library/windows/hardware/dn931851)

[OID\_PD\_OPEN\_PROVIDER](https://msdn.microsoft.com/library/windows/hardware/dn931852)

 

 




