---
ms.assetid: bf92ab5f-9e54-4faa-8ae9-5cbe43434514
title: Signing a Driver
description: All drivers running on 64-bit versions of Windows must be signed before Windows will load them. However, driver signing is not required on 32-bit versions of Windows.Visual Studio to sign a driver package.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Signing a Driver

All drivers running on 64-bit versions of Windows must be signed before Windows will load them. However, driver signing is not required on 32-bit versions of Windows.

In order to sign a driver, a certificate is required. You can create your own certificate to sign your driver with during development and testing. However, for a public release you must sign your driver with a certificate issued by a trusted root authority.

**Note**  A *driver package project* can package the output of other projects. If you build a driver package project, Microsoft Visual Studio will build the other projects on which it has dependencies. The driver package project has its own driver signing properties that are separate from any other dependent projects, and its driver signing properties apply *only* to the catalog (if any) produced by the driver package project. That is, the driver package project will not automatically add an embedded signature to driver binaries produced by other projects, as a different certificate may be used to sign the other driver projects, for example, a test certificate, and the result in such a case would be a driver package where the binaries are unintentionally signed with one certificate, while the package catalog is signed with a different certificate. This can result in performance degradation. For example, if a boot start driver binary's embedded signature is invalid, Windows cannot use certificate it was signed with to validate the binary. Instead, Windows must validate the binary against the catalog's signature, which would increase boot time.

 

This section describes how to use Visual Studio to sign a driver package.

-   [Signing a Driver During Development and Testing](signing-a-driver-during-development-and-testing.md)
-   [Signing a Driver for Public Release](signing-a-driver-for-public-release.md)

 

 





