---
title: General I/O Targets
description: General I/O Targets
ms.assetid: e5527aa2-a63f-49d8-aa9a-f91efd2ae9ad
keywords:
- general I/O targets WDK KMDF
- I/O targets WDK KMDF , general
- local I/O targets WDK KMDF
- remote I/O targets WDK KMDF
- general I/O targets WDK KMDF , about general I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General I/O Targets





General I/O targets do not support special, device-specific data formats, such as USB request blocks. Before drivers send data to a general I/O target, they must put data into a write buffer in a format that the I/O target can interpret. Likewise, when drivers read data from a general I/O target, the drivers must be able interpret the contents of data buffers that they receive from the target.

General I/O targets are either local or remote:

<a href="" id="local-i-o-targets"></a>Local I/O Targets  
Each framework-based function driver, filter driver, and miniport driver has a local I/O target for each of the driver's devices. A device's local I/O target is always the next-lower driver in the driver stack.

<a href="" id="remote-i-o-targets"></a>Remote I/O Targets  
Remote I/O targets represent the top of a different driver stack or (rarely) a different driver in the current driver's stack.

This section includes:

-   [Initializing a General I/O Target](initializing-a-general-i-o-target.md)

-   [Sending I/O Requests to General I/O Targets](sending-i-o-requests-to-general-i-o-targets.md)

-   [Controlling a General I/O Target's State](controlling-a-general-i-o-target-s-state.md)

-   [Obtaining Information About a General I/O Target](obtaining-information-about-a-general-i-o-target.md)

 

 





