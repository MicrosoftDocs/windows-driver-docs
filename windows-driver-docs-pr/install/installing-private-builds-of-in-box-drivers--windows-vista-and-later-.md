---
title: Installing Private Builds of Inbox Drivers
description: Installing Private Builds of Inbox Drivers
ms.assetid: 89170dff-284d-4d82-953c-46792158fbe5
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





