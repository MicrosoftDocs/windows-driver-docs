---
title: Managing the Signing Process
description: Managing the Signing Process
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing the Signing Process


The process of signing a [driver package's](driver-packages.md) [catalog file](catalog-files.md) or embedding a signature in a driver file involves the following activities.

### Driver Signing Administration

This is typically handled by the publisher's program management and software release services and includes the following topics:

-   [Selecting the appropriate signature type](./digital-signatures-and-pnp-device-installation--windows-vista-and-late.md)

-   Obtaining the necessary [release certificate](release-certificates.md) or [test certificate](./makecert-test-certificate.md)

-   [Managing the digital signature or code signing keys](managing-the-digital-signature-or-code-signing-keys.md)

### Driver Development

This is typically handled by the publisher's development team and includes the following:

-   Implementing the driver.

-   Creating a signed driver package for internal testing. For information about test signing, see [Signing Drivers during Development and Test](./introduction-to-test-signing.md).

-   Creating a signed driver package for release. For information about how to sign drivers for release, see [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md).

