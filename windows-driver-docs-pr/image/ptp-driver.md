---
title: PTP Driver
author: windows-driver-content
description: PTP Driver
MS-HAID:
- 'WIA\_drv\_cam\_f513ce0b-6019-417f-80f4-8a8dab3a8f48.xml'
- 'image.ptp\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c8bfdea9-0778-498f-a87d-d2766c9c02cc
---

# PTP Driver


## <a href="" id="ddk-ptp-driver-si"></a>


The Picture Transfer Protocol (PTP) driver enables PTP devices to support the WIA driver model. This driver is written using the WIA architecture and adheres to the PIMA 15740:2000 standard, First Edition, and Revision 1.0 of the USB Still Image Capture Device Definition (USB SICDD).

Several terms used in the PIMA 15740:2000, First Edition standard are used in this documentation: StorageInfo dataset, ObjectInfo dataset, and DeviceInfo dataset. Refer to the I3A PTP-Picture Transfer Protocol standard on the [I3A IT10 Electronic Still Picture Imaging](http://www.i3a.org/technologies/digitalimaging/ptp/) website for definitions of these structures.

This section covers the following topics:

[Installing a PTP Camera](installing-a-ptp-camera.md)

[Mapping PTP Objects to WIA Items](mapping-ptp-objects-to-wia-items.md)

[PTP Events](ptp-events.md)

[PTP Error Recovery](ptp-error-recovery.md)

[PTP Error Codes](ptp-error-codes.md)

[PTP Required Commands](ptp-required-commands.md)

[Canceling a Data Transfer by a Device](canceling-a-data-transfer-by-a-device.md)

[Creating a Well-Behaved PTP Camera](creating-a-well-behaved-ptp-camera.md)

[Vendor-Extended Features](vendor-extended-features.md)

[PTP References](ptp-references.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PTP%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


