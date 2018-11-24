---
title: welcomeTitle XML Element
description: welcomeTitle XML Element
ms.assetid: 480b6d02-b8b1-4e3f-9a00-869cc2b93279
keywords: ["welcomeTitle XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- welcomeTitle XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# welcomeTitle XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **welcomeTitle** XML element customizes the bold text of the welcome title that appears at the top of the DPInst welcome page.

### Element Tag

```cpp
<welcomeTitle>
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
<td align="left"><p>String that customizes the title text at the top of a welcome page</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **welcomeTitle** element customizes the title text on a welcome page. The text that specifies the custom welcome title is shown in bold font style.

```cpp
<dpinst>
  ...
  <language code="0x0409">
    ...
    <welcomeTitle>Welcome to the toaster Installer!</welcomeTitle>
    ...
  </language>
  ...
</dpinst>
```

If a **welcomeTitle** element is not specified, DPInst displays the default welcome title that is shown on the default welcome page.

## See also


[**language**](language-xml-element.md)

 

 






