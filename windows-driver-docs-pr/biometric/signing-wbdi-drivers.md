---
title: Signing WBDI Drivers
description: Signing WBDI Drivers
ms.assetid: 1BE83F60-4A04-457E-BD31-5E6F104A3505
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Signing WBDI Drivers


The specific code-signing requirements for WBDI drivers depend on whether the WBDI driver is implemented by using the user-mode driver framework (UMDF), the kernel-mode driver framework (KMDF), or the Windows Driver Model (WDM). In addition to the catalog file that needs to be signed, certain dlls need to be signed with a specific attribute. For more information, see [Steps to submit a fingerprint driver](https://docs.microsoft.com/windows-hardware/design/device-experiences/windows-hello-driver-signing).

All WBDI driver packages must be signed through the WHQL portal, to ensure that it has not been tampered with. Such a signature is required whether the driver runs in kernel mode or in user mode. You are not required to sign every individual file in the package. Instead, you create a catalog file that contains a hash value for every file in the package, and you sign the catalog file. The CatalogFile directive in the INF indicates the name of this file. For most WBDI drivers, the catalog file signature is the only type of signature that you need.

For some WBDI drivers, multiple signatures are needed. A kernel-mode boot-start driver, which is a driver that is loaded by the Windows loader during the boot process, requires an additional embedded signature on both x86 and x64 platforms. Therefore, a boot-start driver must usually be signed in two ways:

-   A boot-start driver package that is installed by using an INF must have a signed catalog file, just like other types of drivers. The catalog file is used for signature verification during installation.
-   A boot-start driver's binary file must be embedded-signed by using an SPC with a corresponding cross-certificate. A cross-certificate is issued by a CA (called a trusted root) that signs the public key for the root certificate of another CA, which creates a chain of trust from a single, trusted root CA to multiple other CAs.

You typically embedded-sign a driver binary after you create and sign the package's catalog file.

Boot-start drivers have the following characteristics:

-   The driver's INF specifies the start type as "Start=0".
-   A kernel service is configured with a **ServiceType** of kernel driver or file system driver and has **StartMode** set to "boot".


This topic does not cover the details of driver-signing requirements or procedures. For general information about signature requirements for drivers, see [Driver Signing](http://go.microsoft.com/fwlink/p/?linkid=201836).

 

 





