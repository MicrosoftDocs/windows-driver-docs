---
title: Attributes for Simulated Fonts
description: Attributes for Simulated Fonts
ms.assetid: 000f3c30-2e8a-41b7-ac06-6f2da550ac70
keywords:
- simulated font attributes WDK Unidrv
- font attributes WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attributes for Simulated Fonts





The following table lists attributes describing the printer's support for simulated fonts.

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
<td><p><strong>*DiffFontsPerByteMode?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. For printers supporting both single-byte and double-byte modes, this indicates whether the printer maintains separate fonts and font characteristics for each mode.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




