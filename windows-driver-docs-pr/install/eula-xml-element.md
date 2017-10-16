---
title: eula XML Element
description: eula XML Element
ms.assetid: ab647583-b0e1-4f40-86af-9b7923f5535c
keywords: ["eula XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- eula XML Element
api_type:
- NA
---

# eula XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **eula** XML element is an empty XML element that includes two attributes that specify a EULA text file that contains custom text for a DPInst EULA page.

### Element Tag

```
<eula>
```

### XML Attributes

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Type</strong></p></td>
<td align="left"><p>The type of vendor-supplied EULA. The value of this attribute must be set to the string &quot;txt&quot;, which indicates a plain-text file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Path</strong></p></td>
<td align="left"><p>A string that identifies the name of the file that contains the text for a DPInst EULA page. The EULA text file must be encoded by using UTF-8 encoding. The EULA file must be located in the DPInst root directory, which is the directory that contains the DPInst executable file (<em>DPInst.exe</em>), or a subdirectory under the DPInst root directory. If the EULA file is in a subdirectory, specify a fully qualified file name that is relative to the DPInst root directory.</p></td>
</tr>
</tbody>
</table>

 

### Element Information

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parent elements</strong></p></td>
<td align="left"><p>[<strong>language</strong>](language-xml-element.md)</p></td>
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

The following code example demonstrates a **eula** element that specifies that *Data\\Eula409.txt* contains custom EULA text. The *Eula409.txt* file is in the *Data* directory, which must be a subdirectory under the DPInst root directory. The text that specifies the custom EULA file is shown below using the &lt;eula&gt; tag.

```
<dpinst>
  ...
  <language code="0x0409">
    ...
    <eula type="txt" path="Data\Eula409.txt"/>
    ...
  </language>
  ...
</dpinst>
```

## See also


[**language**](language-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20eula%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





