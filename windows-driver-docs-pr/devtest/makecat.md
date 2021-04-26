---
title: MakeCat
description: MakeCat
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MakeCat


MakeCat (Makecat.exe) is a command-line [CryptoAPI](/windows/win32/seccrypto/cryptography-portal) tool that creates a [catalog file](../install/catalog-files.md) for a [driver package](../install/driver-packages.md).

For more information about the MakeCat tool and its command-line arguments, see the [Using MakeCat](/windows/win32/seccrypto/using-makecat) website.

For more information about how to use the MakeCat tool, see [Creating a Catalog File for Release-Signing a Driver Package](../install/creating-a-catalog-file-for-release-signing-a-driver-package.md).

**Note**   You must use the MakeCat tool only to create catalog files for driver packages that are not installed by using an INF file. If the driver package is installed by using an INF file, use the [**Inf2Cat**](inf2cat.md) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](../install/using-inf2cat-to-create-a-catalog-file.md).

 

 

