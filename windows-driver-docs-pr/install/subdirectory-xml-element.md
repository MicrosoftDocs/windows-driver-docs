---
title: subDirectory XML Element
description: subDirectory XML Element
ms.assetid: 41f86668-148e-4d7c-89b8-e3c21efffd7b
keywords: ["subDirectory XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- subDirectory XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# subDirectory XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **subDirectory** XML element specifies one or all the subdirectories under the DPInst working directory.

### Element Tag

```cpp
<subDirectory>
```

### XML Attributes

None

### Element Information

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parent elements</strong></p></td>
<td align="left"><p><a href="search-xml-element.md" data-raw-source="[&lt;strong&gt;search&lt;/strong&gt;](search-xml-element.md)"><strong>search</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>Specifies one or all of the subdirectories that are relative to the DPInst working directory. This element can contain:</p>
<ul>
<li><p>A string to specify a specific subdirectory</p></li>
<li><p>The wildcard character (<strong>*</strong>) to specify all of the subdirectories</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **search** element that contains one **subDirectory** element that specifies an *i386* subdirectory under the DPInst working directory. The text that specifies the custom subdirectory is shown in bold font style.

```cpp
<dpinst>
  ...
  <search>
    <subDirectory>i386</subDirectory>
  </search>
  ...
</dpinst>
```

The following code example demonstrates a **search** element that contains a **subDirectory** element that specifies all of the subdirectories under the DPInst working directory. The wildcard character (\*) that specifies all of the subdirectories is shown in bold font style.

```cpp
<search>
  <subDirectory>*</subDirectory>
</search>
```

## See also


[**search**](search-xml-element.md)

 

 






