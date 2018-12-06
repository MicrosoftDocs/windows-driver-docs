---
title: eulaYesButton XML Element
description: eulaYesButton XML Element
ms.assetid: 7d91d3ec-af0a-4b6a-83d8-fa14a527378b
keywords: ["eulaYesButton XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- eulaYesButton XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# eulaYesButton XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **eulaYesButton** XML element customizes the text that is associated with the accept option button on a DPInst EULA page.

### **Element Tag**

```cpp
<eulaYesButton>
```

### **XML Attributes**

None

### **Element Information**

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
<td align="left"><p>String that customizes the text that is associated with the accept option button on a DPInst EULA page</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **eulaYesButton** element that customizes the accept option button text on a DPInst EULA page. The text that specifies the custom text of the accept option button is shown in bold font style.

```cpp
<dpinst>
  ...
  <language code="0x0409">
    ...
    <eulaYesButton>I &amp;accept this EULA</eulaYesButton>
    ...
  </language>
  ...
</dpinst>
```

If a **eulaYesButton** element is not specified, DPInst displays the default option button text that is shown on the default DPInst EULA page.

## See also


[**eula**](eula-xml-element.md)

[**eulaNoButton**](eulanobutton-xml-element.md)

[**language**](language-xml-element.md)

 

 






