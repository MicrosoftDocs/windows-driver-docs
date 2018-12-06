---
title: watermarkPath XML Element
description: watermarkPath XML Element
ms.assetid: 3c64738b-4ead-4e78-a1bd-45d098a11dad
keywords: ["watermarkPath XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- watermarkPath XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# watermarkPath XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **watermarkPath** element specifies the source file for a custom watermark bitmap that DPInst displays on the left side of the DPInst welcome page and the DPInst finish page.

### Element Tag

```cpp
<watermarkPath>
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
<td align="left"><p>String that specifies the name of the file that contains a watermark bitmap that DPInst displays on the left side of a welcome page and a finish page. The watermark file must be located in the DPInst root directory, which is the directory that contains the DPInst executable file (<em>DPInst.exe</em>), or in a subdirectory under the DPInst root directory. If the watermark bitmap file is in a subdirectory, specify a fully qualified file name that is relative to the DPInst root directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

A **watermarkPath** element is customized, but not localized, if it is a child element of a **dpinst** element. A **watermarkPath** element is customized and localized if it is a child element of a **language** element.

The following code example demonstrates a **watermarkPath** element that specifies *Data\\Watermark.bmp* as the source of the watermark bitmap that DPInst displays on the left side of the welcome and finish pages. The text that specifies the custom watermark bitmap file is shown in bold font style.

```cpp
<dpinst>
  ...
  <watermarkPath>Data\Watermark.bmp</watermarkPath>
  ...
</dpinst>
```

If a **watermarkPath** element is not specified, DPInst uses a default watermark.

## See also


[**dpinst**](dpinst-xml-element.md)

[**language**](language-xml-element.md)

 

 






