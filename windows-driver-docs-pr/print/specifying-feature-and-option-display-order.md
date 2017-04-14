---
title: Specifying Feature and Option Display Order
author: windows-driver-content
description: Specifying Feature and Option Display Order
ms.assetid: 51e18121-540b-40f0-85f8-eb2755a583f7
keywords: ["Unidrv, feature and option display order", "display order of features/options WDK Unidrv", "property sheet pages WDK print , feature and option display order", "Unidrv WDK print"]
---

# Specifying Feature and Option Display Order


## <a href="" id="ddk-specifying-feature-and-option-display-order-gg"></a>


To control the order in which features and options are displayed on Unidrv-generated property sheet pages, include empty \*Feature and \*Option entries in the GPD file. These entries must be placed towards the beginning of the file, before the appearance of full \*Feature and \*Option entries, and before any other references to feature or option names. The order in which the empty entries are listed is the order in which the features and options appear on the property sheet pages. (Note, however, that options of the PaperSize feature are always listed in alphabetical order, and this order cannot be changed.)

Following is an example of a set of empty \*Feature and \*Option entries:

```
*Feature: EconoMode
{
    *Option: Off{}
    *Option: On{}
}
*Feature: Orientation
{
    *Option: PORTRAIT{}
    *Option: LANDSCAPE_CC90{}
}
*Feature: PaperSize
{
}
*Feature: Resolution
{
    *Option: Option1{}
    *Option: Option2{}
    *Option: Option3{}
}
```

The example specifies the order in which the EconoMode, Orientation, PaperSize, and Resolution features are displayed. Additionally, it specifies the display order for the EconoMode, Orientation, and Resolution options. PaperSize options are displayed in alphabetical order.

If a GPD file does not include empty \*Feature and \*Option entries specifying the display order, the GPD parser determines the display order. While the parser generally causes features and options to be displayed in the order they appear in a GPD file, this order is not guaranteed. Additionally, by default the parser always causes the InputBin feature to be displayed first.

Including empty \*Feature and \*Option entries to explicitly specify display order is recommended over allowing the parser to create the order.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Specifying%20Feature%20and%20Option%20Display%20Order%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


