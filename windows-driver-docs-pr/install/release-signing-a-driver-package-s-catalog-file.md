---
title: Release-Signing a Driver Package's Catalog File
description: Release-Signing a Driver Package's Catalog File
ms.assetid: 8bfedf24-403a-406e-993d-5ab8cc790f60
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Release-Signing a Driver Package's Catalog File


Once the [catalog file](catalog-files.md) for a [driver package](driver-packages.md) is created or updated, the catalog file can be signed through [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778). Once signed, the digital signature stored within the catalog file is invalidated if any components of the driver package are modified.

When digitally signing a catalog file, SignTool saves the digital signature within the catalog file. The components of the driver package are not changed by SignTool. However, since the catalog file contains hashed values of the components of the driver package, the digital signature within the catalog file is maintained as long as the components hash to the same value.

SignTool can also add a time stamp to the digital signature. The time stamp lets you determine when a signature was created and supports more flexible certificate revocation options, if necessary.

The following command line shows how to run SignTool to do the following:

-   Release-sign the *tstamd64.cat* catalog file of the *ToastPkg* sample [driver package](driver-packages.md). For more information about how this [catalog file](catalog-files.md) was created, see [Creating a Catalog File for Release-Signing a Driver Package](creating-a-catalog-file-for-release-signing-a-driver-package.md).

-   Use a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) issued by a commercial certificate authority (CA).

-   Use a compatible cross-certificate for SPC.

-   Assign a time stamp to the digital signature through a time stamp authority (TSA).

To release-sign the *tstamd64.cat* catalog file, run the following command line:

```cpp
Signtool sign /v /ac MSCV-VSClass3.cer /s MyPersonalStore /n contoso.com /t http://timestamp.verisign.com/scripts/timstamp.dll tstamd64.cat
```

Where:

-   The **sign** command configures SignTool to sign the specified catalog file, *tstamd64.cat*.

-   The **/v** option enables verbose operations, in which SignTool displays successful execution and warning messages.

-   The **/ac** option specifies the name of the file which contains the cross-certificate (*MSCV-VSClass3.cer*) obtained from the CA. Use the full path name if the cross-certificate is not in the current directory.

-   The **/s** option specifies the name of the Personal certificate store (*MyPersonalStore)* that contains the SPC.

-   The **/n** option specifies the name of the SPC (*Contoso.com)* that is installed in the specified certificate store.

-   The **/t** option specifies URL of the TSA (*http://timestamp.verisign.com/scripts/timstamp.dll*) which will timestamp the digital signature.
    **Important**   Including a time stamp provides the necessary information for key revocation in case the signer's code signing private key is compromised.

     

-   *tstamd64.cat* specifies the name of the catalog file, which will be digitally-signed.

For more information about SignTool and its command-line arguments, see [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778).

For more information about release-signing driver packages, see [Release-Signing Driver Packages](release-signing-driver-packages.md).

 

 





