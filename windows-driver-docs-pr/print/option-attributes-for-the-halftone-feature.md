---
title: Option Attributes for the Halftone Feature
description: Option Attributes for the Halftone Feature
ms.assetid: a188908a-ddf7-4b4d-a46d-e3550ffb0418
keywords: ["Halftone Feature"]
---

# Option Attributes for the Halftone Feature


## <a href="" id="ddk-option-attributes-for-the-halftone-feature-gg"></a>


The following table lists the attributes associated with the Halftone feature. For more information about the Halftone feature, see [Standard Features](standard-features.md).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute Name</th>
<th align="left">Attribute Parameter</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>*<strong>HTCallbackID</strong></p></td>
<td align="left"><p>Positive numeric value passed to the rendering plug-in's [<strong>IPrintOemUni::HalftonePattern</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554258) method as its <em>dwCallbackID</em> parameter.</p></td>
<td align="left"><p>Required if an <strong>IPrintOemUni::HalftonePattern</strong> method is provided. See [Halftoning with Unidrv](halftoning-with-unidrv.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>*<strong>HTNumPatterns</strong></p></td>
<td align="left"><p>Numeric value representing the number of halftone patterns provided.</p>
<p>See [Halftoning with Unidrv](halftoning-with-unidrv.md).</p></td>
<td align="left"><p>Optional. Can be 1 or 3, where 3 implies separate patterns for red, green, and blue, in that order. If not specified, the default value is 1. Can be used with either *<strong>rcHTPatternID</strong> or *<strong>HTCallbackID</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>*<strong>HTPatternSize</strong></p></td>
<td align="left"><p>[Pair](pairs.md) of numeric values representing the width and height, in pixels, of the pattern specified by *<strong>rcHTPatternID</strong>.</p></td>
<td align="left"><p>Required if *<strong>rcHTPatternID</strong> is specified. The maximum pattern size is PAIR (256, 256). Width and height, multiplied together, must be divisible by 4 for storage as DWORDs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>*<strong>rcHTPatternID</strong></p></td>
<td align="left"><p>Resource identifier for an RC_HTPATTERN resource representing halftone pattern data.</p></td>
<td align="left"><p>Required if a halftone pattern is provided in a resource DLL. See [Halftoning with Unidrv](halftoning-with-unidrv.md).</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For more information about using these attributes, see [Halftoning with Unidrv](halftoning-with-unidrv.md). These attributes are not used with [minidriver-supplied halftoning](minidriver-supplied-halftoning.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Option%20Attributes%20for%20the%20Halftone%20Feature%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




