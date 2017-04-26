---
title: Installation Constraints
author: windows-driver-content
description: Installation Constraints
ms.assetid: 0adf5a6a-e9de-4bb0-bf1c-fe7eef565840
keywords:
- installation constraints WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installation Constraints


## <a href="" id="ddk-installation-constraints-gg"></a>


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

```
*InvalidInstallableCombination: LIST(InputBin.ENVFEED, Duplex)
```

All \*InvalidInstallationCombination entries must be located at the GPD file's root level (that is, not within braces). The number of features and options included in an entry is not limited.

If a feature or option is included in an \*InvalidInstallationCombination entry, the feature or option's \*Installable? attribute must be set to **TRUE**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installation%20Constraints%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


