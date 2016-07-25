---
title: Installing a Release-Signed Catalog File for a Non-PnP Driver
description: Installing a Release-Signed Catalog File for a Non-PnP Driver
ms.assetid: a67f3b71-b7a6-4712-a76f-b3b412a149c2
---

# Installing a Release-Signed Catalog File for a Non-PnP Driver


To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, a non-boot, non-PnP kernel-mode driver must have either an embedded release signature or a released-signed [catalog file](catalog-files.md) that is installed in the system component and driver database. In addition, if you use a release-signed catalog file to authenticate a user-mode driver or a 32-bit non-PnP kernel-mode driver, the Windows code-signing policy requires that the catalog file be installed in the system component and driver database. PnP device installation automatically installs the catalog file of a PnP driver in the driver database. However, for non-PnP drivers, the installation application that installs a non-PnP driver must install the catalog file in the driver database.

To install a catalog file for a non-PnP driver that is released to the public, a redistributable installation application should use the [CryptCATAdminAddCatalog](http://go.microsoft.com/fwlink/p/?linkid=104926) cryptography function, as described in [Installing a Catalog File by using CryptCATAdminAddCatalog](installing-a-catalog-file-by-using-cryptcatadminaddcatalog.md).

**Note**   In general, a redistributable installation application cannot use the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool to install a catalog file because SignTool is not a redistributable tool.

 

**Tip**   Using embedded signatures is generally easier and more efficient than by using a signed catalog file. For more information about the advantages and disadvantages of using embedded signatures versus signed catalog files, see [Test Signing a Driver](https://msdn.microsoft.com/windows-drivers/develop/signing_a_driver).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Release-Signed%20Catalog%20File%20for%20a%20Non-PnP%20Driver%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




