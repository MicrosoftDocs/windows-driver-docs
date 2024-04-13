---
title: Using MakeCat to Create a Catalog File
description: Using MakeCat to Create a Catalog File
ms.date: 02/11/2022
---

# Using MakeCat to Create a Catalog File

You can use the [MakeCat](/windows/win32/seccrypto/makecat) tool to create a [catalog file](catalog-files.md).

You must use the MakeCat tool only to create catalog files for files that are not installed by using an INF file. If the files are installed by using an INF file, use the [**Inf2Cat**](../devtest/inf2cat.md) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](using-inf2cat-to-create-a-catalog-file.md).

> [!NOTE]
> For any kernel-mode binaries that are a *boot-start driver*, you should also embed a signature in the binary. For more information about this procedure, see [Test-Signing a Driver through an Embedded Signature](test-signing-a-driver-through-an-embedded-signature.md).

To create a catalog file, you must first manually create a Catalog Definition File (*.cdf*) that describes the catalog header attributes and file entries. Once this file is created, you can then run the [MakeCat](/windows/win32/seccrypto/makecat) tool to create a catalog file. The MakeCat tool does the following when it processes the *.cdf* file:

-   Verifies the list of attributes for each file that is listed in the *.cdf* file.

-   Adds the listed attributes to the [catalog file](catalog-files.md).

-   Generates a cryptographic hash, or *thumbprint*, of each of the listed files.

-   Stores the thumbprint of each file in the catalog file.

This topic describes how to create a *.cdf* file for the 64-bit kernel-mode binary files of the *ToastPkg* sample driver package. Within the WDK installation directory, these binary files are located in the *src\\general\\toaster\\toastpkg\\toastcd\\amd64* directory.

To create a *.cdf* file for the *ToastPkg* sample [driver package](driver-packages.md), do the following:

1.  Start Notepad and copy the text from the following sample. It contains the list of files to be cataloged, along with their attributes.

    ```cpp
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

The following command line shows how to create a catalog file through the [MakeCat](/windows/win32/seccrypto/makecat) tool by using the *tstamd64.cdf* file:

```cpp
makecat -v tstamd64.cdf
```

After you run the tool, a file that is named *tstamd64.cat* is created.

For more information about the MakeCat tool and its command-line arguments, see the [Using MakeCat](/windows/win32/seccrypto/using-makecat) website.

For more information about how to use the MakeCat tool, see [Creating a Catalog File for a Non-PnP Driver Package](creating-a-catalog-file-for-a-non-pnp-driver-package.md).

