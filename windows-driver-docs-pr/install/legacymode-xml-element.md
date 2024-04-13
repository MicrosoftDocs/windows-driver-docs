---
title: legacyMode XML Element
description: The legacyMode XML element is an empty element that sets the legacyMode flag to ON, which configures DPInst to install unsigned drivers and driver packages that have missing files.
keywords: ["legacyMode XML Element Device and Driver Installation"]
topic_type:
- apiref
ms.topic: reference
api_name:
- legacyMode XML Element
api_type:
- NA
ms.date: 10/17/2018
---

# legacyMode XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](./difx-guidelines.md).\]

The **legacyMode** XML element is an empty element that sets the **legacyMode** flag to ON, which configures DPInst to install unsigned drivers and [driver packages](./driver-packages.md) that have missing files.

**Element Tag**

```cpp
<legacyMode>
```

**XML Attributes**

None

**Element Information**

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

 

**Remarks**

By default, DPInst installs only signed [driver packages](./driver-packages.md) and driver packages that do not have missing files. To configure DPInst to accept unsigned driver packages or driver packages that have missing files, set the **legacyMode** flag to ON by including an **legacyMode** element as a child element of a **dpinst** XML element or by using the **/lm** command-line switch.

The following code example demonstrates a **legacyMode** element.

```cpp
<dpinst>
  ...
  <legacyMode/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

 

