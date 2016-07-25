---
title: Test-Signing a Driver through an Embedded Signature
description: Test-Signing a Driver through an Embedded Signature
ms.assetid: 862e89e0-f84a-4058-a32f-09ae3043b884
---

# Test-Signing a Driver through an Embedded Signature


A signed [catalog file](catalog-files.md) is all that you must have to correctly install and load most [driver packages](driver-packages.md). However, embedded-signing might also be an option. Embedded-signing refers to adding a digital signature to the driver's binary image file itself, instead of saving the digital signature in a catalog file. As a result, the driver's binary image is modified when the driver is embedded-signed.

Embedded-signing of kernel-mode binaries (for example, drivers and associated .dll files) are required whenever:

-   The driver is a boot-start driver. In 64-bit versions of Windows Vista and later versions of Windows, the [kernel-mode code signing requirements](kernel-mode-code-signing-requirements--windows-vista-and-later-.md) state that a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) must have an embedded signature. This is required regardless of whether the driver's driver package has a digitally-signed catalog file.

-   The driver is installed through a driver package that does not include a catalog file.

As with [catalog files](catalog-files.md), [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) is used to embed a digital signature within kernel-mode binary files by using a test certificate. The following command line shows how to run SignTool to do the following:

-   Test-sign the 64-bit version of the Toastpkg sample's binary file, toaster.sys. Within the WDK installation directory, this file is located in the *src\\general\\toaster\\toastpkg\\toastcd\\amd64* directory.

-   Use the Contoso.com(Test) certificate from the PrivateCertStore for the test signature. For more information about how this certificate was created, see [Creating Test Certificates](creating-test-certificates.md).

-   Time stamp the digital signature through a time stamp authority (TSA).

To test-sign the *toaster.sys* file, run the following command line:

```
Signtool sign /v /s PrivateCertStore /n Contoso.com(Test) /t http://timestamp.verisign.com/scripts/timestamp.dll amd64\toaster.sys
```

Where:

-   The **sign** command configures SignTool to sign the specified catalog file, tstamd64.cat.

-   The **/v** option enables verbose operations, in which SignTool displays successful execution and warning messages.

-   The **/s** option specifies the name of the certificate store (*PrivateCertStore)* that contains the test certificate.

-   The **/n** option specifies the name of the certificate (*Contoso.com(Test))* that is installed in the specified certificate store.

-   The **/t** option specifies URL of the TSA (*http://timestamp.verisign.com/scripts/timestamp.dll*) which will time stamp the digital signature.
    **Important**   Including a time stamp provides the necessary information for key revocation in case the signer's code signing private key is compromised.

     

-   *amd64\\toaster.sys* specifies the name of the kernel-mode binary file which will be embedded-signed.

For more information about SignTool and its command-line arguments, see [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778).

For more information about how to test-sign a driver by using an embedded signature, see [Test-Signing a Driver File](test-signing-a-driver-file.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Test-Signing%20a%20Driver%20through%20an%20Embedded%20Signature%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




