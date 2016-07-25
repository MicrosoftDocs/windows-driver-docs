---
title: Creating a Catalog File for Test-Signing a Driver Package
description: Creating a Catalog File for Test-Signing a Driver Package
ms.assetid: 0bbb4dfa-d203-4618-946e-95d2896081ac
keywords: ["test signing driver packages WDK , catalog files", "catalog files WDK driver signing , creating"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Creating%20a%20Catalog%20File%20for%20Test-Signing%20a%20Driver%20Package%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




