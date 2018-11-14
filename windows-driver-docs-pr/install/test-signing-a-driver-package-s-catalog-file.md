---
title: Test-Signing a Driver Package's Catalog File
description: Test-Signing a Driver Package's Catalog File
ms.assetid: 8cc54f57-bac3-45a1-b780-48626943b446
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Test-Signing a Driver Package's Catalog File


After the [catalog file](catalog-files.md) for a [driver package](driver-packages.md) is created or updated, the catalog file can be signed through [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778). Once signed, the digital signature stored within the catalog file is invalidated if any components of the driver package are modified.

When digitally signing a catalog file, SignTool saves the digital signature within the catalog file. The components of the driver package are not changed by SignTool. However, since the catalog file contains hashed values of the components of the driver package, the digital signature within the catalog file is maintained as long as the components hash to the same value.

SignTool can also add a time stamp to the digital signature. The time stamp allows you to determine when a signature was created and supports more flexible certificate revocation options, if necessary.

The following command line shows how to run SignTool to do the following:

-   Test-sign the *tstamd64.cat* catalog file of the *ToastPkg* sample [driver package](driver-packages.md). For more information about how this [catalog file](catalog-files.md) was created, see [Creating a Catalog File for Test-Signing a Driver Package](creating-a-catalog-file-for-test-signing-a-driver-package.md).

-   Use the Contoso.com(Test) certificate from the PrivateCertStore for the test signature. For more information about how this certificate was created, see [Creating Test Certificates](creating-test-certificates.md).

-   Timestamps the digital signature through a time stamp authority (TSA).

To test-sign the *tstamd64.cat* catalog file, run the following command line:

```cpp
Signtool sign /v /s PrivateCertStore /n Contoso.com(Test) /t http://timestamp.verisign.com/scripts/timstamp.dll tstamd64.cat
```

Where:

-   The **sign** command configures SignTool to sign the specified catalog file, tstamd64.cat.

-   The **/v** option enables verbose operations, in which SignTool displays successful execution and warning messages.

-   The **/s** option specifies the name of the certificate store (*PrivateCertStore)* that contains the test certificate.

-   The **/n** option specifies the name of the certificate (*Contoso.com(Test))* that is installed in the specified certificate store.

-   The **/t** option specifies URL of the TSA (*http://timestamp.verisign.com/scripts/timstamp.dll*) which will time stamp the digital signature.
    **Important**   Including a time stamp provides the necessary information for key revocation in case the signer's code signing private key is compromised.

     

-   *tstamd64.cat* specifies the name of the catalog file, which will be digitally-signed.

For more information about SignTool and its command-line arguments, see [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778).

For more information about test-signing a driver package's catalog file, see [Test-Signing a Catalog File](test-signing-a-catalog-file.md).

 

 





