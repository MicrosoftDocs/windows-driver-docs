---
title: Installation Constraints
description: Installation Constraints
ms.assetid: 0adf5a6a-e9de-4bb0-bf1c-fe7eef565840
keywords:
- installation constraints WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installation Constraints





Sometimes, certain installable printer options cannot be installed simultaneously. For example, it might not be possible to install both the envelope feeder and the duplexing unit.

To specify combinations of printer options that cannot be simultaneously installed, use \*InvalidInstallableCombination entries.

The \*InvalidInstallableCombination entry has the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>*InvalidInstallableCombination: LIST (</strong><em>FeatureName</em> <strong>.</strong> <em>OptionName</em><strong>,</strong> <em>FeatureName</em> <strong>.</strong> <em>OptionName</em><strong>,</strong> ...<strong>)</strong></p></td>
</tr>
</tbody>
</table>

 

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature. This list can include features as well as options, in which case the period and *OptionName* are not included.

The features and options listed in a single \*InvalidInstallableCombination entry indicate a set of features and options that cannot be used in combination. For example, the following entry specifies that the envelope feeder and the duplexing unit cannot be simultaneously installed.

```cpp
*InvalidInstallableCombination: LIST(InputBin.ENVFEED, Duplex)
```

All \*InvalidInstallationCombination entries must be located at the GPD file's root level (that is, not within braces). The number of features and options included in an entry is not limited.

If a feature or option is included in an \*InvalidInstallationCombination entry, the feature or option's \*Installable? attribute must be set to **TRUE**.

 

 




