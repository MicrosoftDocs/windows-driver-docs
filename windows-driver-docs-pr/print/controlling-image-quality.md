---
title: Controlling Image Quality
description: Controlling Image Quality
keywords:
- Unidrv, image quality
- image quality options WDK Unidrv
- draft image quality WDK Unidrv
- better image quality WDK Unidrv
- best image quality WDK Unidrv
- quality setting entries WDK Unidrv
- print jobs WDK , image quality
- formats WDK image quality
- Unidrv WDK print
ms.date: 01/27/2023
---

# Controlling Image Quality

[!include[Print Support Apps](../includes/print-support-apps.md)]

Unidrv's user interface provides a set of three radio buttons that allow a user to select "draft", "better", or "best" image quality for a print job. Draft quality emphasizes printer speed over image resolution, while best quality does the opposite.

The purpose of these radio buttons is to allow the user to easily select the feature options required to obtain the desired quality, without the necessity of explicitly selecting the required options individually.

The options that Unidrv should select when a radio button is pressed are specified in the printer's GPD file. The GPD language defines the following three entries:

- *DraftQualitySettings

- *BetterQualitySettings

- *BestQualitySettings

Each of these entries is associated with one of the radio buttons, and each entry accepts a list of options. When a user selects the corresponding button, Unidrv goes through the list and sets the specified options.

The format for each of the quality setting entries is as follows:

\**XXXX*QualitySettings: LIST(*FeatureName*.*OptionName*, *FeatureName*.*OptionName*, *FeatureName*.*OptionName*, ...)

where each *FeatureName* is a name associated with a \**Feature* entry, and *OptionName* is a name associated with one of the feature's \**Option* entries. An empty list causes the associated radio button to be grayed out.

An additional, required entry specifies the default image quality. The format is as follows:

**DefaultQuality:** *DefaultQuality*

where *DefaultQuality* is one of `DRAFTQUALITY`, `BETTERQUALITY`, or `BESTQUALITY`.

These GPD file entries can be associated with any option of the `ColorMode` and `MediaType` features. Typically, they're placed in [conditional statements](conditional-statements.md), as illustrated in the following example.

```cpp
*switch: ColorMode {
    *case: Mono {
        *BestQualitySettings: LIST(ColorMode.Mono,
                                   Resolution.Option1,
                                   TextQuality.Option3)
        *BetterQualitySettings: LIST(ColorMode.Mono,
                                     Resolution.Option1,
                                     TextQuality.Option1)
        *DraftQualitySettings: LIST(ColorMode.Mono,
                                    Resolution.Option2,
                                    TextQuality.Option2)
        *DefaultQuality: BETTERQUALITY }
    *default: {
        *BestQualitySettings: LIST(ColorMode.24bpp,
                                   Resolution.Option2,
                                   TextQuality.Option3)
        *BetterQualitySettings: LIST(ColorMode.Color,
                                     Resolution.Option2,
                                     TextQuality.Option1)
        *DraftQualitySettings: LIST(ColorMode.Color,
                                    Resolution.Option2,
                                    TextQuality.Option2)
        *DefaultQuality: BETTERQUALITY }}
```

As illustrated in the example, a good strategy is to specify one \***Case** entry for single color mode, then use a \***Default** entry for all multicolor modes. This is because Unidrv's **Page Setup** property sheet page offers the user two choices -- color or noncolor printing. If you use the format in the example, Unidrv displays the quality buttons when the user selects the color printing option.

Following is a more complex example, which ties image quality to both color mode and media type:

```cpp
*switch: Colormode {
    *case: Mono {
    *switch: MediaType {
        *case: CLAYCOATED {
            *DraftQualitySettings:  LIST(Option List)
            *BetterQualitySettings:  LIST(Option List)
            *BestQualitySettings:  LIST(Option List)
            *DefaultQuality:  BESTQUALITY }
        *case: GLOSSY {
            *DraftQualitySettings:  LIST(Option List)
            *BetterQualitySettings:  LIST(Option List)
            *BestQualitySettings:  LIST(Option List)
            *DefaultQuality:  BETTERQUALITY 
        *default: 
            *DraftQualitySettings:  LIST(Option List)
            *BetterQualitySettings:  LIST(Option List)
            *BestQualitySettings:  LIST(Option List)
            *DefaultQuality:  DRAFTQUALITY }}}
    *default: {
    *switch: MediaType {
        *case: CLAYCOATED {
            *DraftQualitySettings:  LIST(Option List)
            *BetterQualitySettings:  LIST(Option List)
            *BestQualitySettings:  LIST(Option List)
            *DefaultQuality:  BESTQUALITY }
        *case: GLOSSY {
            *DraftQualitySettings:  LIST(Option List)
            *BetterQualitySettings:  LIST(Option List)
            *BestQualitySettings:  LIST(Option List)
            *DefaultQuality:  BETTERQUALITY }
        *default: {
            *DraftQualitySettings:  LIST(Option List)
            *BetterQualitySettings:  LIST(Option List)
            *BestQualitySettings:  LIST(Option List)
            *DefaultQuality:  DRAFTQUALITY }}}
}
```

When using the quality setting GPD entries, the following rules must be observed:

- You must always use all four entries. Specifying an empty option list is allowed, and causes the associated radio button to be grayed out.

- All four entries must be specified for all ColorMode and MediaType combinations. The examples use a \***Default** entry within each conditional statement to achieve this.

- Option lists within the quality setting entries must not violate any [option constraints](option-constraints.md) you've specified.

- Options included in an option list shouldn't change the selected medium type. Also, while it's acceptable, for example, to set the color mode to 24 bits/pixel for best quality, 8 bits/pixel for better quality, and 4 bits/pixel for draft quality, changing to 1 bits/pixel (single color) wouldn't be acceptable.

If a feature is included in a conditional statement that specifies quality settings, the parser sets the feature's \*UpdateQualityMacro? attribute to **TRUE**. For more information, see [Feature Attributes](feature-attributes.md).
