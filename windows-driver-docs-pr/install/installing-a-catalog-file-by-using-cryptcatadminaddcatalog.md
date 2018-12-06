---
title: Installing a Catalog File by using CryptCATAdminAddCatalog
description: Installing a Catalog File by using CryptCATAdminAddCatalog
ms.assetid: 2ab71f74-5a94-4f07-bd08-d3f5f6b6a785
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Catalog File by using CryptCATAdminAddCatalog


An installation program can use the [CryptCATAdminAddCatalog](http://go.microsoft.com/fwlink/p/?linkid=104926) and other **CryptCATAdmin*Xxx*** cryptography functions to programmatically install a [catalog file](catalog-files.md) in the system component and driver database.

The installation program must use the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 in the following way:

- The source files of the installation program must include the following header (*.h*) files:
  - *Mscat.h*, which defines the prototypes and structures for the various **CryptCATAdmin*Xxx*** functions.
  - *Softpub.h*, which defines the various data structures and GUIDs that are used by the **CryptCATAdmin*Xxx*** functions.

- The installation program must link to *Wintrust.lib*.

To use these **CryptCATAdmin*Xxx*** cryptography functions, an installation program does the following:

1.  Calls [CryptCATAdminAcquireContext](http://go.microsoft.com/fwlink/p/?linkid=105783) to obtain a handle to a catalog administrator context. The application identifies the subsystem by setting the *pgSubsystem* input parameter to a pointer to the GUID DRIVER_ACTION_VERIFY. This GUID is defined in *Softpub.h*.

2.  Calls [CryptCATAdminAddCatalog](http://go.microsoft.com/fwlink/p/?linkid=136382) to add the [catalog file](catalog-files.md) to the system component and driver database. The installation program supplies the handle to the catalog administrator context that was obtained in step 1, a pointer to the fully qualified path of the catalog file, and a pointer to the name of the catalog file that the function uses to install a copy of the catalog file in the database. The function returns a handle to the catalog information context for the catalog file that was added to the database.

3.  Calls [CryptCATAdminReleaseCatalogContext](http://go.microsoft.com/fwlink/p/?linkid=105784) to release the handle to the catalog information context for the catalog file. The installation program supplies the handle to the catalog administrator context that was obtained in step 1 and the handle to the catalog information context that was returned in step 2.

4.  Calls [CryptCATAdminReleaseContext](http://go.microsoft.com/fwlink/p/?linkid=105785) to release the handle to the catalog administrator context. The application supplies the handle to the catalog administrator context that was obtained in step 1.









