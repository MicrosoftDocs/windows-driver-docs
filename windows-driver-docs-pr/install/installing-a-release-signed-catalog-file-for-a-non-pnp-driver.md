---
title: Installing a Release-Signed Catalog File for a Non-PnP Driver
description: Installing a Release-Signed Catalog File for a Non-PnP Driver
ms.assetid: a67f3b71-b7a6-4712-a76f-b3b412a149c2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Release-Signed Catalog File for a Non-PnP Driver


To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, a non-boot, non-PnP kernel-mode driver must have either an embedded release signature or a released-signed [catalog file](catalog-files.md) that is installed in the system component and driver database. In addition, if you use a release-signed catalog file to authenticate a user-mode driver or a 32-bit non-PnP kernel-mode driver, the Windows code-signing policy requires that the catalog file be installed in the system component and driver database. PnP device installation automatically installs the catalog file of a PnP driver in the driver database. However, for non-PnP drivers, the installation application that installs a non-PnP driver must install the catalog file in the driver database.

To install a catalog file for a non-PnP driver that is released to the public, a redistributable installation application should use the [CryptCATAdminAddCatalog](http://go.microsoft.com/fwlink/p/?linkid=104926) cryptography function, as described in [Installing a Catalog File by using CryptCATAdminAddCatalog](installing-a-catalog-file-by-using-cryptcatadminaddcatalog.md).

**Note**   In general, a redistributable installation application cannot use the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool to install a catalog file because SignTool is not a redistributable tool.

 

**Tip**   Using embedded signatures is generally easier and more efficient than by using a signed catalog file. For more information about the advantages and disadvantages of using embedded signatures versus signed catalog files, see [Test Signing a Driver](https://msdn.microsoft.com/windows-drivers/develop/signing_a_driver).

 

 

 





