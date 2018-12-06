---
title: icon XML Element
description: icon XML Element
ms.assetid: 1d5acaf7-ef90-40f7-a2f9-f1002207f3fb
keywords: ["icon XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- icon XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# icon XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **icon** XML element specifies the source file for a custom icon that DPInst displays on the DPInst EULA page. DPInst uses this icon to represent DPInst on the Microsoft Windows taskbar and desktop. DPInst also uses this icon for the entry that represents a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840), which DPInst adds to **Programs and Features** in Control Panel

**Note**  Prior to Windows Vista, DPInst added the entry for the driver package to **Add or Remove Programs** in Control Panel.

 

### Element Tag

```cpp
<icon>
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
<td align="left"><p>String that specifies the source file that contains the icon that DPInst displays on a DPInst EULA page. The icon file must be located in the DPInst root directory, which is the directory that contains the DPInst executable file (<em>DPInst.exe</em>), or in a subdirectory under the DPInst root directory. If the icon file is in a subdirectory, specify a fully qualified file name that is relative to the DPInst root directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

An **icon** element is customized, but not localized, if it is a child element of a **dpinst** XML element. An **icon** element is customized and localized if it is a child element of a **language** XML element.

The following code example demonstrates an **icon** element that specifies Data\\Small.ico as the source of a custom icon that DPInst displays on the DPInst EULA page. The text that specifies the custom icon file is shown in bold font style.

```cpp
<dpinst>
  ...
  <icon>Data\Eula.ico</icon>
  ...
</dpinst>
```

If an **icon** element is not specified, DPInst displays a default icon. The position of this icon cannot be changed.

## See also


[**dpinst**](dpinst-xml-element.md)

[**language**](language-xml-element.md)

 

 






