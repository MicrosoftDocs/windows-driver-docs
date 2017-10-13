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
---

# suppressAddRemovePrograms XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **suppressAddRemovePrograms** XML element is an empty element that sets the **suppressAddRemovePrograms** flag to ON, which configures DPInst to suppress the addition of entries to **Programs and Features** in Control Panel. These entries represent the [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840) and driver package groups that DPInst installs.

**Note**  In versions of Windows earlier than Windows Vista, DPInst added the entry for the driver package to **Add or Remove Programs** in Control Panel.

 

### Element Tag

```
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
<td align="left"><p>[<strong>dpinst</strong>](dpinst-xml-element.md) or [<strong>group</strong>](group-xml-element.md)</p></td>
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

```
<dpinst>
  ...
   <suppressAddRemovePrograms/>
  ...
</dpinst>
```

The following code example demonstrates a **suppressAddRemovePrograms** element that is child element of a **group** element.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20suppressAddRemovePrograms%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





