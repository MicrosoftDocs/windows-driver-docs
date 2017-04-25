---
title: Selection Constraints
author: windows-driver-content
description: Selection Constraints
ms.assetid: 9537e4c7-2cee-494d-b1ec-95d8c91a90e6
keywords:
- selection constraints WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Selection Constraints


## <a href="" id="ddk-selection-constraints-gg"></a>


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

```
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

```
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

```
*Feature: InputBin
{
    *Option: ENVFEED
    {
        *Constraints: LIST(PaperSize.Letter, PaperSize.A4)
    }
}
```

These examples specify that if a user attempts to select the envelope feeder and letter-sized paper, or the envelope feeder and A4-sized paper, Unidrv rejects the selection.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Selection%20Constraints%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


