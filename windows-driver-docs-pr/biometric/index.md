---
title: Biometric Devices Design Guide
description: Biometric Devices Design Guide
ms.assetid: 78270890-4ea2-403e-bbd7-84a22581bbb7
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Biometric Devices Design Guide


## <span id="ddk_biometric_design_guide_kg"></span><span id="DDK_BIOMETRIC_DESIGN_GUIDE_KG"></span>


This section describes how to write user-mode drivers that work with the Windows Biometric Driver Interface (WBDI). WBDI is the driver interface of the Windows Biometric Framework (WBF). WBF ships with Windows 7 and later versions of the Windows operating system.

## <span id="in_this_section"></span>In this section


-   [Getting Started with Biometric Drivers](getting-started-with-biometric-drivers.md)
-   [Roadmap for Developing Biometric Drivers](roadmap-for-developing-biometric-drivers.md)
-   [Sample Biometric Driver](sample-biometric-driver.md)
-   [Supporting Biometric IOCTL Calling Sequence](supporting-biometric-ioctl-calling-sequence.md)
-   [Using WinUSB in a WBDI Driver](using-winusb-in-a-wbdi-driver.md)
-   [Installing a Biometric Driver](installing-a-biometric-driver.md)
-   [Managing Queues in a WBDI Driver](managing-queues-in-a-wbdi-driver.md)
-   [Creating a Device Interface for a WBDI Driver](creating-a-device-interface-for-a-wbdi-driver.md)
-   [Supporting Secure Channels in WBDI Drivers](supporting-secure-channels-in-wbdi-drivers.md)
-   [Using WBDI with Non-PnP Devices or Proprietary Stacks](using-wbdi-with-non-pnp-devices-or-proprietary-stacks.md)
-   [Hardware Considerations for Biometric Drivers](hardware-considerations-for-biometric-drivers.md)
-   [Ranking a Biometric Driver on Windows Update](ranking-a-biometric-driver-on-windows-update.md)
-   [Testing Biometric Drivers](testing-biometric-drivers.md)
-   [Signing WBDI Drivers](signing-wbdi-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Biometric%20Devices%20Design%20Guide%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




