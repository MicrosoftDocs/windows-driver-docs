---
title: Power Management (NDIS 6.0 and NDIS 6.1)
description: Power Management (NDIS 6.0 and NDIS 6.1)
ms.assetid: 10CACB4E-BBC8-497F-9B54-810518B726A8
keywords:
- miniport drivers WDK networking , power management
- NDIS miniport drivers WDK , power management
- power management WDK networking , miniport drivers
- power management WDK NDIS miniport
- power management WDK NDIS miniport , about miniport driver power management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Management (NDIS 6.0 and NDIS 6.1)





This section describes the NDIS power management interface that was introduced with Windows XP and NDIS 5.1. This power management interface is supported in the following versions of NDIS:

-   NDIS 5.1 (Windows XP)

-   NDIS 6.0 and later versions of NDIS (Windows Vista and later versions of Windows)

This section describes:

-   The power management services that NDIS provides for NDIS miniport drivers.

-   The miniport driver requirements for supporting power management.

-   How NDIS sets the power policy for a network adapter.

This section includes the following topics:

[Required and Optional OIDs for Power Management](required-and-optional-oids-for-power-management.md)

[Device Power States for Network Adapters](device-power-states-for-network-adapters.md)

[Network Wake-Up Events](network-wake-up-events.md)

[Handling an OID\_PNP\_QUERY\_POWER OID](handling-an-oid-pnp-query-power-oid.md)

[Handling an OID\_PNP\_SET\_POWER OID](handling-an-oid-pnp-set-power-oid.md)

[Power Management Considerations for Gigabit Ethernet Network Adapters](power-management-considerations-for-gigabit-ethernet-network-adapters.md)

[Power Management for Old Miniport Drivers](power-management-for-old-miniport-drivers.md)

[How NDIS Sets the Power Policy for a Network Adapter](how-ndis-sets-the-power-policy-for-a-network-adapter.md)

[Avoiding NDIS Power Management Problems](avoiding-ndis-power-management-problems.md)

**Note**  Starting with NDIS 6.20, the NDIS power management interface has been revised and extended. If you are developing NDIS 6.20 miniport drivers that support power management, please review the information in [Power Management (NDIS 6.20 and Later)](https://msdn.microsoft.com/library/windows/hardware/hh205401). If you are developing NDIS 6.30 miniport drivers that support power management, please review the information in [Power Management (NDIS 6.30 and Later)](https://msdn.microsoft.com/library/windows/hardware/hh440160).

 

 

 





