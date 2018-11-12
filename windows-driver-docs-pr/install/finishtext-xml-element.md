---
title: finishText XML Element
description: finishText XML Element
ms.assetid: b8c63f75-e0d3-458f-9265-a19d6f64ac6b
keywords: ["finishText XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- finishText XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# finishText XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **finishText** XML element customizes the main text that DPInst displays on a DPInst finish page.

### Element Tag

```cpp
<finishText>
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
<td align="left"><p>String that customizes the main text on a finish page</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **finishText** element that customizes the main text on a finish page that DPInst displays for a successful installation. The text that specifies the custom finish text is shown in bold font style.

```cpp
dpinst>
  ...
  <language code="0x0409">
    ...
    <finishText>Enjoy using the Toaster.</finishText>
    ...
  </language>
  ...
</dpinst>
```

If a **finishText** element is not specified, DPInst displays default finish text that indicates whether the installation was a success or a failure.

## See also


[**finishTitle**](finishtitle-xml-element.md)

[**language**](language-xml-element.md)

 

 






