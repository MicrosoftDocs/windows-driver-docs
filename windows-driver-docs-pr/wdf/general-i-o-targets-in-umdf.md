---
title: General I/O Targets in UMDF
description: General I/O Targets in UMDF
ms.assetid: 46fac165-3afd-4481-b68d-8d3474e0ff52
keywords: ["general I/O targets WDK UMDF", "I/O targets WDK UMDF general", "local I/O targets WDK UMDF", "remote I/O targets WDK UMDF", "general I/O targets WDK UMDF about general I/O targets"]
---

# General I/O Targets in UMDF


\[This topic applies to UMDF 1.*x*.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20General%20I/O%20Targets%20in%20UMDF%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




