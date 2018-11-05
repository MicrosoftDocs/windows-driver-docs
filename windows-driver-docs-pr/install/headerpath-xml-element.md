---
title: headerPath XML Element
description: headerPath XML Element
ms.assetid: 9764fed5-75bc-4679-bae0-5bfe738268e2
keywords: ["headerPath XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- headerPath XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# headerPath XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **headerPath** XML element specifies the source file name for a custom header bitmap that DPInst displays in the upper-right corner of the DPInst EULA page and DPInst installation page.

### Element Tag

```cpp
<headerPath>
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
<td align="left"><p><a href="dpinst-xml-element.md" data-raw-source="[&lt;strong&gt;dpinst&lt;/strong&gt;](dpinst-xml-element.md)"><strong>dpinst</strong></a> or <a href="language-xml-element.md" data-raw-source="[&lt;strong&gt;language&lt;/strong&gt;](language-xml-element.md)"><strong>language</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>String that specifies the file name of the header bitmap that DPInst displays in the upper-right corner of the DPInst EULA and installation pages. The header bitmap file must be located in the DPInst root directory, which is the directory that contains the DPInst executable file (<em>DPInst.exe</em>), or in a subdirectory under the DPInst root directory. If the header bitmap file is in a subdirectory, specify a fully qualified file name that is relative to the DPInst root directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

A **headerPath** element is customized, but not localized, if it is a child element of a **dpinst** XML element. A **headerPath** element is customized and localized if it is a child element of a **language** XML element.

The following code example demonstrates a **headerPath** element that specifies *Data\\Header.bmp* as the header bitmap file that DPInst displays in the upper-right corner of a DPInst EULA and installation pages and an installation page. The text that specifies the custom header bitmap file is shown in bold font style.

```cpp
<dpinst>
  ...
  <headerPath>Data\Header.bmp</headerPath>
  ...
</dpinst>
```

If a **headerPath** element is not specified, DPInst uses a default header bitmap.

## See also


[**dpinst**](dpinst-xml-element.md)

[**language**](language-xml-element.md)

 

 






