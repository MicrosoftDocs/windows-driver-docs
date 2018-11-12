---
title: Intermediate Driver Binding Operations
description: Intermediate Driver Binding Operations
ms.assetid: 129a744c-d4d4-4741-9812-e76087c585fc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver Binding Operations





When a miniport adapter becomes available, NDIS calls the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function of any intermediate driver that can bind to that miniport adapter.

An intermediate driver must provide the protocol binding operations documented in [Binding to an Adapter](binding-to-an-adapter.md).

Binding-time actions include allocating and initializing an adapter-specific context area for the binding, initializing any virtual miniports, and calling [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) to bind to the adapter.

Intermediate drivers are not required to allocate separate [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure pools for each binding. Intermediate drivers are required to allocate NET\_BUFFER\_LIST structure pools only if the drivers design requires it to allocate its own structures. Otherwise, the driver can just pass on the structures that it receives from other drivers. Such drivers should allocate different pools for send and receive.

For information about the requirements to allocate and manage network data, see [Intermediate Driver Network Data Management](intermediate-driver-network-data-management.md).

 

 





