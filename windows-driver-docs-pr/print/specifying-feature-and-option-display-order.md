---
title: Specifying Feature and Option Display Order
description: Specifying Feature and Option Display Order
ms.assetid: 51e18121-540b-40f0-85f8-eb2755a583f7
keywords:
- Unidrv, feature and option display order
- display order of features/options WDK Unidrv
- property sheet pages WDK print , feature and option display order
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Feature and Option Display Order





To control the order in which features and options are displayed on Unidrv-generated property sheet pages, include empty \*Feature and \*Option entries in the GPD file. These entries must be placed towards the beginning of the file, before the appearance of full \*Feature and \*Option entries, and before any other references to feature or option names. The order in which the empty entries are listed is the order in which the features and options appear on the property sheet pages. (Note, however, that options of the PaperSize feature are always listed in alphabetical order, and this order cannot be changed.)

Following is an example of a set of empty \*Feature and \*Option entries:

```cpp
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

 

 




