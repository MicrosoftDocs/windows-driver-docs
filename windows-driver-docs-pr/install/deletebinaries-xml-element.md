---
title: deleteBinaries XML Element
description: The deleteBinaries XML element is an empty element that sets the deleteBinaries flag to ON, which configures DPInst to delete binary files from a system that were copied to the system when a driver package was installed.Element Tag deleteBinaries XML AttributesNoneElement Information Parent elementsdpinstChild elementsNoneData contentsNone permittedDuplicate child elementsNone permitted RemarksBy default, the deleteBinaries flag is set to OFF. To set the deleteBinaries flag to ON, include a deleteBinaries element as a child element of a dpinst element or use the /d DPInst command-line switch. The following code example demonstrates a deleteBinaries element. dpinst ... deleteBinaries/ ... /dpinst Note � Starting with Windows 7, the operating system ignores a setting of ON for the deleteBinaries XML element. The binary files, which were copied to a system when a driver package was installed, can no longer be deleted by using DPInst.�
ms.assetid: 2711b2c2-b1ec-41cb-aeb2-1d9078740075
keywords: ["deleteBinaries XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- deleteBinaries XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# deleteBinaries XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **deleteBinaries** XML element is an empty element that sets the **deleteBinaries** flag to ON, which configures DPInst to delete binary files from a system that were copied to the system when a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) was installed.

**Element Tag**

```cpp
<deleteBinaries>
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
<td align="left"><p>None</p></td>
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

By default, the **deleteBinaries** flag is set to OFF. To set the **deleteBinaries** flag to ON, include a **deleteBinaries** element as a child element of a **dpinst** element or use the **/d** DPInst command-line switch.

The following code example demonstrates a **deleteBinaries** element.

```cpp
<dpinst>
  ...
   <deleteBinaries/>
  ...
</dpinst>
```

**Note**   Starting with Windows 7, the operating system ignores a setting of ON for the **deleteBinaries** XML element. The binary files, which were copied to a system when a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) was installed, can no longer be deleted by using DPInst.

 

## See also


[**dpinst**](dpinst-xml-element.md)

 

 






