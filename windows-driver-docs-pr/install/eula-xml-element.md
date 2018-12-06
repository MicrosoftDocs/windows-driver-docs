---
title: eula XML Element
description: eula XML Element
ms.assetid: ab647583-b0e1-4f40-86af-9b7923f5535c
keywords: ["eula XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- eula XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# eula XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **eula** XML element is an empty XML element that includes two attributes that specify a EULA text file that contains custom text for a DPInst EULA page.

### Element Tag

```cpp
<eula>
```

### XML Attributes

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Type</strong></p></td>
<td align="left"><p>The type of vendor-supplied EULA. The value of this attribute must be set to the string &quot;txt&quot;, which indicates a plain-text file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Path</strong></p></td>
<td align="left"><p>A string that identifies the name of the file that contains the text for a DPInst EULA page. The EULA text file must be encoded by using UTF-8 encoding. The EULA file must be located in the DPInst root directory, which is the directory that contains the DPInst executable file (<em>DPInst.exe</em>), or a subdirectory under the DPInst root directory. If the EULA file is in a subdirectory, specify a fully qualified file name that is relative to the DPInst root directory.</p></td>
</tr>
</tbody>
</table>

 

### Element Information

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parent elements</strong></p></td>
<td align="left"><p><a href="language-xml-element.md" data-raw-source="[&lt;strong&gt;language&lt;/strong&gt;](language-xml-element.md)"><strong>language</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **eula** element that specifies that *Data\\Eula409.txt* contains custom EULA text. The *Eula409.txt* file is in the *Data* directory, which must be a subdirectory under the DPInst root directory. The text that specifies the custom EULA file is shown below using the &lt;eula&gt; tag.

```cpp
<dpinst>
  ...
  <language code="0x0409">
    ...
    <eula type="txt" path="Data\Eula409.txt"/>
    ...
  </language>
  ...
</dpinst>
```

## See also


[**language**](language-xml-element.md)

 

 






