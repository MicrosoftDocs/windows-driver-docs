---
title: Signing WBDI Drivers
description: Signing WBDI Drivers
ms.assetid: 1BE83F60-4A04-457E-BD31-5E6F104A3505
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Signing WBDI Drivers


The code-signing requirements for WBDI drivers are the same as for other drivers. The specific requirements depend on whether the WBDI driver is implemented by using the user-mode driver framework (UMDF), the kernel-mode driver framework (KMDF), or the Windows Driver Model (WDM).

If a fingerprint device supports Plug and Play, the WBDI driver package must be signed to ensure that it hasn not been tampered with. Such a signature is required whether the driver runs in kernel mode or in user mode. You are not required to sign every individual file in the package. Instead, you create a catalog file that contains a hash value for every file in the package, and you sign the catalog file. The CatalogFile directive in the INF indicates the name of this file. For most WBDI drivers, the catalog file signature is the only type of signature that you need.

For some WBDI drivers, multiple signaturesare needed. A kernel-mode boot-start driver, which is a driver that is loaded by the Windows loader during the boot process, requires an additional embedded signature on both x86 and x64 platforms. Therefore, a boot-start driver must usually be signed in two ways:

-   A boot-start driver package that is installed by using an INF must have a signed catalog file, just like other types of drivers. The catalog file is used for signature verification during installation.
-   A boot-start driver's binary file must be embedded-signed by using an SPC with a corresponding cross-certificate. A cross-certificate is issued by a CA (called a trusted root) that signs the public key for the root certificate of another CA, which creates a chain of trust from a single, trusted root CA to multiple other CAs.

You typically embedded-sign a driver binary after you create and sign the package's catalog file.

Boot-start drivers have the following characteristics:

-   The driver's INF specifies the start type as "Start=0".
-   A kernel service is configured with a **ServiceType** of kernel driver or file system driver and has **StartMode** set to "boot".

If the driver is packaged in a self-extracting executable file, the self-extracting executable file should also be signed.

This topic does not cover the details of driver-signing requirements or procedures. For general information about signature requirements for drivers, see [Driver Signing](http://go.microsoft.com/fwlink/p/?linkid=201836).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Signing%20WBDI%20Drivers%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




