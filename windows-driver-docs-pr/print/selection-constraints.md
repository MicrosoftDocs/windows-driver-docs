---
title: Selection Constraints
description: Selection Constraints
ms.assetid: 9537e4c7-2cee-494d-b1ec-95d8c91a90e6
keywords:
- selection constraints WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selection Constraints





Often, certain options for various printer features cannot be selected simultaneously. For example, if the envelope feeder is selected, then nonenvelope paper sizes, such as letter-sized or A4-sized paper, cannot be selected.

To specify combinations of printer options that cannot be simultaneously selected, use \*InvalidCombination or \*Constraints entries. If a user attempts to select a combination of options that you have specified as being invalid, Unidrv rejects the selection.

The \*InvalidCombination entry has the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*InvalidCombination : LIST ( <em>FeatureName</em> . <em>OptionName</em> , <em>FeatureName</em> . <em>OptionName</em> , ...)</p></td>
</tr>
</tbody>
</table>

 

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature.

The options listed in a single \*InvalidCombination entry indicate a set of options that cannot be used in combination. For example, the following entry specifies that [*CMYK*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cmyk) color mode cannot be used with plain paper and 720 DPI.

```cpp
*InvalidCombination: LIST(Resolution.720dpi, MediaType.Plain, ColorMode.CMYK)
```

All \*InvalidCombination entries must be located at the GPD file's root level (that is, not within braces). The number of options included in an entry is not limited.

If you only need to indicate an invalid combination relationship between two options, you can use a \*Constraints entry. Its format is:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*Constraints : <em>FeatureName</em> . <em>OptionName</em></p></td>
</tr>
</tbody>
</table>

 

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature. A \*Constraints entry must be placed inside an \*Option entry. For example, to indicate that letter-sized and A4-sized paper cannot be used with the envelope feeder, you can use the following entries:

```cpp
*Feature: InputBin
{
    *Option: ENVFEED
    {
        *Constraints: PaperSize.Letter
        *Constraints: PaperSize.A4
    }
}
```

or, equivalently:

```cpp
*Feature: InputBin
{
    *Option: ENVFEED
    {
        *Constraints: LIST(PaperSize.Letter, PaperSize.A4)
    }
}
```

These examples specify that if a user attempts to select the envelope feeder and letter-sized paper, or the envelope feeder and A4-sized paper, Unidrv rejects the selection.

 

 




