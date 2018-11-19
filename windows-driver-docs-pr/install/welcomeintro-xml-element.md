---
title: welcomeIntro XML Element
description: welcomeIntro XML Element
ms.assetid: d0325d14-c31a-453d-b28e-4bdb646d0711
keywords: ["welcomeIntro XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- welcomeIntro XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# welcomeIntro XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **welcomeIntro** XML element customizes the main text on the DPInst welcome page.

### Element Tag

```cpp
<welcomeIntro>
```

### XML Attributes

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
<td align="left"><p>String that customizes the main text on a welcome page</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **welcomeIntro** element that customizes the main text on a welcome page. The text that specifies the custom welcome introduction is shown in bold font style.

```cpp
<dpinst>
  ...
  <language code="0x0409">
    . . .
    <welcomeIntro>This wizard will walk you through updating the drivers for your Toaster device.</welcomeIntro>
    ...
  </language>
  ...
</dpinst>
```

If a **welcomeIntro** element is not specified, DPInst displays the default main text that is shown on the default welcome page.

## See also


[**language**](language-xml-element.md)

 

 






