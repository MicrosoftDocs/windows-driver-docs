---
title: Constraints Between Selections and Installations
description: Constraints between selections and installations
keywords:
- installation constraints WDK Unidrv
- selection constraints WDK Unidrv
ms.date: 06/16/2023
---

# Constraints between selections and installations

[!include[Print Support Apps](../includes/print-support-apps.md)]

Sometimes it's necessary to specify that a certain option can't be selected if some other option is installed, or that a certain option can't be selected if some other option isn't installed. For example, a user shouldn't be able to select tabloid paper if a printer's large format paper tray isn't installed.

To specify relationships between the selection of certain options with the installation state of other options, use \***InstalledConstraints** and \***NotInstalledConstraints** entries. Their format is:

InstalledConstraints: *FeatureName.*OptionName*

NotInstalledConstraints: *FeatureName.*OptionName*

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature. If the argument is a feature, the period and *OptionName* aren't included.

An \***InstalledConstraints** or \***NotInstalledConstraints** entry must be placed inside a \*Feature or \*Option entry. For example, to indicate that a user shouldn't be able to select tabloid paper if a printer's large format paper tray isn't installed, the following entries can be used:

```GPD
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
