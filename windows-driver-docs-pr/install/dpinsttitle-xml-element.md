---
title: dpinstTitle XML Element
description: dpinstTitle XML Element
ms.assetid: a6867874-436b-414f-9610-aea585822a91
keywords: ["dpinstTitle XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- dpinstTitle XML Element
api_type:
- NA
ms.localizationpriority: medium
---

# dpinstTitle XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **dpinstTitle** XML element customizes the text that appears on the title bar of all of the DPInst wizard pages.

### Element Tag

```
<dpinstTitle>
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
<td align="left"><p>[<strong>language</strong>](language-xml-element.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>String that customizes the title bar text on all of the wizard pages</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example of a **dpinstTitle** element customizes the title bar text. The text that specifies the custom DPInst title is shown in bold font style.

```
<dpinst>
  ...
  <language code="0x0409">
    ...
    <dpinstTitle>Toaster Device Installer</dpinstTitle>
    ...
  </language>
  ...
</dpinst>
```

If a **dpinstTitle** element is not specified, DPInst displays the default title bar text that appears on the default welcome page.

## See also


[**language**](language-xml-element.md)

 

 






