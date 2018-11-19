---
title: IEEE 1394 Bus Driver in Windows 7
description: Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver that supports faster speeds and alternative media as defined in the IEEE-1394b specification.
ms.assetid: 3744C1D5-E411-4E47-9154-40E15626250D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IEEE 1394 Bus Driver in Windows 7


Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver that supports faster speeds and alternative media as defined in the IEEE-1394b specification. The 1394ohci.sys bus driver is a single (monolithic) device driver, implemented by using the kernel-mode driver framework (KMDF). The legacy 1394 bus driver (available in earlier versions of Windows) includes multiple device drivers that were implemented by using the Windows Driver Model (WDM) in a port/miniport configuration. The 1394ohci.sys bus driver replaces the legacy port driver, 1394bus.sys, and the primary miniport driver, ochi1394.sys.

The new 1394ohci.sys bus driver is fully backward compatible with the legacy bus driver. This topic describes some of the known differences in behavior between the new and the legacy 1394 bus driver.

**Note**  The 1394ohci.sys driver is a system driver that is included in Windows. It is automatically loaded when you install a 1394 controller. This is not a redistributable driver that you can download separately.

 

-   [I/O Request Completion](#io-request-completion)
-   [Configuration ROM Retrieval](#configuration-rom-retrieval)
-   [IEEE-1394-1995 PHY Support](#ieee-1394-1995-phy-support)
-   [NODE\_DEVICE\_EXTENSION Structure Usage](#-node-device-extension-structure-usage)
-   [Gap Count Optimization](#gap-count-optimization)
-   [Device Driver Interface (DDI) Changes](#device-driver-interface-ddi-changes)
-   [Related topics](#related-topics)

##  I/O Request Completion


All I/O requests that are sent to the new 1394 bus driver return STATUS\_PENDING because the 1394ohci.sys bus driver is implemented by using KMDF instead of WDM. This behavior differs from that of the legacy 1394 bus driver, in which certain I/O requests complete immediately.

A client driver must wait until I/O requests sent to the new 1394 bus driver are complete. You can provide an I/O completion routine that is called after the request is complete. The status of the completed I/O request is in the IRP.

## Configuration ROM Retrieval


The new 1394 bus driver tries to use asynchronous block transactions at faster bus speeds to retrieve the contents of a node's configuration ROM. The legacy 1394 bus driver uses asynchronous quadlet reads at S100 speed—or 100 megabits per second (Mbps). The 1394ohci.sys bus driver also uses the values that are specified in **generation** and **max\_rom** entries of the node's configuration ROM header to improve the retrieval of the remaining content of the configuration ROM. For more information about how the new 1394 bus driver retrieves the contents of a node's configuration ROM, see [Retrieving the Contents of a IEEE 1394 Node's Configuration ROM](https://msdn.microsoft.com/library/windows/hardware/gg266408).

## IEEE-1394-1995 PHY Support


The 1394ohci.sys bus driver requires a physical layer (PHY) that supports IEEE-1394a or IEEE-1394b. It does not support a PHY that supports IEEE-1394-1995. This requirement is due to the 1394ohci.sys bus driver's exclusive use of short (arbitrated) bus resets.

##  NODE\_DEVICE\_EXTENSION Structure Usage


A client driver can reference the device extension in the 1394 bus driver associated with the physical device object (PDO) for the device that the client driver controls. This device extension is described by the **NODE\_DEVICE\_EXTENSION** structure. In 1394ohci.sys, this structure remains at the same location as in the legacy 1394 bus driver, but the nonstatic members of the structure might not be valid. When a client driver uses the new 1394 bus driver, they must make sure that the data accessed in **NODE\_DEVICE\_EXTENSION** is valid. The static members of **NODE\_DEVICE\_EXTENSION** that contain valid data are **Tag**, **DeviceObject**, and **PortDeviceObject**. All other members **NODE\_DEVICE\_EXTENSION** are nonstatic, which the client driver must not reference.

## Gap Count Optimization


The default behavior of the 1394ohci.sys bus driver is to optimize the gap count when it finds only IEEE 1394a devices on the 1394 bus, excluding the local node. For example, if the system that is running 1394ohci.sys has a host controller that complies with IEEE 1394b but all devices on the bus comply with IEEE 1394a, then the new 1394 bus driver tries to optimize the gap count.

Gap count optimization occurs only if the 1394ohci.sys bus driver determines that the local node is the bus manager.

The 1394ohci.sys bus driver determines whether a device complies with IEEE-1394a by the speed setting in the node's self-id packet. If a node sets both of the bits in the speed (sp) field in the self-id packet, then 1394ohci.sys considers the node to comply with IEEE-1394b. If the speed field contains any other value, then 1394ohci.sys considers the node to comply with IEEE-1394a. The gap count value that is used is based on table E-1 in the IEEE-1394a specification, which provides the gap count as a function of hops. The 1394ohci.sys bus driver does not compute the gap count. You can change the default gap count behavior by using a registry value. For more information, see [Modifying the Default Behavior of the IEEE 1394 Bus Driver](https://msdn.microsoft.com/library/windows/hardware/gg266403).

##  Device Driver Interface (DDI) Changes


In Windows 7, the 1394 DDIs were changed to support faster speeds as defined by the 1394b specification and improved to simplify the development of 1394 client drivers. For more information about the general DDI changes that the new 1394 bus driver supports, see [Device Driver Interface (DDI) Changes in Windows 7](https://msdn.microsoft.com/library/windows/hardware/gg266400).

## Related topics
[The IEEE 1394 Driver Stack](https://msdn.microsoft.com/library/windows/hardware/ff538867)  
[Retrieving the Contents of a IEEE 1394 Node's Configuration ROM](https://msdn.microsoft.com/library/windows/hardware/gg266408)  



