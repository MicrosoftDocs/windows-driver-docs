---
title: suppressAddRemovePrograms XML Element
description: suppressAddRemovePrograms XML Element
ms.assetid: ab3bac90-dffa-400b-916a-a7deecbc42d7
keywords: ["suppressAddRemovePrograms XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- suppressAddRemovePrograms XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# suppressAddRemovePrograms XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **suppressAddRemovePrograms** XML element is an empty element that sets the **suppressAddRemovePrograms** flag to ON, which configures DPInst to suppress the addition of entries to **Programs and Features** in Control Panel. These entries represent the [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840) and driver package groups that DPInst installs.

**Note**  In versions of Windows earlier than Windows Vista, DPInst added the entry for the driver package to **Add or Remove Programs** in Control Panel.

 

### Element Tag

```cpp
<suppressAddRemovePrograms>
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
<td align="left"><p><a href="dpinst-xml-element.md" data-raw-source="[&lt;strong&gt;dpinst&lt;/strong&gt;](dpinst-xml-element.md)"><strong>dpinst</strong></a> or <a href="group-xml-element.md" data-raw-source="[&lt;strong&gt;group&lt;/strong&gt;](group-xml-element.md)"><strong>group</strong></a></p></td>
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

By default, the **suppressAddRemovePrograms** flag is set to OFF. To set the **suppressAddRemovePrograms** flag to ON for all of the drivers that DPInst installs, including all of the drivers in [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) groups, include a **suppressAddRemovePrograms** element as a child element of a **dpinst** XML element in a DPInst descriptor file, or use the **/sa** command-line switch. To set the **suppressAddRemoverPrograms** flag only for a specific driver package group, include a **suppressAddRemovePrograms** element as a child element of the corresponding **group** XML element in a DPInst descriptor file.

The following code example demonstrates a **suppressAddRemovePrograms** element that is child element of a **dpinst** element.

```cpp
<dpinst>
  ...
   <suppressAddRemovePrograms/>
  ...
</dpinst>
```

The following code example demonstrates a **suppressAddRemovePrograms** element that is child element of a **group** element.

```cpp
<dpinst>
  ...
  <group>
    <package path="DirAbc\Abc.inf" /> 
    <package path="DirDef\Def.inf" /> 
    <suppressAddRemovePrograms/>
  <group/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

[**group**](group-xml-element.md)

 

 






