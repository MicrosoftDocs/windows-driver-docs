---
title: IDE Port Driver
description: IDE Port Driver
ms.assetid: 8e292680-6fa7-4f6b-b4ec-6f0f0d795d03
---

# IDE Port Driver


In Microsoft Windows NT 4.0, the port/miniport driver pair associated with the IDE bus is a SCSI miniport driver, *atapi.sys*, that linked to the SCSI port driver, *scsiport.sys*.

In Microsoft Windows 2000 and Windows XP, the IDE port driver *atapi.sys* is an independent driver that no longer links to *scsiport.sys*, nor to any other wrapper driver.

There are three system-supplied drivers in the IDE driver model for Windows 2000 and Windows XP: *atapi.sys* (port driver), *pciidex.sys* (controller driver), and *pciide.sys* (generic controller minidriver). All three drivers are illustrated in the following figure.

![windows 2000 and windows xp ide driver stack ](images/idedrvrs.png)

Starting from the bottom of the figure, the following describes each driver in the stack:

1.  The IDE stack in Windows 2000 and Windows XP is layered over the PCI bus driver.

2.  Microsoft provides a native IDE controller driver/minidriver pair that is capable of managing most IDE controllers. The IDE controller driver, *pciidex.sys*, handles the hardware-independent aspects of the driver pair, and the minidriver, *pciide.sys*, handles the hardware-dependent aspects.

3.  Vendors can elect to provide their own IDE controller minidriver instead of using the native minidriver, *pciide.sys*. The vendor's minidriver must work together with the Microsoft-supplied controller driver to form a controller-minidriver pair. See [Requirements for Vendor-Supplied IDE Controller Minidrivers](requirements-for-vendor-supplied-ide-controller-minidrivers.md) for an explanation of the requirements a vendor's minidriver must fulfill to work properly with the native Microsoft controller driver.

4.  Microsoft provides an IDE port driver, *atapi.sys,* which is also known as the *channel driver*, because it creates and manages a functional device object (FDO) for each IDE channel. The port driver is layered above the IDE controller/minidriver pair. It translates the SCSI request blocks (SRB) that it receives from the storage class driver into the format required by the underlying IDE controller. In particular, the command descriptor blocks (CDB) contained within an SRB are defined differently for ATAPI and SCSI devices. The port driver repackages CDBs to make them compatible with the ATAPI transport protocol, thereby insulating upper-level drivers from peculiarities of the IDE bus.

5.  Microsoft provides a CD-ROM class driver capable of managing all CD-ROM (type 5 SCSI) devices.

To see a diagram of the device object stack corresponding to the driver stack in the previous figure, see [Device Object Example for a PCI IDE Controller](device-object-example-for-a-pci-ide-controller.md).

In Windows Vista and later versions of the operating system, the IDE stack is managed by the [ATA Port Driver](ata-port-driver.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20IDE%20Port%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




