---
title: Option Attributes for the Memory Feature
author: windows-driver-content
description: Option Attributes for the Memory Feature
ms.assetid: 17646f6e-b234-4a17-ba24-4bc7f6f85ace
keywords:
- Memory Feature WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Option Attributes for the Memory Feature


## <a href="" id="ddk-option-attributes-for-the-memory-feature-gg"></a>


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
<td><p>*<strong>MemConfigKB</strong></p></td>
<td><p>PAIR of numeric values indicating the total and available printer-resident memory, in kilobytes. For example, PAIR (1024, 450) indicates 1024 kilobytes total, 450 kilobytes available, with a GPD-generated option name of &quot;1024KB&quot;.</p></td>
<td><p>Optional. See [Describing Printer Memory Configurations](describing-printer-memory-configurations.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MemConfigMB</strong></p></td>
<td><p>PAIR of numeric values indicating the total and available printer-resident memory, in megabytes. For example, PAIR (2, 1) indicates 2 megabytes total, 1 megabyte available, with a GPD-generated option name of &quot;2MB&quot;.</p></td>
<td><p>Optional. See [Describing Printer Memory Configurations](describing-printer-memory-configurations.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MemoryConfigKB</strong></p></td>
<td><p>PAIR of numeric values indicating the total and available printer-resident memory, in kilobytes. For example, PAIR (1024, 450) indicates 1024 kilobytes total, 450 kilobytes available.</p></td>
<td><p>Optional. See [Describing Printer Memory Configurations](describing-printer-memory-configurations.md).</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For more information about using these attributes, along with examples, see [Describing Printer Memory Configurations](describing-printer-memory-configurations.md).

For information about additional option attributes, see [Option Attributes for All Features](option-attributes-for-all-features.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Option%20Attributes%20for%20the%20Memory%20Feature%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


