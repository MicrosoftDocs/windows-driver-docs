---
title: Installing a Test-Signed Catalog File for a Non-PnP Driver
description: Installing a Test-Signed Catalog File for a Non-PnP Driver
ms.assetid: 8586bacc-86c5-4402-84fa-6f1efe967f5d
keywords: ["test signing driver packages WDK , catalog files", "CAT files", ".cat files", "non-PnP driver catalog files WDK driver signing"]
---

# Installing a Test-Signed Catalog File for a Non-PnP Driver


To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, a non-boot, non-PnP driver must have either an embedded signature or a signed [catalog file](catalog-files.md) that is installed in the system component and driver database. PnP device installation automatically installs the catalog file of a PnP driver in the driver database. However, for non-PnP drivers, the installation application that installs a non-PnP driver must install the catalog file in the driver database.

A driver installation application can programmatically install a catalog file in the system component and driver database by using the [CryptCATAdminAddCatalog](http://go.microsoft.com/fwlink/p/?linkid=104926) cryptography function. If the application is to be redistributable, you should use this approach to install the catalog file. For more information about this approach, see [Installing a Catalog File by using CryptCATAdminAddCatalog](installing-a-catalog-file-by-using-cryptcatadminaddcatalog.md).

Alternatively, you can use the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool to install a [catalog file](catalog-files.md) in the system component and driver database. However, SignTool is not a redistributable tool. Therefore, an installation application can use SignTool on a computer only if the tool is already installed on the computer in a manner that complies with the Microsoft Software License Terms for the tool. For more information about this approach, see [Installing a Catalog File by using SignTool](installing-a-catalog-file-by-using-signtool.md).

**Tip**   Using embedded signatures is generally easier and more efficient than by using a signed catalog file. For more information about the advantages and disadvantages of using embedded signatures versus signed catalog files, see [Test Signing a Driver](https://msdn.microsoft.com/windows-drivers/develop/signing_a_driver).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Test-Signed%20Catalog%20File%20for%20a%20Non-PnP%20Driver%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




