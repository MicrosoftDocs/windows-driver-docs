---
title: Option Attributes for the Memory Feature
description: Option Attributes for the Memory Feature
ms.assetid: 17646f6e-b234-4a17-ba24-4bc7f6f85ace
keywords:
- Memory Feature WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Option Attributes for the Memory Feature





The following table lists the attributes associated with the Memory feature. For more information about the Memory feature, see [Standard Features](standard-features.md).

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
<td><p><em><strong>MemConfigKB</strong></p></td>
<td><p>PAIR of numeric values indicating the total and available printer-resident memory, in kilobytes. For example, PAIR (1024, 450) indicates 1024 kilobytes total, 450 kilobytes available, with a GPD-generated option name of &quot;1024KB&quot;.</p></td>
<td><p>Optional. See <a href="describing-printer-memory-configurations.md" data-raw-source="[Describing Printer Memory Configurations](describing-printer-memory-configurations.md)">Describing Printer Memory Configurations</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MemConfigMB</strong></p></td>
<td><p>PAIR of numeric values indicating the total and available printer-resident memory, in megabytes. For example, PAIR (2, 1) indicates 2 megabytes total, 1 megabyte available, with a GPD-generated option name of &quot;2MB&quot;.</p></td>
<td><p>Optional. See <a href="describing-printer-memory-configurations.md" data-raw-source="[Describing Printer Memory Configurations](describing-printer-memory-configurations.md)">Describing Printer Memory Configurations</a>.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MemoryConfigKB</strong></p></td>
<td><p>PAIR of numeric values indicating the total and available printer-resident memory, in kilobytes. For example, PAIR (1024, 450) indicates 1024 kilobytes total, 450 kilobytes available.</p></td>
<td><p>Optional. See <a href="describing-printer-memory-configurations.md" data-raw-source="[Describing Printer Memory Configurations](describing-printer-memory-configurations.md)">Describing Printer Memory Configurations</a>.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For more information about using these attributes, along with examples, see [Describing Printer Memory Configurations](describing-printer-memory-configurations.md).

For information about additional option attributes, see [Option Attributes for All Features](option-attributes-for-all-features.md).

 

 




