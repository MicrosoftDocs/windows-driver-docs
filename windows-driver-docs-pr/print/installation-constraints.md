---
title: Installation constraints
description: Installation constraints
keywords:
- installation constraints WDK Unidrv
ms.date: 06/26/2023
---

# Installation constraints

[!include[Print Support Apps](../includes/print-support-apps.md)]

Sometimes, certain installable printer options can't be installed simultaneously. For example, it might not be possible to install both the envelope feeder and the duplexing unit.

To specify combinations of printer options that can't be simultaneously installed, use \*InvalidInstallableCombination entries.

The \*InvalidInstallableCombination entry has the following format:

\***InvalidInstallableCombination: LIST** (*FeatureName*.*OptionName*,*FeatureName*.*OptionName*, ...)

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature. This list can include features as well as options, in which case the period and *OptionName* aren't included.

The features and options listed in a single \*InvalidInstallableCombination entry indicate a set of features and options that can't be used in combination. For example, the following entry specifies that the envelope feeder and the duplexing unit can't be simultaneously installed.

```GPD
*InvalidInstallableCombination: LIST(InputBin.ENVFEED, Duplex)
```

All \*InvalidInstallationCombination entries must be located at the GPD file's root level (that is, not within braces). The number of features and options included in an entry isn't limited.

If a feature or option is included in an \*InvalidInstallationCombination entry, the feature or option's \*Installable? attribute must be set to **TRUE**.
