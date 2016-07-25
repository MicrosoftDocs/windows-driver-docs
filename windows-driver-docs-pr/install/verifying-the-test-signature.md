---
title: Verifying the Test Signature
description: Verifying the Test Signature
ms.assetid: 996ce3d4-76b5-4c78-9ea9-ca8a04cfef99
---

# Verifying the Test Signature


After the test certificate is copied to the Trusted Root Certification Authorities certificate store on the test computer, [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) can be used to do the following:

-   Verify the signature of a specified file in a [driver package's](driver-packages.md) [catalog files](catalog-files.md).

-   Verify the embedded signature of a kernel-mode binary file, such as a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

The following example verifies the signature for one of the files, *toastpkg.inf*, in the Toastpkg sample's signed catalog file, *tstamd64.cat*. For more information about how this catalog file was created, see [Using Inf2Cat to Create a Catalog File](using-inf2cat-to-create-a-catalog-file.md):

```
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

```
Signtool verify /pa /v tstamd64.cat
```

For more information about how to use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to verify a digital signature of a catalog file, see [Verifying the Signature of a Test-Signed Catalog File](verifying-the-signature-of-a-test-signed-catalog-file.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Verifying%20the%20Test%20Signature%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




