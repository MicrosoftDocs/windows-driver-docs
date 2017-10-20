---
title: watermarkPath XML Element
description: watermarkPath XML Element
ms.assetid: 3c64738b-4ead-4e78-a1bd-45d098a11dad
keywords: ["watermarkPath XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- watermarkPath XML Element
api_type:
- NA
---

# watermarkPath XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **watermarkPath** element specifies the source file for a custom watermark bitmap that DPInst displays on the left side of the DPInst welcome page and the DPInst finish page.

### Element Tag

```
<watermarkPath>
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
<td align="left"><p>String that specifies the name of the file that contains a watermark bitmap that DPInst displays on the left side of a welcome page and a finish page. The watermark file must be located in the DPInst root directory, which is the directory that contains the DPInst executable file (<em>DPInst.exe</em>), or in a subdirectory under the DPInst root directory. If the watermark bitmap file is in a subdirectory, specify a fully qualified file name that is relative to the DPInst root directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

A **watermarkPath** element is customized, but not localized, if it is a child element of a **dpinst** element. A **watermarkPath** element is customized and localized if it is a child element of a **language** element.

The following code example demonstrates a **watermarkPath** element that specifies *Data\\Watermark.bmp* as the source of the watermark bitmap that DPInst displays on the left side of the welcome and finish pages. The text that specifies the custom watermark bitmap file is shown in bold font style.

```
<dpinst>
  ...
  <watermarkPath>Data\Watermark.bmp</watermarkPath>
  ...
</dpinst>
```

If a **watermarkPath** element is not specified, DPInst uses a default watermark.

## See also


[**dpinst**](dpinst-xml-element.md)

[**language**](language-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20watermarkPath%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





