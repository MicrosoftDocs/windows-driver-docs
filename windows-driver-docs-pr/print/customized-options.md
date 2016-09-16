---
title: Customized Options
author: windows-driver-content
description: Customized Options
MS-HAID:
- 'nt5gpd\_3a366d4d-1c80-4529-9602-f7adf74c7c06.xml'
- 'print.customized\_options'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8b54c59e-b469-488a-ae31-52045c00c971
keywords: ["printer options WDK Unidrv , customized", "customized printer options WDK Unidrv"]
---

# Customized Options


## <a href="" id="ddk-customized-options-gg"></a>


Customized options are those that are not defined by predefined names in the GPD language. You must create unique names for these options.

Customized options can be associated with customized features. For an example of customized options associated with customized features, see [Customized Features](customized-features.md).

You can also specify customized options for some of the [standard features](standard-features.md). For example, if your printer provides a paper size that is not described by one of the standard options for the **PaperSize** feature, you can specify a customized paper size option by creating a unique name for the option.

Customized option names must be unique within a feature, but option names can be reused in different features. Also, you can use standard option names within customized features. Thus, for example, you can use the standard option names ON and OFF within several \*[Feature](feature-entry-format.md) entries for customized features.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20Options%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


