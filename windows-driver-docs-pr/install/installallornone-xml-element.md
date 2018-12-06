---
title: installAllOrNone XML Element
description: installAllOrNone XML Element
ms.assetid: f5634def-c9a1-45db-88ce-f652171d19c9
keywords: ["installAllOrNone XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- installAllOrNone XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# installAllOrNone XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **installAllOrNone** XML element is an empty element that sets the **installAllOrNone** flag to ON, which configures DPInst to install drivers in a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) only if all of the driver packages in the installation package can be installed or if all of driver packages in the driver package group can be installed.

### **Element Tag**

```cpp
<installAllOrNone>
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

By default, the **installAllOrNone** flag is set to OFF. To set the **installAllOrNone** flag to ON for all of the [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840), including those in driver package groups, include an **installAllOrNone** element as a child element of a **dpinst** XML element, or use the **/a** command-line switch. To set the **installAllOrNone** flag to ON only for a specific driver package group, include an **installAllOrNone** element as child element of the corresponding **group** XML element.

The following code example demonstrates an **installAllOrNone** element that is a child element of a **dpinst** element.

```cpp
<dpinst>
  ...
  <installAllOrNone/>
  ...
</dpinst>
```

The following code example demonstrates an **installAllOrNone** element that is a child element of a **group** element.

```cpp
<dpinst>
  ...
  <group>
    <package path="DirAbc\Abc.inf" /> 
    <package path="DirDef\Def.inf" /> 
    <installAllOrNone/>
  <group/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

[**group**](group-xml-element.md)

 

 






