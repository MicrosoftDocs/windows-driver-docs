---
title: MakeCat
description: MakeCat
ms.assetid: 348c5069-0360-4ff9-897e-9a8832ac196c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MakeCat


MakeCat (Makecat.exe) is a command-line [CryptoAPI](https://go.microsoft.com/fwlink/p/?linkid=136391) tool that creates a [catalog file](https://docs.microsoft.com/windows-hardware/drivers/install/catalog-files) for a [driver package](https://docs.microsoft.com/windows-hardware/drivers/install/driver-packages).

For more information about the MakeCat tool and its command-line arguments, see the [Using MakeCat](https://go.microsoft.com/fwlink/p/?linkid=70086) website.

For more information about how to use the MakeCat tool, see [Creating a Catalog File for Release-Signing a Driver Package](https://docs.microsoft.com/windows-hardware/drivers/install/creating-a-catalog-file-for-release-signing-a-driver-package).

**Note**   You must use the MakeCat tool only to create catalog files for driver packages that are not installed by using an INF file. If the driver package is installed by using an INF file, use the [**Inf2Cat**](inf2cat.md) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](https://docs.microsoft.com/windows-hardware/drivers/install/using-inf2cat-to-create-a-catalog-file).

 

 

 





