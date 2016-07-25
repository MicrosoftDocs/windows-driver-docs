---
title: Release-Signing a Driver Package's Catalog File
description: Release-Signing a Driver Package's Catalog File
ms.assetid: 8bfedf24-403a-406e-993d-5ab8cc790f60
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Release-Signing%20a%20Driver%20Package's%20Catalog%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




