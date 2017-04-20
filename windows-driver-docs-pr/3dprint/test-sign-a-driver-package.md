---
title: Test-sign a driver package
author: windows-driver-content
description: This section describes how to test-sign a driver package.
ms.assetid: 3BC92099-A464-4C62-9EB7-DD6AA0D1FB03
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Test-sign a driver package


This section describes how to test-sign a driver package.

## <a href="" id="test-sign-a-driver-package-"></a>Test-sign a driver package


Use the following steps to test-sign a driver package using a test certificate:

1.  Create a new certificate file:

    ``` syntax
    makecert -r -pe -ss TestCertStoreName -n "CN=WSD FabrikamV4 Driver Testing Cert" CertFileName.cer -sv CertFile.pvk
    ```

    You will be prompted to enter a password.

2.  Use the pvk file to create a pfx file:

    ``` syntax
    pvk2pfx.exe /pvk CertFile.pvk /spc CertFileName.cer /pfx CertPfx.pfx
    ```

    You will be prompted to enter a password.

3.  Add the certificate to the root and trustedpublisher certificate stores on the machine where the that the driver will be installed.

    This enables the driver to pass signature validation during plug and play install. Without this step the driver will not pass this check and will fail to auto install the printer.

    ``` syntax
    CertMgr /add CertFileName.cer /s /r localMachine root
    CertMgr /add CertFileName.cer /s /r localMachine trustedpublisher
    ```

4.  Sign the "FabrikamPrintDriverV4 Package" with the pfx file you created in step 2. The other projects do not need to be driver signed as this step is what creates the package.

For more information, see [How to Test-Sign a Driver Package](https://msdn.microsoft.com/library/windows/hardware/ff546236.aspx).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Test-sign%20a%20driver%20package%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


