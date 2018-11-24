---
title: Feature Entry Format
description: Feature Entry Format
ms.assetid: f4e91611-aa68-4426-82ef-9ad3f09d62f2
keywords:
- printer features WDK Unidrv , entry format
- formats WDK printer features
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Feature Entry Format





To specify a printer feature entry in a GPD file, use the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*Feature: <em>FeatureName</em> {<em>FeatureAttributes</em>}</p></td>
</tr>
</tbody>
</table>

 

where *FeatureName* is the name of either one of the predefined [standard features](standard-features.md) or a customized feature name, and *FeatureAttributes* is a set of [feature attributes](feature-attributes.md).

For example, a GPD file might contain the following specification of the standard InputBin feature.

```cpp
*Feature: InputBin
{
    *Name: "Paper Bin"
    *DefaultOption: Upper
    *Option: Upper
    {
        *Name: "Upper Tray"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.10
            *Cmd: "<1B>&l1H"
        }
        *Constraints: PaperSize.Env10
    }
    *Option: Manual
    {
        *Name: "Manual Feed"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.10
            *Cmd: "<1B>&l2H"
        }
        *Installable?: TRUE
    }
}
```

If you repeat a feature specification by, for example, including two or more InputBin feature entries, then the following rules apply:

-   Attributes and options that are not duplicated are added to Unidrv's database.

-   Attributes and options that are duplicated are overwritten, and Unidrv retains only the last specification.

You can control the order in which features are displayed to the user. See [Specifying Feature and Option Display Order](specifying-feature-and-option-display-order.md).

 

 




