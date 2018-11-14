---
title: Porting a Miniport Driver to NDIS 6.0
description: Porting a Miniport Driver to NDIS 6.0
ms.assetid: 1e4eea3a-dabe-4d4f-b65f-d9b968c4c58a
keywords:
- miniport drivers WDK networking , porting
- NDIS miniport drivers WDK , porting
- NDIS porting drivers WDK , miniport drivers
- porting drivers WDK networking , miniport drivers
- network driver porting WDK , miniport drivers
- porting miniport drivers WD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting a Miniport Driver to NDIS 6.0





This section describes what is required to port an NDIS 5.*x* miniport driver to NDIS 6.0. The most significant changes to the miniport driver are illustrated with code samples.

NDIS 6.0 retains backward compatibility with earlier NDIS versions. For more information about backward compatibility, see [NDIS 6.0 Backward Compatibility](ndis-6-0-backward-compatibility.md).

For a summary of NDIS 6.0 miniport driver porting issues, see [Summary of Changes Required to Port a Miniport Driver to NDIS 6.0](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-0.md).

This section also includes the following topics that describe porting a miniport driver to NDIS 6.0 in more detail:

[Porting Miniport Driver Initialization to NDIS 6.0](porting-miniport-driver-initialization-to-ndis-6-0.md)

[Porting Miniport Driver Unload Operations to NDIS 6.0](porting-miniport-driver-unload-operations-to-ndis-6-0.md)

[Porting Miniport Adapter Initialization to NDIS 6.0](porting-miniport-adapter-initialization-to-ndis-6-0.md)

[Porting Miniport Adapter Halt Operations to NDIS 6.0](porting-miniport-adapter-halt-operations-to-ndis-6-0.md)

[Supporting NDIS 6.0 Miniport Adapter Pause and Restart Operations](supporting-ndis-6-0-miniport-adapter-pause-and-restart-operations.md)

[Porting Miniport Driver Send and Receive Operations to NDIS 6.0](porting-miniport-driver-send-and-receive-operations-to-ndis-6-0.md)

[Porting Miniport Driver DMA operations to NDIS 6.0](porting-miniport-driver-dma-operations-to-ndis-6-0.md)

[Porting Miniport Driver Interrupt Operations to NDIS 6.0](porting-miniport-driver-interrupt-operations-to-ndis-6-0.md)

[Porting Miniport Driver OID Request Handling to NDIS 6.0](porting-miniport-driver-oid-request-handling-to-ndis-6-0.md)

[Porting Miniport Driver Status Indications to NDIS 6.0](porting-miniport-driver-status-indications-to-ndis-6-0.md)

[Porting Miniport Driver Plug and Play Event Notification Handling to NDIS 6.0](porting-miniport-driver-plug-and-play-event-notification-handling-to-n.md)

[Porting Miniport Adapter Check for Hang and Reset Operations to NDIS 6.0](porting-miniport-adapter-check-for-hang-and-reset-operations-to-ndis-6.md)

[Porting Miniport Adapter Shutdown Operations to NDIS 6.0](porting-miniport-adapter-shutdown-operations-to-ndis-6-0.md)

 

 





