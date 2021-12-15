---
title: Status Indications in an Intermediate Driver
description: Status Indications in an Intermediate Driver
keywords:
- intermediate drivers WDK networking , status indications
- NDIS intermediate drivers WDK , status indications
- status indications WDK networking , intermediate drivers
ms.date: 04/20/2017
---

# Status Indications in an Intermediate Driver





The implementation of status indications in intermediate drivers is nearly identical to the implementation in protocol drivers. For more information about intermediate driver status indications, see [Status Indications in a Protocol Driver](status-indications-in-a-protocol-driver.md).

When an intermediate driver receives a status indication, it can indicate the status indication up to the higher-level drivers by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex). An intermediate driver should indicate status changes to overlying drivers as appropriate for its specific design requirements.

 

