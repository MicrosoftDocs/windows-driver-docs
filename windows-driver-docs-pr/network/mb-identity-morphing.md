---
title: MB identity morphing
description: Describes identity morphing for MB device drivers
ms.assetid: 7AA14A5E-47AA-4A9A-94A4-769F374EA465
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Identity Morphing


## Identity Morphing


Mobile broadband USB dongle solutions eliminate the need for distributing the driver package for mobile broadband and other IHV functions through separate media (such as CD-ROM) by having a storage function in the USB device itself that contains the driver package.

Upon first time insertion of such a device in Windows, the device presents itself as mass storage, which results in the Windows AutoPlay dialog displayed to the user. At this point, the device exposes no other functions to the host except the mass storage function to prevent the other functions appearing to the user as non-functional due to missing driver software. The user can run the IHV-supplied software that installs the driver package. In addition to installing the driver package, the IHV-supplied software also morphs the device to expose the other functions to the user.

Mobile broadband devices that use the previously described mechanism when inserted in Windows 8 would come up as mass storage. Because Windows 8 has native support for mobile broadband functions that conform to the MBIM specification, installation of the driver package is not necessary for the user to use the mobile broadband function. The subtopics in this section provide guidance to IHVs on how to implement this solution for Windows 8 to allow the user to use the mobile broadband device without the need to install the driver package.

Mobile broadband devices that exhibit morphing behavior are referred to as morphing devices throughout the subtopics in this section.

[MB Identity Morphing Solution Overview](mb-identity-morphing-solution-overview.md)
[MB Identity Morphing Solution Details](mb-identity-morphing-solution-details.md)
 

 





