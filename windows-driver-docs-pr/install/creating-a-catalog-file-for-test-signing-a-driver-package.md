---
title: Creating a Catalog File for Test-Signing a Driver Package
description: Creating a Catalog File for Test-Signing a Driver Package
keywords:
- test signing driver packages WDK , catalog files
- catalog files WDK driver signing , creating
ms.date: 02/11/2022
---

# Creating a Catalog File for Test-Signing a Driver Package


The catalog (*.cat*) file contains the digital signature for all the files which are part of the [driver package](driver-packages.md). For more information, see [Catalog Files](catalog-files.md).

There are two ways to create a [catalog file](catalog-files.md):

-   The [**Inf2Cat**](../devtest/inf2cat.md) tool can be used to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](using-inf2cat-to-create-a-catalog-file.md).

-   The [MakeCat](/windows/win32/seccrypto/makecat) tool can be used to create a catalog file by using a manually-created Catalog Definition File (*.cdf*). For more information about how to use the MakeCat tool, see [Using MakeCat to Create a Catalog File](using-makecat-to-create-a-catalog-file.md).

If the driver package contains a *boot-start driver*, you additionally have to embed a digital signature within the driver binary. For more information about this procedure, see [Test-Signing a Driver through an Embedded Signature](test-signing-a-driver-through-an-embedded-signature.md).

## See also

* [Creating a Catalog File for a PnP Driver Package](creating-a-catalog-file-for-a-pnp-driver-package.md)
* [Creating a Catalog File for a Non-PnP Driver Package](creating-a-catalog-file-for-a-non-pnp-driver-package.md)