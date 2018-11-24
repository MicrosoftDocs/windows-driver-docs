---
title: Indicating Miniport Driver Status
description: Indicating Miniport Driver Status
ms.assetid: 366caecb-6c4b-42f3-927d-b72db764d6cf
keywords:
- status information WDK CoNDIS
- connection-oriented NDIS WDK , miniport drivers
- CoNDIS WDK networking , miniport drivers
- miniport drivers WDK networking , CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Miniport Driver Status





Miniport drivers provide status indications to overlying drivers. The CoNDIS status indication functions are similar to the connectionless status indication functions.

To report a change in the status of a connection-oriented NIC or a change in the status of a particular VC active on the NIC, a connection-oriented miniport driver calls [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562). If the miniport driver is reporting a change in the status of a particular VC, it supplies an *NdisVcHandle* that identifies the VC.

This section includes the following topics:

[CoNDIS Miniport Driver Status Indications](condis-miniport-driver-status-indications.md)

[Handling Status Indications in a CoNDIS Protocol Driver](handling-status-indications-in-a-condis-protocol-driver.md)

 

 





