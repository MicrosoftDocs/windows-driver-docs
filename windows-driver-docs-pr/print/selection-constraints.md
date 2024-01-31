---
title: Selection Constraints
description: Selection Constraints
keywords:
- selection constraints WDK Unidrv
ms.date: 01/30/2024
---

# Selection constraints

[!include[Print Support Apps](../includes/print-support-apps.md)]

Often, certain options for various printer features can't be selected simultaneously. For example, if the envelope feeder is selected, then nonenvelope paper sizes, such as letter-sized or A4-sized paper, can't be selected.

To specify combinations of printer options that can't be simultaneously selected, use \*InvalidCombination or \*Constraints entries. If a user attempts to select a combination of options that you specified as being invalid, Unidrv rejects the selection.

The \*InvalidCombination entry has the following format:

\*InvalidCombination : LIST ( *FeatureName* . *OptionName* , *FeatureName* . *OptionName* , ...)

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature.

The options listed in a single \*InvalidCombination entry indicate a set of options that can't be used in combination. For example, the following entry specifies that *CMYK* color mode can't be used with plain paper and 720 DPI.

```GPD
*InvalidCombination: LIST(Resolution.720dpi, MediaType.Plain, ColorMode.CMYK)
```

All \*InvalidCombination entries must be located at the GPD file's root level (that is, not within braces). The number of options included in an entry isn't limited.

If you only need to indicate an invalid combination relationship between two options, you can use a \*Constraints entry. Its format is:

\*Constraints : *FeatureName* . *OptionName*

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature. A \*Constraints entry must be placed inside an \*Option entry. For example, to indicate that letter-sized and A4-sized paper can't be used with the envelope feeder, you can use the following entries:

```GPD
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

```GPD
*Feature: InputBin
{
    *Option: ENVFEED
    {
        *Constraints: LIST(PaperSize.Letter, PaperSize.A4)
    }
}
```

These examples specify that if a user attempts to select the envelope feeder and letter-sized paper, or the envelope feeder and A4-sized paper, Unidrv rejects the selection.
