---
title: group XML Element
description: group XML Element
ms.assetid: 8035fd60-065c-4282-a18c-34e6a5201e56
keywords: ["group XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- group XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# group XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **group** XML element specifies an ordered collection of [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840) that DPInst handles as a driver package group.

### Element Tag

```cpp
<group>
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
<td align="left"><p><a href="package-xml-element.md" data-raw-source="[&lt;strong&gt;package&lt;/strong&gt;](package-xml-element.md)"><strong>package</strong></a> (zero or more)</p>
<p><a href="installallornone-xml-element.md" data-raw-source="[&lt;strong&gt;installAllOrNone&lt;/strong&gt;](installallornone-xml-element.md)"><strong>installAllOrNone</strong></a> (zero or one)</p>
<p><a href="suppressaddremoveprograms-xml-element.md" data-raw-source="[&lt;strong&gt;suppressAddRemovePrograms&lt;/strong&gt;](suppressaddremoveprograms-xml-element.md)"><strong>suppressAddRemovePrograms</strong></a> (zero or one)</p></td>
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

The following code example demonstrates a **group** element that includes two [**package XML elements**](package-xml-element.md) and an [**installAllOrNone XML element**](installallornone-xml-element.md). The example **group** element configures DPInst to handle the "Abc" [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) and the "Def" driver package as a group. The **installAllOrNone** XML element configures DPInst to install the driver packages in the driver package group only if both drivers can be installed.

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

[**installAllOrNone**](installallornone-xml-element.md)

[**package**](package-xml-element.md)

[**suppressAddRemovePrograms**](suppressaddremoveprograms-xml-element.md)

 

 






