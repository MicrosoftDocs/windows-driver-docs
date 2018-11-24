---
title: Status Indications in an Intermediate Driver
description: Status Indications in an Intermediate Driver
ms.assetid: be8d50f9-4a8d-4f3c-a507-e64dedff9a3e
keywords:
- intermediate drivers WDK networking , status indications
- NDIS intermediate drivers WDK , status indications
- status indications WDK networking , intermediate drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Status Indications in an Intermediate Driver





The implementation of status indications in intermediate drivers is nearly identical to the implementation in protocol drivers. For more information about intermediate driver status indications, see [Status Indications in a Protocol Driver](status-indications-in-a-protocol-driver.md).

When an intermediate driver receives a status indication, it can indicate the status indication up to the higher-level drivers by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). An intermediate driver should indicate status changes to overlying drivers as appropriate for its specific design requirements.

 

 





