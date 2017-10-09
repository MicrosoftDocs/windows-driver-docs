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
---

# package XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **package** XML element specifies an INF file for a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).

**Element Tag**

```
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
<td align="left"><p>[<strong>group</strong>](group-xml-element.md)</p></td>
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20package%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





