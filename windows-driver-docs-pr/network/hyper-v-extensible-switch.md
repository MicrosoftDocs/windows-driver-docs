---
title: Hyper-V Extensible Switch
description: The Hyper-V extensible switch supports an interface that allows instances of NDIS filter drivers (known as extensible switch extensions) to bind within the extensible switch driver stack.
ms.assetid: FB6AA190-0DB1-441E-9BC6-2FD3A6D88114
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch


The Hyper-V extensible switch supports an interface that allows instances of NDIS filter drivers (known as *extensible switch extensions*) to bind within the extensible switch driver stack. After they are bound and enabled, extensions can monitor, modify, and forward packets to extensible switch ports. This also allows extensions to reject, redirect, or originate packets to ports that are used by the Hyper-V partitions.

The Hyper-V extensible switch is supported starting with NDIS 6.30 in Windows Server 2012.

This section includes the following topics that describe the Hyper-V extensible switch and its interface:

-   [Getting Started Writing a Hyper-V Extensible Switch Extension](getting-started-writing-a-hyper-v-extensible-switch-extension.md)
-   [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md)
-   [Hyper-V Extensible Switch Architecture](hyper-v-extensible-switch-architecture.md)
-   [Writing Hyper-V Extensible Switch Extensions](writing-hyper-v-extensible-switch-extensions.md)
-   [Installing Hyper-V Extensible Switch Extensions](installing-hyper-v-extensible-switch-extensions.md)
-   [Hyper-V Extensible Switch OIDs](hyper-v-extensible-switch-oids.md)

 

 





