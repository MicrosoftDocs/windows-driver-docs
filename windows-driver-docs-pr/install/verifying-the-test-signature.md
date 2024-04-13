---
title: Verifying the Test Signature
description: Verifying the Test Signature
ms.date: 04/20/2017
---

# Verifying the Test Signature


After the test certificate is copied to the Trusted Root Certification Authorities certificate store on the test computer, [**SignTool**](../devtest/signtool.md) can be used to do the following:

-   Verify the signature of a specified file in a [driver package's](driver-packages.md) [catalog files](catalog-files.md).

-   Verify the embedded signature of a kernel-mode binary file, such as a *boot-start driver*.

The following example verifies the signature for one of the files, *toastpkg.inf*, in the Toastpkg sample's signed catalog file, *tstamd64.cat*. For more information about how this catalog file was created, see [Using Inf2Cat to Create a Catalog File](using-inf2cat-to-create-a-catalog-file.md):

```cpp
Signtool verify /pa /v /c tstamd64.cat toastpkg.inf
```

Where:

-   The **verify** command configures SignTool to verify the specified file, t*oastpkg.inf*.

-   The **/pa** option specifies the use of the Authenticode verification policy when verifying the digital signature.

-   The **/v** option enables verbose operations, in which SignTool displays successful execution and warning messages.

-   The **/c** option specifies the catalog file name.

    **Note**  When verifying the signature of an embedded-signed kernel-mode binary file, do not use the **/c** argument.

     

-   *toastpkg.inf* specifies the name of the file to be verified.

The following example verifies the signature of the *Toastpkg* sample's signed catalog file, *Tstamd64.cat*:

```cpp
Signtool verify /pa /v tstamd64.cat
```

For more information about how to use [**SignTool**](../devtest/signtool.md) to verify a digital signature of a catalog file, see [Verifying the Signature of a Test-Signed Catalog File](verifying-the-signature-of-a-test-signed-catalog-file.md).

 

