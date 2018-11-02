---
title: NDIS Processing of Plug and Play Events
description: NDIS Processing of Plug and Play Events
ms.assetid: 3e9ae945-4241-4c66-bdb1-b9e3466167be
keywords:
- Plug and Play WDK NDIS miniport , IRP processing for NIC
- IRP processing for NIC WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Processing of Plug and Play Events





The [function drivers](https://msdn.microsoft.com/library/windows/hardware/ff546516) for a network interface card (NIC) are implemented as an NDIS and miniport driver pair. When a NIC is added to the system, NDIS creates the functional device object (FDO) for the NIC. NDIS then subsequently handles all IRPs, including Plug and Play (PnP) and power management IRPs, that are passed to this FDO. The miniport driver for the NIC provides the operational interface for the NIC.\`

The following sections describe how NDIS processes PnP IRPs on behalf of a NIC:

[Adding a NIC](adding-a-nic.md)

[Starting a NIC](starting-a-nic.md)

[Stopping a NIC](stopping-a-nic.md)

[Removing a NIC](removing-a-nic.md)

[Processing the Surprise Removal of a NIC](processing-the-surprise-removal-of-a-nic.md)

 

 





