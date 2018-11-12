---
title: Release-Signing a Driver through an Embedded Signature
description: Release-Signing a Driver through an Embedded Signature
ms.assetid: ffea2479-83ee-4d94-a5e6-73ecea9fc17d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Release-Signing a Driver through an Embedded Signature


A signed [catalog file](catalog-files.md) is all that you must have to correctly install and load most [driver packages](driver-packages.md). However, embedded-signing might also be an option. Embedded-signing refers to adding a digital signature to the driver's binary image file itself, instead of saving the digital signature in a catalog file. As a result, the driver's binary image is modified when the driver is embedded-signed.

Embedded-signing of kernel-mode binaries (for example, drivers and associated .dll files) are required whenever:

-   The driver is a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver). In 64-bit versions of Windows Vista and later versions of Windows, the [kernel-mode code signing requirements](kernel-mode-code-signing-requirements--windows-vista-and-later-.md) state that a *boot-start driver* must have an embedded signature. This is required regardless of whether the driver's driver package has a digitally-signed catalog file.

-   The driver is installed through a driver package that does not include a catalog file.

As with [catalog files](catalog-files.md), the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool is used to embed a digital signature within kernel-mode binary files by using a test certificate. The following command line shows how to run SignTool to do the following:

-   Test-sign the 64-bit version of the Toastpkg sample's binary file, toaster.sys. Within the WDK installation directory, this file is located in the *src\\general\\toaster\\toastpkg\\toastcd\\amd64* directory.

-   Use a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) issued by a commercial certificate authority (CA).

-   Use a compatible cross-certificate for SPC.

-   Assign a time stamp to the digital signature through a time stamp authority (TSA).

To test-sign the *toaster.sys* file, run the following command line:

```cpp
Signtool sign /v /ac MSCV-VSClass3.cer /s MyPersonalStore /n contoso.com /t http://timestamp.verisign.com/scripts/timstamp.dll amd64\toaster.sys
```

Where:

-   The **sign** command configures SignTool to sign the specified kernel-mode binary file, *amd64\\toaster.sys*.

-   The **/v** option enables verbose operations, in which SignTool displays successful execution and warning messages.

-   The **/ac** option specifies the name of the file which contains the cross-certificate (*MSCV-VSClass3.cer*) obtained from the CA. Use the full path name if the cross-certificate is not in the current directory.

-   The **/s** option specifies the name of the Personal certificate store (*MyPersonalStore)* that contains the SPC.

-   The **/n** option specifies the name of the certificate (*Contoso.com)* that is installed in the specified certificate store.

-   The **/t** option specifies URL of the TSA (*http://timestamp.verisign.com/scripts/timstamp.dll*) which will timestamp the digital signature.

    **Important**   Including a time stamp provides the necessary information for key revocation in case the signer's code signing private key is compromised.

     

-   *amd64\\toaster.sys* specifies the name of the kernel-mode binary file which will be embedded-signed.

For more information about SignTool and its command-line arguments, see [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778).

For more information about release-signing a driver through an embedded signature, see [Release-Signing Driver Packages](release-signing-driver-packages.md) and [Release-Signing a Driver File](release-signing-a-driver-file.md).

 

 





