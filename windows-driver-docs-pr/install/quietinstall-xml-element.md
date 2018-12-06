---
title: quietInstall XML Element
description: quietInstall XML Element
ms.assetid: 1151a68f-17c8-4852-9dc0-ab5dea9d58c6
keywords: ["quietInstall XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- quietInstall XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# quietInstall XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **quietInstall** XML element is an empty element that sets the **quietInstall** flag to ON, which configures DPInst to suppress the display of wizard pages and most other user messages.

### **Element Tag**

```cpp
<quietInstall>
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
<td align="left"><p><a href="dpinst-xml-element.md" data-raw-source="[&lt;strong&gt;dpinst&lt;/strong&gt;](dpinst-xml-element.md)"><strong>dpinst</strong></a></p></td>
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

By default, the **quietInstall** flag is set to OFF. You can set the **quietInstall** flag to ON by including a **quietInstall** element in a DPInst descriptor file or by using the **/q** command-line switch. The **quietInstall** flag works with the presence of a EULA page and the **suppressEulaPage** flag.

The following code example demonstrates a **quietInstall** element

```cpp
<dpinst>
  ...
  <quietInstall/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

 

 






