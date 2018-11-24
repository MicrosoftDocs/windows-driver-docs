---
title: Handling an OID_PNP_SET_POWER OID
description: Handling an OID_PNP_SET_POWER OID
ms.assetid: 6140c772-57ba-47d3-b294-a2e2b2e3ccc7
keywords:
- OID_PNP_SET_POWER_OID
- network interface cards WDK networking , transitioning power states
- network adapters WDK networking , transitioning power states
- power management WDK NDIS miniport , transitioning power states
- device power states WDK networking
- power states WDK networking
- transitioning power states WDK networking
- wake-up capabilities WDK networking , transitioning power states
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling an OID\_PNP\_SET\_POWER OID





NDIS sends an OID request of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) to notify a miniport driver that a network adapter will be making a transition from the working state to a sleeping state or from a sleeping state to the working state. An OID\_PNP\_SET\_POWER request can be preceded by an [OID\_PNP\_QUERY\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569778) request.

This section includes:

[Transitioning to a Sleeping State](transitioning-to-a-sleeping-state.md)

[Transitioning to the Working State](transitioning-to-the-working-state.md)

 

 





