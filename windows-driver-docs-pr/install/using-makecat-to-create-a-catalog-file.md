---
title: Using MakeCat to Create a Catalog File
description: Using MakeCat to Create a Catalog File
ms.assetid: c9f9360b-2b1d-4060-af4d-8d281319e181
---

# Using MakeCat to Create a Catalog File


You can use the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) tool to create a [catalog file](catalog-files.md) for a [driver package](driver-packages.md).

You must use the MakeCat tool only to create catalog files for driver packages that are not installed by using an INF file. If the driver package is installed by using an INF file, use the [**Inf2Cat**](https://msdn.microsoft.com/library/windows/hardware/ff547089) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](using-inf2cat-to-create-a-catalog-file.md).

**Note**  Instead of creating and signing a catalog file, you can also embed a signature in the kernel-mode binaries of your [driver package](driver-packages.md), such as the driver and any .dll files your package may provide. For more information about this procedure, see [Test-Signing a Driver through an Embedded Signature](test-signing-a-driver-through-an-embedded-signature.md).

 

To create a catalog file, you must first manually create a Catalog Definition File (*.cdf*) that describes the catalog header attributes and file entries. Once this file is created, you can then run the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) tool to create a catalog file. The MakeCat tool does the following when it processes the *.cdf* file:

-   Verifies the list of attributes for each file that is listed in the *.cdf* file.

-   Adds the listed attributes to the [catalog file](catalog-files.md).

-   Generates a cryptographic hash, or *thumbprint*, of each of the listed files.

-   Stores the thumbprint of each file in the catalog file.

This topic describes how to create a *.cdf* file for the 64-bit kernel-mode binary files of the *ToastPkg* sample driver package. Within the WDK installation directory, these binary files are located in the *src\\general\\toaster\\toastpkg\\toastcd\\amd64* directory.

To create a *.cdf* file for the *ToastPkg* sample [driver package](driver-packages.md), do the following:

1.  Start Notepad and copy the text from the following sample. It contains the list of files to be cataloged, along with their attributes.

    ```
    [CatalogHeader]
    Name=tstamd64.cat
    PublicVersion=0x0000001
    EncodingType=0x00010001
    CATATTR1=0x10010001:OSAttr:2:6.0
    [CatalogFiles]
    <hash>File1=amd64\toaster.pdb
    <hash>File2=amd64\toaster.sys
    <hash>File3=amd64\toastva.exe
    <hash>File4=amd64\toastva.pdb
    <hash>File5=amd64\tostrcls.dll
    <hash>File6=amd64\tostrcls.pdb
    <hash>File7=amd64\tostrco2.dll
    <hash>File8=amd64\tostrco2.pdb
    ```

2.  Save the file as *tstamd64.cdf* in the same folder as the driver package.
    **Note**  When building a driver for multiple platforms, create a separate catalog file for each platform.

     

The following command line shows how to create a catalog file through the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) tool by using the *tstamd64.cdf* file:

```
makecat -v tstamd64.cdf
```

After you run the tool, a file that is named *tstamd64.cat* is created.

For more information about the MakeCat tool and its command-line arguments, see the [Using MakeCat](http://go.microsoft.com/fwlink/p/?linkid=70086) website.

For more information about how to use the MakeCat tool, see [Creating a Catalog File for a Non-PnP Driver Package](creating-a-catalog-file-for-a-non-pnp-driver-package.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20MakeCat%20to%20Create%20a%20Catalog%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




