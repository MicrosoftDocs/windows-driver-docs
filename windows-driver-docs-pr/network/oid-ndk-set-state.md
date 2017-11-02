---
title: OID_NDK_SET_STATE
author: windows-driver-content
description: As a set request, NDIS and overlying drivers use the OID_NDK_SET_STATE OID to set the state of the miniport adapter's NDK functionality.
ms.assetid: 5BA49F42-FE37-4860-B68F-92A7F4007639
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_NDK_SET_STATE Network Drivers Starting with Windows Vista
---

# OID\_NDK\_SET\_STATE


As a set request, NDIS and overlying drivers use the OID\_NDK\_SET\_STATE OID to set the state of the miniport adapter's NDK functionality.

NDIS 6.30 and later miniport drivers that provide NDK services must support this OID. Otherwise, this OID is optional.

Remarks
-------

NDIS issues this OID with the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure pointing to a **BOOLEAN** and **InformationBufferLength** member equal to sizeof(**BOOLEAN**).

-   If the **BOOLEAN** value is **TRUE** and the **\*NetworkDirect** keyword value is nonzero, the miniport adapter's NDK functionality must be enabled.

    The miniport driver can read the **\*NetworkDirect** keyword value by doing the following:

    1.  Call [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) with the NDIS handle that the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function returned when the miniport driver was initialized. For more information about calling **NdisOpenConfigurationEx**, see [Reading the Registry in an NDIS 6.0 Miniport Driver](https://msdn.microsoft.com/library/windows/hardware/ff570429).

    2.  Call [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511), passing:

        -   "\*NetworkDirect" for the *Keyword* parameter

        -   **NdisParameterInteger** for the *ParameterType* parameter

-   If the **BOOLEAN** value is **FALSE**, the NDK functionality of the miniport adapter must be disabled.

To enable or disable its NDK functionality, the miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) callback function should follow the steps in [Enabling and Disabling NDK Functionality](https://msdn.microsoft.com/library/windows/hardware/dn163547).

**Note**  An NDK-capable miniport driver must never call [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) from the context of its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function, because doing so could cause a deadlock. Instead, it should call **NdisMNetPnPEvent** from some other context or queue a work item.

 

An NDK-capable miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function must return **STATUS\_SUCCESS** for an OID\_NDK\_SET\_STATE OID request unless a failure occurs. The driver must not return **NDIS\_STATUS\_PENDING**.

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
<td><p>None supported</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616)

[**NdisQueueIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff563775)

[**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511)

[**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848)

[OID\_NDK\_SET\_STATE](oid-ndk-set-state.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_NDK_SET_STATE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


