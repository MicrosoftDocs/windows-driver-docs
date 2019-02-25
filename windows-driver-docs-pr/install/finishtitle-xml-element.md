---
title: finishTitle XML Element
description: finishTitle XML Element
ms.assetid: d8730b49-9cc0-46f4-88a1-fd5543063277
keywords: ["finishTitle XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- finishTitle XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# finishTitle XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **finishTitle** XML element customizes the text of the finish title that appears at the top of a DPInst finish page.

### **Element Tag**

```cpp
<finishTitle>
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
<td align="left"><p>String that customizes the title text at the top of a finish page.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **finishTitle** element that customizes the title text at the top of a finish page. The text that specifies the custom title text is shown in bold font style.

```cpp
dpinst>
  ...
  <language code="0x0409">
    ...
    <finishTitle>Congratulations! You are finished installing your Toaster device.</finishTitle>
    ...
  </language>
  ...
</dpinst>
```

If a **finishTitle** element is not specified, DPInst displays the default title text that is shown on the default finish page.

## See also


[**finishText**](finishtext-xml-element.md)

[**language**](language-xml-element.md)

 

 






