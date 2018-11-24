---
title: package XML Element
description: The package XML element specifies an INF file for a driver package.Element Tag package XML AttributespathThe path to an INF file for a driver package.
ms.assetid: c7089e58-50c7-46ec-a9bf-c8e2d2bd354a
keywords: ["package XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- package XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# package XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **package** XML element specifies an INF file for a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).

**Element Tag**

```cpp
<package>
```

**XML Attributes**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>path</strong></p></td>
<td align="left"><p>The path to an INF file for a driver package. The path is relative to the DPInst working directory.</p></td>
</tr>
</tbody>
</table>

 

**Element Information**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parent elements</strong></p></td>
<td align="left"><p><a href="group-xml-element.md" data-raw-source="[&lt;strong&gt;group&lt;/strong&gt;](group-xml-element.md)"><strong>group</strong></a></p></td>
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

The following code example demonstrates a **package** element that specifies DirAbc\\Abc.inf as the INF file for the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).

```cpp
<dpinst>
  ...
  <group>
    <package path="DirAbc\Abc.inf" />
  </group>
  ...
</dpinst>
```

## See also


[**group**](group-xml-element.md)

 

 






