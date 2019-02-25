---
title: Still Image Drivers
description: Still Image Drivers
ms.assetid: e207f76e-ff35-4a0d-a4bf-744931055eb8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Still Image Drivers





The Microsoft Windows Driver Kit (WDK) includes an architecture called Windows Image Acquisition (WIA). WIA is built on the foundation of the Microsoft Still Image architecture (Microsoft STI), thus drivers built on STI easily migrate to WIA.

This section is provided for legacy drivers that are developed on Microsoft STI. It describes the COM interfaces that are defined by Microsoft STI and available to vendors of such still image hardware as flatbed scanners and digital still image cameras. The COM interfaces described in this section are called by, or defined by, the following vendor-supplied software:

-   Device-specific components of image acquisition API software, such as the TWAIN data sources that are required so the TWAIN API can support specific still image devices.

-   User-mode still image minidrivers, which provide a communications path from image acquisition software to lower-level device and bus drivers.

The section contains the following sections:

[Overview of Microsoft STI and Microsoft WIA](overview-of-microsoft-sti-and-microsoft-wia.md)

[Introduction to Microsoft STI](introduction-to-microsoft-sti.md)

[Microsoft STI Components](microsoft-sti-components.md)

[Still Image COM Interfaces](still-image-com-interfaces.md)

[Creating Push-Model Aware Applications](creating-push-model-aware-applications.md)

[Creating Device-Specific Components for Image Acquisition APIs](creating-device-specific-components-for-image-acquisition-apis.md)

[Creating a User-Mode Still Image Minidriver](creating-a-user-mode-still-image-minidriver.md)

[Installing and Configuring Still Image Components](installing-and-configuring-still-image-components.md)

[Starting and Stopping the Still Image Service](starting-and-stopping-the-still-image-service.md)

[Debugging Still Image Components](debugging-still-image-components.md)

 

 




