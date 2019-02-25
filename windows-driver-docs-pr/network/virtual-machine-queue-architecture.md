---
title: Virtual Machine Queue Architecture
description: Virtual Machine Queue Architecture
ms.assetid: 7aa8c9a4-1bb2-48a5-be28-9806e16d4e94
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Machine Queue Architecture





The NDIS virtual machine queue (VMQ) architecture provides advantages for virtualization such as:

-   Virtualization impacts performance and VMQ helps overcome those effects.

-   VMQ supports live migration.

-   VMQ coexists with NDIS task offloads and other optimizations.

This section provides high-level information about the NDIS VMQ interface. You should read this section before writing an NDIS driver that supports VMQ. For information about writing VMQ drivers, see [Writing VMQ Drivers](writing-vmq-drivers.md).

This section includes the following topics:

[Introduction to NDIS Virtual Machine Queue (VMQ)](introduction-to-ndis-virtual-machine-queue--vmq-.md)

[Security Issues with NDIS Virtual Machine (VM) Shared Memory](security-issues-with-ndis-virtual-machine--vm--shared-memory.md)

[NDIS VMQ Live Migration Support](ndis-vmq-live-migration-support.md)

[NDIS VM Queue States](ndis-virtual-machine-queue-states.md)

 

 





