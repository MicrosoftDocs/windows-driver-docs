---
title: eulaHeaderTitle XML Element
description: eulaHeaderTitle XML Element
ms.assetid: 65b8e793-ed7b-4d2c-8a55-9860e6188b77
keywords: ["eulaHeaderTitle XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- eulaHeaderTitle XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# eulaHeaderTitle XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **eulaHeaderTitle** XML element customizes the text of the EULA header title that appears directly below the title bar on a DPInst EULA page.

### Element Tag

```cpp
<eulaHeaderTitle>
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
<td align="left"><p>String that customizes the title on a DPInst EULA page</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **eulaHeaderTitle** element that customizes the header title of a DPInst EULA page. The text that specifies the custom header title is shown in bold font style.

```cpp
<dpinst>
  ...
  <language code="0x0409">
    . . .
    <eulaHeaderTitle>End User License Agreement</eulaHeaderTitle>
    . . .
  </language>
  ...
</dpinst>
```

If a **eulaHeaderTitle** element is not specified, DPInst displays the default EULA header title that is shown on the default DPInst EULA page.

## See also


[**language**](language-xml-element.md)

 

 






