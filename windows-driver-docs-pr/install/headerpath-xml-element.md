---
title: headerPath XML Element
description: headerPath XML Element
ms.assetid: 9764fed5-75bc-4679-bae0-5bfe738268e2
keywords: ["headerPath XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- headerPath XML Element
api_type:
- NA
---

# headerPath XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **headerPath** XML element specifies the source file name for a custom header bitmap that DPInst displays in the upper-right corner of the DPInst EULA page and DPInst installation page.

### Element Tag

```
<headerPath>
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
<td align="left"><p>[<strong>dpinst</strong>](dpinst-xml-element.md) or [<strong>language</strong>](language-xml-element.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>String that specifies the file name of the header bitmap that DPInst displays in the upper-right corner of the DPInst EULA and installation pages. The header bitmap file must be located in the DPInst root directory, which is the directory that contains the DPInst executable file (<em>DPInst.exe</em>), or in a subdirectory under the DPInst root directory. If the header bitmap file is in a subdirectory, specify a fully qualified file name that is relative to the DPInst root directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

A **headerPath** element is customized, but not localized, if it is a child element of a **dpinst** XML element. A **headerPath** element is customized and localized if it is a child element of a **language** XML element.

The following code example demonstrates a **headerPath** element that specifies *Data\\Header.bmp* as the header bitmap file that DPInst displays in the upper-right corner of a DPInst EULA and installation pages and an installation page. The text that specifies the custom header bitmap file is shown in bold font style.

```
<dpinst>
  ...
  <headerPath>Data\Header.bmp</headerPath>
  ...
</dpinst>
```

If a **headerPath** element is not specified, DPInst uses a default header bitmap.

## See also


[**dpinst**](dpinst-xml-element.md)

[**language**](language-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20headerPath%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





