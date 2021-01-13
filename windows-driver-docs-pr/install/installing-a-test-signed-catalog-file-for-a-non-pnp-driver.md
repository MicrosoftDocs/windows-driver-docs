---
title: Installing a Test-Signed Catalog File for a Non-PnP Driver
description: Installing a Test-Signed Catalog File for a Non-PnP Driver
keywords:
- test signing driver packages WDK , catalog files
- CAT files
- .cat files
- non-PnP driver catalog files WDK driver signing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Test-Signed Catalog File for a Non-PnP Driver


To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, a non-boot, non-PnP driver must have either an embedded signature or a signed [catalog file](catalog-files.md) that is installed in the system component and driver database. PnP device installation automatically installs the catalog file of a PnP driver in the driver database. However, for non-PnP drivers, the installation application that installs a non-PnP driver must install the catalog file in the driver database.

A driver installation application can programmatically install a catalog file in the system component and driver database by using the [CryptCATAdminAddCatalog](/windows/win32/api/mscat/nf-mscat-cryptcatadminaddcatalog) cryptography function. If the application is to be redistributable, you should use this approach to install the catalog file. For more information about this approach, see [Installing a Catalog File by using CryptCATAdminAddCatalog](installing-a-catalog-file-by-using-cryptcatadminaddcatalog.md).

Alternatively, you can use the [**SignTool**](../devtest/signtool.md) tool to install a [catalog file](catalog-files.md) in the system component and driver database. However, SignTool is not a redistributable tool. Therefore, an installation application can use SignTool on a computer only if the tool is already installed on the computer in a manner that complies with the Microsoft Software License Terms for the tool. For more information about this approach, see [Installing a Catalog File by using SignTool](installing-a-catalog-file-by-using-signtool.md).

**Tip**   Using embedded signatures is generally easier and more efficient than by using a signed catalog file. For more information about the advantages and disadvantages of using embedded signatures versus signed catalog files, see [Test Signing a Driver](/windows-hardware/drivers).

 

