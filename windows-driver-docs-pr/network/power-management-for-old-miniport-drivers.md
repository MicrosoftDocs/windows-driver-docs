---
title: Power Management for Old Miniport Drivers
description: Power Management for Old Miniport Drivers
ms.assetid: 676c8c4c-3fd7-4063-a704-2bbfdd03a94e
keywords:
- power management WDK NDIS miniport , old miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Management for Old Miniport Drivers





NDIS treats a miniport driver as an old miniport driver that is not power management-aware if:

-   During initialization, the bus driver indicates that the system or the NIC is not power management-aware.

-   The miniport driver returns NDIS\_STATUS\_UNSUPPORTED in response to the [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774) query. Only NDIS 5.1 and earlier miniport drivers or intermediate drivers receive this OID query.

-   The user disables power management in the user interface.

NDIS supports only two device power states for old miniport drivers that do not support power manegement: the highest-powered (D0) state and the D3 state.

During initialization, an old miniport driver can indicate that NDIS should not halt it before the system transitions to the sleeping (D3) state. A miniport driver makes such an indication by setting the NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND flag in the *AttributeFlags* parameter that the miniport driver passes to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function. An old miniport driver should set this flag only if it can:

-   Save all hardware context that it might require.

-   Put a NIC in an appropriate state for the sleeping state (D3).

-   Reactivate the NIC to the highest-powered state (D0).

If NDIS determines from the bus driver that the NIC is not power management-aware and if the miniport driver did not set the NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND flag, NDIS will not query the miniport driver's power management capabilities. However, if the miniport driver set the NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND flag, NDIS issues an [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774) request to the miniport driver. In this case, the miniport driver should succeed the OID\_PNP\_CAPABILITIES request with NDIS\_STATUS\_SUCCESS. In the NDIS\_PM\_WAKE\_UP\_CAPABILITIES structure that the miniport driver returns in response to this request, the miniport driver must also specify a device power state of **NdisDeviceStateUnspecified** for each wake-up capability.

NDIS provides the following power management support for old miniport drivers:

-   NDIS succeeds all [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) requests that the system power manager sends to the device object that represents the NIC. That is, NDIS guarantees that the miniport driver's NIC will transition to the D3 state in response to any IRP\_MN\_QUERY\_POWER request from the system.

-   If the miniport driver did not set the NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND flag during initialization, NDIS calls the miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function before the miniport driver's NIC transitions to state D3. The miniport driver's NIC loses all hardware context information.

-   If the miniport driver set the NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND flag during initialization, NDIS does not halt the miniport driver before the system transitions to state D3. Instead, NDIS issues the miniport driver an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request to D3 state. The miniport driver must save any hardware context that it uses and put a NIC in a state appropriate for the D3 state.

-   While the system is transitioning to the S0 [system power states](https://msdn.microsoft.com/library/windows/hardware/ff564571), NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function if NDIS halted the miniport driver. If NDIS did not halt the miniport driver, NDIS issues the miniport driver an OID\_PNP\_SET\_POWER request to D0 state. The miniport driver must put a NIC in a state appropriate for the D0 state.

-   If the miniport driver was halted and reinitialized, NDIS restores all the appropriate miniport driver settings, such as packet filters and multicast address lists, by issuing OID requests. If the miniport driver was not halted and then reinitialized, the miniport driver must restore such settings.

 

 





