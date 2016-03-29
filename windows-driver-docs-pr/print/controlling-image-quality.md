---
title: Controlling Image Quality
description: Controlling Image Quality
ms.assetid: b6d25178-6726-4ce0-ab34-efeedc618044
keywords: ["Unidrv, image quality", "image quality options WDK Unidrv", "draft image quality WDK Unidrv", "better image quality WDK Unidrv", "best image quality WDK Unidrv", "quality setting entries WDK Unidrv", "print jobs WDK , image quality", "formats WDK image quality", "Unidrv WDK print"]
---

# Controlling Image Quality


## <a href="" id="ddk-controlling-image-quality-gg"></a>


Unidrv's user interface provides a set of three radio buttons that allow a user to select "draft", "better", or "best" image quality for a print job. Draft quality emphasizes printer speed over image resolution, while best quality does the opposite.

The purpose of these radio buttons is to allow the user to easily select the feature options required to obtain the desired quality, without the necessity of explicitly selecting the required options individually.

The options that Unidrv should select when a radio button is pressed are specified in the printer's GPD file. The GPD language defines the following three entries:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>*<strong>DraftQualitySettings</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>*<strong>BetterQualitySettings</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>*<strong>BestQualitySettings</strong></p></td>
</tr>
</tbody>
</table>

 

Each of these entries is associated with one of the radio buttons, and each entry accepts a list of options. When a user selects the corresponding button, Unidrv goes through the list and sets the specified options.

The format for each of the quality setting entries is as follows:

\**XXXX*QualitySettings: LIST(*FeatureName*.*OptionName*, *FeatureName*.*OptionName*, *FeatureName*.*OptionName*, ...)

where each *FeatureName* is a name associated with a \**Feature* entry, and *OptionName* is a name associated with one of the feature's \**Option* entries. An empty list causes the associated radio button to be grayed out.

An additional, required entry specifies the default image quality. The format is as follows:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>*<strong>DefaultQuality:</strong> <em>DefaultQuality</em></p></td>
</tr>
</tbody>
</table>

 

where *DefaultQuality* is one of `DRAFTQUALITY`, `BETTERQUALITY`, or `BESTQUALITY`.

These GPD file entries can be associated with any option of the `ColorMode` and `MediaType` features. Typically, they are placed in [conditional statements](conditional-statements.md), as illustrated in the following example.

```
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

```
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

-   You must always use all four entries. Specifying an empty option list is allowed, and causes the associated radio button to be grayed out.

-   All four entries must be specified for all ColorMode and MediaType combinations. The examples use a \***Default** entry within each conditional statement to achieve this.

-   Option lists within the quality setting entries must not violate any [option constraints](option-constraints.md) you have specified.

-   Options included in an option list should not change the selected medium type. Also, while it is acceptable, for example, to set the color mode to 24 bits/pixel for best quality, 8 bits/pixel for better quality, and 4 bits/pixel for draft quality, changing to 1 bits/pixel (single color) would not be acceptable.

If a feature is included in a conditional statement that specifies quality settings, the parser sets the feature's \*UpdateQualityMacro? attribute to **TRUE**. (See [Feature Attributes](feature-attributes.md).)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Controlling%20Image%20Quality%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




