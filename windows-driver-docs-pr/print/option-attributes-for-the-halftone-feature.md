---
title: Option Attributes for the Halftone Feature
author: windows-driver-content
description: Option Attributes for the Halftone Feature
ms.assetid: a188908a-ddf7-4b4d-a46d-e3550ffb0418
keywords:
- Halftone Feature
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Option Attributes for the Halftone Feature





The following table lists the attributes associated with the Halftone feature. For more information about the Halftone feature, see [Standard Features](standard-features.md).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>Attribute Parameter</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>*<strong>HTCallbackID</strong></p></td>
<td><p>Positive numeric value passed to the rendering plug-in's [<strong>IPrintOemUni::HalftonePattern</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554258) method as its <em>dwCallbackID</em> parameter.</p></td>
<td><p>Required if an <strong>IPrintOemUni::HalftonePattern</strong> method is provided. See [Halftoning with Unidrv](halftoning-with-unidrv.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>HTNumPatterns</strong></p></td>
<td><p>Numeric value representing the number of halftone patterns provided.</p>
<p>See [Halftoning with Unidrv](halftoning-with-unidrv.md).</p></td>
<td><p>Optional. Can be 1 or 3, where 3 implies separate patterns for red, green, and blue, in that order. If not specified, the default value is 1. Can be used with either *<strong>rcHTPatternID</strong> or *<strong>HTCallbackID</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>HTPatternSize</strong></p></td>
<td><p>[Pair](pairs.md) of numeric values representing the width and height, in pixels, of the pattern specified by *<strong>rcHTPatternID</strong>.</p></td>
<td><p>Required if *<strong>rcHTPatternID</strong> is specified. The maximum pattern size is PAIR (256, 256). Width and height, multiplied together, must be divisible by 4 for storage as DWORDs.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>rcHTPatternID</strong></p></td>
<td><p>Resource identifier for an RC_HTPATTERN resource representing halftone pattern data.</p></td>
<td><p>Required if a halftone pattern is provided in a resource DLL. See [Halftoning with Unidrv](halftoning-with-unidrv.md).</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For more information about using these attributes, see [Halftoning with Unidrv](halftoning-with-unidrv.md). These attributes are not used with [minidriver-supplied halftoning](minidriver-supplied-halftoning.md).

 

 




