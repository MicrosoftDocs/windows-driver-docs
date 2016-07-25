---
title: Installing a Catalog File by using CryptCATAdminAddCatalog
description: Installing a Catalog File by using CryptCATAdminAddCatalog
ms.assetid: 2ab71f74-5a94-4f07-bd08-d3f5f6b6a785
---

# Installing a Catalog File by using CryptCATAdminAddCatalog


An installation program can use the [CryptCATAdminAddCatalog](http://go.microsoft.com/fwlink/p/?linkid=104926) and other **CryptCATAdmin*Xxx*** cryptography functions to programmatically install a [catalog file](catalog-files.md) in the system component and driver database.

The installation program must use the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 in the following way:

-   The source files of the installation program must include the following header (*.h*) files:
    -   *Mscat.h*, which defines the prototypes and structures for the various **CryptCATAdmin*Xxx*** functions.
    -   *Softpub.h*, which defines the various data structures and GUIDs that are used by the **CryptCATAdmin*Xxx*** functions.
-   The installation program must link to *Wintrust.lib*.

To use these **CryptCATAdmin*Xxx*** cryptography functions, an installation program does the following:

1.  Calls [CryptCATAdminAcquireContext](http://go.microsoft.com/fwlink/p/?linkid=105783) to obtain a handle to a catalog administrator context. The application identifies the subsystem by setting the *pgSubsystem* input parameter to a pointer to the GUID DRIVER\_ACTION\_VERIFY. This GUID is defined in *Softpub.h*.

2.  Calls [CryptCATAdminAddCatalog](http://go.microsoft.com/fwlink/p/?linkid=136382) to add the [catalog file](catalog-files.md) to the system component and driver database. The installation program supplies the handle to the catalog administrator context that was obtained in step 1, a pointer to the fully qualified path of the catalog file, and a pointer to the name of the catalog file that the function uses to install a copy of the catalog file in the database. The function returns a handle to the catalog information context for the catalog file that was added to the database.

3.  Calls [CryptCATAdminReleaseCatalogContext](http://go.microsoft.com/fwlink/p/?linkid=105784) to release the handle to the catalog information context for the catalog file. The installation program supplies the handle to the catalog administrator context that was obtained in step 1 and the handle to the catalog information context that was returned in step 2.

4.  Calls [CryptCATAdminReleaseContext](http://go.microsoft.com/fwlink/p/?linkid=105785) to release the handle to the catalog administrator context. The application supplies the handle to the catalog administrator context that was obtained in step 1.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Catalog%20File%20by%20using%20CryptCATAdminAddCatalog%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




