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
---

# deleteBinaries XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **deleteBinaries** XML element is an empty element that sets the **deleteBinaries** flag to ON, which configures DPInst to delete binary files from a system that were copied to the system when a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) was installed.

**Element Tag**

```
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
<td align="left"><p>[<strong>dpinst</strong>](dpinst-xml-element.md)</p></td>
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

```
<dpinst>
  ...
   <deleteBinaries/>
  ...
</dpinst>
```

**Note**   Starting with Windows 7, the operating system ignores a setting of ON for the **deleteBinaries** XML element. The binary files, which were copied to a system when a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) was installed, can no longer be deleted by using DPInst.

 

## See also


[**dpinst**](dpinst-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20deleteBinaries%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





