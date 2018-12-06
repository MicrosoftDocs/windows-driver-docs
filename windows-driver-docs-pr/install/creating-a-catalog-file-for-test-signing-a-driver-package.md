---
title: Creating a Catalog File for Test-Signing a Driver Package
description: Creating a Catalog File for Test-Signing a Driver Package
ms.assetid: 0bbb4dfa-d203-4618-946e-95d2896081ac
keywords:
- test signing driver packages WDK , catalog files
- catalog files WDK driver signing , creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Catalog File for Test-Signing a Driver Package


The catalog (*.cat*) file contains the digital signature for all the files which are part of the [driver package](driver-packages.md). For more information, see [Catalog Files](catalog-files.md).

There are two ways to create a [catalog file](catalog-files.md):

-   If the driver package is installed through an INF file, use the [**Inf2Cat**](https://msdn.microsoft.com/library/windows/hardware/ff547089) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](using-inf2cat-to-create-a-catalog-file.md).

-   If the driver package is not installed through an INF file, use the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) tool to create a catalog file by using a manually-created Catalog Definition File (*.cdf*).

    For example, if the driver package is installed through an application, you may want to create a catalog file to digitally-sign all kernel-mode binary components of the package, such as the driver and any supporting *.dll* files. For more information about how to use the MakeCat tool, see [Using MakeCat to Create a Catalog File](using-makecat-to-create-a-catalog-file.md).

A catalog file is not needed to install the following types of drivers:

-   A [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

-   A driver that is installed by using an application that does not use a [catalog file](catalog-files.md).

For these types of drivers, you have to embed a digital signature within the driver. For more information about this procedure, see [Test-Signing a Driver through an Embedded Signature](test-signing-a-driver-through-an-embedded-signature.md).

For more information about how to create catalog files, see [Creating a Catalog File for a Test-Signed Driver Package](creating-a-catalog-file-for-a-test-signed-driver-package.md).

 

 





