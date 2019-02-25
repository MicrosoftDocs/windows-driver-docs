---
title: SCSI Port Driver
description: SCSI Port Driver
ms.assetid: e97ea5f2-7f20-4d3d-82a2-7d83e1eba30e
keywords:
- storage port drivers WDK , SCSI Port driver
- SCSI Port drivers WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Port Driver


## <span id="ddk_scsi_port_driver_kg"></span><span id="DDK_SCSI_PORT_DRIVER_KG"></span>


Microsoft provides a SCSI Port driver as a standard feature of the Microsoft Windows storage architecture. The SCSI Port driver streamlines the Windows storage subsystem by emulating a simplified SCSI adapter. Storage class drivers load on top of the port driver. This means that you can write storage class drivers for Windows with minimal concern for the unique hardware features of each SCSI adapter.

The emulation capabilities of the SCSI Port driver also allow you to develop minidrivers that are much simpler to design and code than a monolithic port driver. In other words, using the SCSI Port driver allows you to focus on developing a miniport driver that handles the particular features of your adapter.

To use the SCSI Port support routines, link to one of the SCSI Port support libraries, *scsiport.lib* or *scsiwmi.lib*. These SCSI Port libraries handle all interaction between the miniport driver and the hardware abstraction layers (HAL) of the operating system. Miniport drivers must not link directly to the HAL support library, *hal.lib*, nor should they link directly to the *ntoskrnl.lib* or *libcntpr.lib* support libraries. SCSI miniport drivers that do so are not eligible for a Windows logo.

The following sections examine the key features of the SCSI Port driver.

1.  [Capabilities Provided by SCSI Port](capabilities-provided-by-scsi-port.md)

2.  [SCSI Port's Interface with the Storage Class Driver](scsi-port-s-interface-with-the-storage-class-driver.md)

3.  [SCSI Port's Interface with SCSI Port Miniport Drivers](scsi-port-s-interface-with-scsi-port-miniport-drivers.md)

4.  [SCSI Port I/O Model](scsi-port-i-o-model.md)

A general discussion of SCSI Port miniport drivers is provided in [SCSI Miniport Drivers](scsi-miniport-drivers.md).

The Windows storage architecture also provides the [Storport Driver](storport-driver.md), an alternative to SCSI Port for high-performance devices.

 

 




