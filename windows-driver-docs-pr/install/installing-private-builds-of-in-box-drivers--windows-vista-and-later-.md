---
title: Installing Private Builds of Inbox Drivers
description: Installing Private Builds of Inbox Drivers
ms.assetid: 89170dff-284d-4d82-953c-46792158fbe5
---

# Installing Private Builds of Inbox Drivers


Starting with Windows Vista, the operating system provides a mechanism that can install updated versions of Microsoft-signed drivers. Otherwise, a Microsoft-signed driver has a higher selection value, or *rank*, than a driver that is signed by a third party. This makes it difficult for driver developers to install private builds of an inbox driver.

This section describes how to build and install a private build of a driver that is included in the default installation of Windows. Such a driver is referred to as an "*inbox*" driver.

**Note**   To understand this material, you must be familiar with digitally signing a driver and how Windows ranks drivers based on this signature and other criteria. For more information about digital signatures for drivers, see [Driver Signing](driver-signing.md).

 

The following topics describe how you can override the default rank number for your driver so that you can install a private build of an inbox driver:

[Overview of Installing Private Builds of Inbox Drivers](overview-of-installing-private-builds-of-in-box-drivers.md)

[Creating a Private Build of an Inbox Driver](creating-a-private-build-of-an-in-box-driver.md)

[Configuring Windows to Rank Driver Signatures Equally](configuring-windows-to-rank-driver-signatures-equally.md)

[Installing the Updated Version of the Driver Package](installing-the-updated-version-of-the-driver-package.md)

**Important**   Windows Update depends on Microsoft-signed drivers having priority over drivers that have third-party signatures. Configuring a system to override this priority can interfere with the ability of Windows Update to provide the correct drivers to consumers. This can result in an installation failure for drivers that are delivered by Windows Update.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20Private%20Builds%20of%20Inbox%20Drivers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




