---
title: installHeaderTitle XML Element
description: installHeaderTitle XML Element
ms.assetid: 43f8611c-9504-46ab-a8f2-06141bf74f1f
keywords: ["installHeaderTitle XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- installHeaderTitle XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# installHeaderTitle XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **installHeaderTitle** XML element customizes the bold text of the installation header title that appears on a DPInst installation page.

### Element Tag

```cpp
<installHeaderTitle>
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
<td align="left"><p><a href="language-xml-element.md" data-raw-source="[&lt;strong&gt;language&lt;/strong&gt;](language-xml-element.md)"><strong>language</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>String that customizes the title text of an installation page</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates an **installHeaderTitle** element that customizes the title text of an installation page. The text that specifies the custom install header title is shown in bold font style.

```cpp
<dpinst>
  ...
  <language code="0x0409">
    ...
    <installHeaderTitle>Installing the software for your Toaster device...</installHeaderTitle>
    ...
  </language>
  ...
</dpinst>
```

If an **installHeaderTitle** element is not specified, DPInst displays the default title text that is shown on the default installation page.

## See also


[**language**](language-xml-element.md)

 

 






