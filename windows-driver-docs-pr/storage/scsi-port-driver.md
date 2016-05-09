---
title: SCSI Port Driver
description: SCSI Port Driver
ms.assetid: e97ea5f2-7f20-4d3d-82a2-7d83e1eba30e
keywords: ["storage port drivers WDK , SCSI Port driver", "SCSI Port drivers WDK storage"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Port%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




