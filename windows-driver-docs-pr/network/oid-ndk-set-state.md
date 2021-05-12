---
title: OID_NDK_SET_STATE
description: As a set request, NDIS and overlying drivers use the OID_NDK_SET_STATE OID to set the state of the miniport adapter's NDK functionality.
ms.date: 08/08/2017
keywords: 
 -OID_NDK_SET_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NDK\_SET\_STATE


As a set request, NDIS and overlying drivers use the OID\_NDK\_SET\_STATE OID to set the state of the miniport adapter's NDK functionality.

NDIS 6.30 and later miniport drivers that provide NDK services must support this OID. Otherwise, this OID is optional.

## Remarks

NDIS issues this OID with the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure pointing to a **BOOLEAN** and **InformationBufferLength** member equal to sizeof(**BOOLEAN**).

-   If the **BOOLEAN** value is **TRUE** and the **\*NetworkDirect** keyword value is nonzero, the miniport adapter's NDK functionality must be enabled.

    The miniport driver can read the **\*NetworkDirect** keyword value by doing the following:

    1.  Call [**NdisOpenConfigurationEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenconfigurationex) with the NDIS handle that the [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function returned when the miniport driver was initialized. For more information about calling **NdisOpenConfigurationEx**, see [Reading the Registry in an NDIS 6.0 Miniport Driver](/previous-versions/windows/hardware/network/reading-the-registry-in-an-ndis-6-0-miniport-driver).

    2.  Call [**NdisReadConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadconfiguration), passing:

        -   "\*NetworkDirect" for the *Keyword* parameter

        -   **NdisParameterInteger** for the *ParameterType* parameter

-   If the **BOOLEAN** value is **FALSE**, the NDK functionality of the miniport adapter must be disabled.

To enable or disable its NDK functionality, the miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) callback function should follow the steps in [Enabling and Disabling NDK Functionality](./enabling-and-disabling-ndk-functionality.md).

**Note**  An NDK-capable miniport driver must never call [**NdisMNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent) from the context of its [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function, because doing so could cause a deadlock. Instead, it should call **NdisMNetPnPEvent** from some other context or queue a work item.

 

An NDK-capable miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function must return **STATUS\_SUCCESS** for an OID\_NDK\_SET\_STATE OID request unless a failure occurs. The driver must not return **NDIS\_STATUS\_PENDING**.

## Requirements

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


[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NdisMNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent)

[**NdisQueueIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisqueueioworkitem)

[**NdisReadConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadconfiguration)

[**NDK\_ADAPTER**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_adapter)

[OID\_NDK\_SET\_STATE](oid-ndk-set-state.md)

 

