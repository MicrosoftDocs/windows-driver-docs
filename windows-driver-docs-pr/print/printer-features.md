---
title: Printer Features
author: windows-driver-content
description: Printer Features
MS-HAID:
- 'nt5gpd\_f534334d-716c-4ec0-bae5-288069e289d0.xml'
- 'print.printer\_features'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: eabbb833-2c0a-4a55-bfa4-a3dc0619c22c
keywords: ["Unidrv, printer features", "GPD files WDK Unidrv , printer features", "printer features WDK Unidrv", "printer features WDK Unidrv , about printer features", "Unidrv WDK print"]
---

# Printer Features


## <a href="" id="ddk-printer-features-gg"></a>


Printer features are capabilities that can be controlled by the Unidrv driver. By listing a feature and its characteristics in a GPD file, you inform the Unidrv driver that your printer supports the feature.

Each printer feature can be assigned to one or more states, and [printer options](printer-options.md) are used to define the possible states. For example, if your printer accepts both letter-sized and legal-sized pages, your GPD file should specify the PaperSize feature, along with the Letter and Legal options.

All features and their associated options are listed on either the printer property sheet or the document property sheet associated with the printer. For more information about these property sheets, see [Unidrv User Interface](unidrv-user-interface.md).

This section explains GPD language support for both [standard features](standard-features.md) and [customized features](customized-features.md). Additional topics in this section include [Feature Entry Format](feature-entry-format.md), [Feature Attributes](feature-attributes.md), and [Feature Conflict Priority](feature-conflict-priority.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Features%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


