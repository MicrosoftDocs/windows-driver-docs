---
title: General I/O Targets in UMDF
description: General I/O Targets in UMDF
ms.assetid: 46fac165-3afd-4481-b68d-8d3474e0ff52
keywords:
- general I/O targets WDK UMDF
- I/O targets WDK UMDF , general
- local I/O targets WDK UMDF
- remote I/O targets WDK UMDF
- general I/O targets WDK UMDF , about general I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General I/O Targets in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

General I/O targets, which can be either *local* or *remote*, are I/O targets that do not support special, device-specific data formats, such as USB request blocks. Before drivers send data to a general I/O target, they must put data into a write buffer in a format that the I/O target and device can interpret. Likewise, when drivers read data from a general I/O target, the drivers must be able to interpret the contents of data buffers that they receive from the target.

<a href="" id="local-i-o-targets-------"></a>**Local I/O Targets**   
Drivers often send I/O requests to the next-lower driver in the driver stack. Therefore, each UMDF-based driver has a *default I/O target* for each device, which is the device's next-lower driver. The default I/O target for the lowest-level UMDF-based driver is the kernel-mode [reflector](overview-of-the-umdf.md).

Sometimes a UMDF-based driver must send I/O requests to a file-handle-based I/O target, such as a file or a network socket. Therefore, the framework also provides file-handle-based I/O target objects.

Both the default I/O target and file-handle-based I/O targets are called *local I/O targets*, because UMDF-based drivers use these targets to send I/O requests to devices that the driver stack supports.

<a href="" id="remote-i-o-targets-------"></a>**Remote I/O Targets**   
Occasionally, a driver must send an I/O request to a different driver stack. Therefore, the framework also provides *remote I/O targets*, which consist of all of the I/O targets except local I/O targets.

A remote I/O target might be a device that the driver stack does not support, a file on that device, or a [device interface](using-device-interfaces-in-umdf-drivers.md) for that device.

The following sections describe how to initialize and use a general I/O target:

-   [Initializing a General I/O Target in UMDF](initializing-a-general-i-o-target-in-umdf.md)
-   [Sending I/O Requests to a General I/O Target in UMDF](sending-i-o-requests-to-a-general-i-o-target-in-umdf.md)
-   [Controlling a General I/O Target's State in UMDF](controlling-a-general-i-o-target-s-state-in-umdf.md)
-   [Obtaining Information About a General I/O Target in UMDF](obtaining-information-about-a-general-i-o-target-in-umdf.md)

 

 





