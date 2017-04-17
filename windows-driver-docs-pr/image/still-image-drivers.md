---
title: Still Image Drivers
author: windows-driver-content
description: Still Image Drivers
ms.assetid: e207f76e-ff35-4a0d-a4bf-744931055eb8
---

# Still Image Drivers


## <a href="" id="ddk-still-image-drivers-si"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Still%20Image%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


