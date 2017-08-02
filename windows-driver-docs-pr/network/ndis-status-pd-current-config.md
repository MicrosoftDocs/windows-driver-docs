---
title: NDIS_STATUS_PD_CURRENT_CONFIG
author: windows-driver-content
description: This status indication is a notification that the NDIS_PD_CONFIG structure has changed.
ms.assetid: 0B63E85E-36A8-4DC4-A060-C40DCB6BE454
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_PD_CURRENT_CONFIG Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_PD_CURRENT_CONFIG%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


