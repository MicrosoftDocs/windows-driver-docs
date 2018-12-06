---
title: MakeCat
description: MakeCat
ms.assetid: 348c5069-0360-4ff9-897e-9a8832ac196c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MakeCat


MakeCat (Makecat.exe) is a command-line [CryptoAPI](http://go.microsoft.com/fwlink/p/?linkid=136391) tool that creates a [catalog file](https://msdn.microsoft.com/library/windows/hardware/ff537872) for a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).

For more information about the MakeCat tool and its command-line arguments, see the [Using MakeCat](http://go.microsoft.com/fwlink/p/?linkid=70086) website.

For more information about how to use the MakeCat tool, see [Creating a Catalog File for Release-Signing a Driver Package](https://msdn.microsoft.com/library/windows/hardware/ff540172).

**Note**   You must use the MakeCat tool only to create catalog files for driver packages that are not installed by using an INF file. If the driver package is installed by using an INF file, use the [**Inf2Cat**](inf2cat.md) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](https://msdn.microsoft.com/library/windows/hardware/ff553618).

 

 

 





