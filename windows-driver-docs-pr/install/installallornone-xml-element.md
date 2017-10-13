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
---

# installAllOrNone XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **installAllOrNone** XML element is an empty element that sets the **installAllOrNone** flag to ON, which configures DPInst to install drivers in a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) only if all of the driver packages in the installation package can be installed or if all of driver packages in the driver package group can be installed.

### **Element Tag**

```
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

By default, the **installAllOrNone** flag is set to OFF. To set the **installAllOrNone** flag to ON for all of the [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840), including those in driver package groups, include an **installAllOrNone** element as a child element of a **dpinst** XML element, or use the **/a** command-line switch. To set the **installAllOrNone** flag to ON only for a specific driver package group, include an **installAllOrNone** element as child element of the corresponding **group** XML element.

The following code example demonstrates an **installAllOrNone** element that is a child element of a **dpinst** element.

```
<dpinst>
  ...
  <installAllOrNone/>
  ...
</dpinst>
```

The following code example demonstrates an **installAllOrNone** element that is a child element of a **group** element.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20installAllOrNone%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





