---
title: Test-Sign a Driver Package
description: This section describes how to test-sign a driver package.
ms.date: 03/17/2023
---

# Test-sign a driver package

This section describes how to test-sign a driver package.

## How to test-sign a driver package

Use the following steps to test-sign a driver package using a test certificate:

1. Create a new certificate file:

    ```console
    makecert -r -pe -ss TestCertStoreName -n "CN=WSD FabrikamV4 Driver Testing Cert" CertFileName.cer -sv CertFile.pvk
    ```

    You will be prompted to enter a password.

1. Use the pvk file to create a pfx file:

    ```console
    pvk2pfx.exe /pvk CertFile.pvk /spc CertFileName.cer /pfx CertPfx.pfx
    ```

    You will be prompted to enter a password.

1. Add the certificate to the root and trustedpublisher certificate stores on the machine where the that the driver will be installed.

    This enables the driver to pass signature validation during plug and play install. Without this step the driver will not pass this check and will fail to auto install the printer.

    ```console
    CertMgr /add CertFileName.cer /s /r localMachine root
    CertMgr /add CertFileName.cer /s /r localMachine trustedpublisher
    ```

1. Sign the "FabrikamPrintDriverV4 Package" with the pfx file you created in step 2. The other projects do not need to be driver signed as this step is what creates the package.

For more information, see [How to Test-Sign a Driver Package](../install/how-to-test-sign-a-driver-package.md).
