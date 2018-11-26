---
title: Constraints between Selections and Installations
description: Constraints between Selections and Installations
ms.assetid: abb6004f-daae-4f28-b36c-102d0b8c9f55
keywords:
- installation constraints WDK Unidrv
- selection constraints WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Constraints between Selections and Installations





Sometimes it is necessary to specify that a certain option cannot be selected if some other option is installed, or that a certain option cannot be selected if some other option is not installed. For example, a user should not be able to select tabloid paper if a printer's large format paper tray is not installed.

To specify relationships between the selection of certain options with the installation state of other options, use \***InstalledConstraints** and \***NotInstalledConstraints** entries. Their format is:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><em>InstalledConstraints : <em>FeatureName</em> . <em>OptionName</em></p></td>
</tr>
<tr class="even">
<td><p></em>NotInstalledConstraints : <em>FeatureName</em> . <em>OptionName</em></p></td>
</tr>
</tbody>
</table>

 

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature. If the argument is a feature, the period and *OptionName* are not included.

An \***InstalledConstraints** or \***NotInstalledConstraints** entry must be placed inside a \*Feature or \*Option entry. For example, to indicate that a user should not be able to select tabloid paper if a printer's large format paper tray is not installed, the following entries can be used:

```cpp
*Feature: InputBin
{
    *Option: LARGEFMT
    {
        Installable?: TRUE
        NotInstalledConstraints: PaperSize.TABLOID
    }
}
```

If a feature or option includes an \***InstalledConstraints** or \***NotInstalledConstraints** entry, the feature or option's \*Installable? attribute must be set to **TRUE**.

 

 




