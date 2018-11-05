---
title: Verifying the Release-Signature
description: Verifying the Release-Signature
ms.assetid: 28ed3bb6-dc57-42f9-8bd5-7118619f3bf5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verifying the Release-Signature


After a [driver package](driver-packages.md) is release-signed, the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool can be used to verify the signatures of:

-   Individual files within the driver package.

-   Kernel-mode binaries, such as drivers, which have been embedded-signed.

The examples in this topic use the 64-bit version of the Toastpkg sample's binary file, *toaster.sys*. Within the WDK installation directory, this file is located in the *src\\general\\toaster\\toastpkg\\toastcd\\amd64* directory.

The following example verifies the signature of *toaster.sys* in the *tstamd64.cat* release-signed [catalog file](catalog-files.md):

```cpp
Signtool verify /kp /v /c tstamd64.cat amd64\toaster.sys
```

Where:

-   The **verify** command configures SignTool to verify the signature in the specified [catalog file](catalog-files.md) (*tstamd64.cat*).

-   The **/kp** option configures SignTool to verify that the kernel policy has been met.

-   The **/v** option configures SignTool to print execution and warning messages.

-   The **/c** option specifies the driver package's [catalog file](catalog-files.md) which was released-signed (*tstamd64.cat*). If you are verifying the digital signature of an embedded-signed driver, do not use this option.

-   *amd64\\toaster.sys* is the name of the file to be verified.

Under the output from this command labeled "Signing Certificate Chain", you should verify that the following is true:

-   The root of the certificate chain for kernel policy is issued to and by the Microsoft Code Verification Root.

-   The cross-certificate, which is issued to the Class 3 Public Primary Certification Authority, is also issued by the Microsoft Code Verification Root.

For a signed catalog file, the Default Authenticode verification policy signature can also be verified on any kernel-mode binary file within the driver package. This ensures that the file appears as signed in the user-mode Plug and Play installation dialog boxes and the MMC Device Manager snap-in.

**Note**  This example is used only for verification of release-signed [catalog files](catalog-files.md) and not embedded-signed kernel-mode binary files.

 

The following example verifies the Default Authenticode verification policy of *toaster.sys* in the *tstamd64.cat* signed catalog file:

```cpp
Signtool verify /pa /v /c tstamd64.cat amd64\toaster.sys
```

Where:

- The **verify** command configures SignTool to verify the signature in the specified file<em>.</em>

- The **/pa** option configures SignTool to verify that the Authenticode verification policy has been met.

- The **/v** option configures SignTool to print execution and warning messages.

- The **/c** option specifies the driver package's [catalog file](catalog-files.md) that was released-signed (*tstamd64.cat*).

- *amd64\\toaster.sys* is the name of the file to be verified.

Under the output from this command labeled "Signing Certificate Chain," you should verify that the default Authenticode certificate chain is issued to and by a Class 3 Public Primary Certification Authority.

You can also verify the digital signature of the catalog file itself through Windows Explorer by following these steps:

-   Right-click the [catalog file](catalog-files.md) and select **Properties**.

-   For digitally signed files, the file's **Properties** dialog box has an additional **Digital Signature** tab, on which the signature, time stamp, and details of the certificate that was used to sign the file appear.

For more information about how to release-sign driver packages, see [Release-Signing Driver Packages](release-signing-driver-packages.md) and [Verifying the SPC Signature of a Catalog File](verifying-the-spc-signature-of-a-catalog-file.md).

 

 





