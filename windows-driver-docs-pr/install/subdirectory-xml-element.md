---
title: subDirectory XML Element
description: subDirectory XML Element
ms.assetid: 41f86668-148e-4d7c-89b8-e3c21efffd7b
keywords: ["subDirectory XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- subDirectory XML Element
api_type:
- NA
---

# subDirectory XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **subDirectory** XML element specifies one or all the subdirectories under the DPInst working directory.

### Element Tag

```
<subDirectory>
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
<td align="left"><p>[<strong>search</strong>](search-xml-element.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>Specifies one or all of the subdirectories that are relative to the DPInst working directory. This element can contain:</p>
<ul>
<li><p>A string to specify a specific subdirectory</p></li>
<li><p>The wildcard character (<strong>*</strong>) to specify all of the subdirectories</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **search** element that contains one **subDirectory** element that specifies an *i386* subdirectory under the DPInst working directory. The text that specifies the custom subdirectory is shown in bold font style.

```
<dpinst>
  ...
  <search>
    <subDirectory>i386</subDirectory>
  </search>
  ...
</dpinst>
```

The following code example demonstrates a **search** element that contains a **subDirectory** element that specifies all of the subdirectories under the DPInst working directory. The wildcard character (\*) that specifies all of the subdirectories is shown in bold font style.

```
<search>
  <subDirectory>*</subDirectory>
</search>
```

## See also


[**search**](search-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20subDirectory%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





