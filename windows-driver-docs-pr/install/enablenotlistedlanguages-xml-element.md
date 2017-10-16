---
title: enableNotListedLanguages XML Element
description: The enableNotListedLanguages XML element is an empty element that sets the enableNotListedLanguages flag to ON, which configures DPInst to enable all of the supported languages that are not explicitly enabled by language XML elements in a DPInst.xml file.
ms.assetid: 7584b222-71b0-4532-84be-3444a4a7003b
keywords: ["enableNotListedLanguages XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- enableNotListedLanguages XML Element
api_type:
- NA
---

# enableNotListedLanguages XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **enableNotListedLanguages** XML element is an empty element that sets the **enableNotListedLanguages** flag to ON, which configures DPInst to enable all of the supported languages that are not explicitly enabled by [**language**](language-xml-element.md) XML elements in a *DPInst.xml* file.

### Element Tag

```
<enableNotListedLanguages>
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
<td align="left"><p>[<strong>dpinst</strong>](dpinst-xml-element.md)</p></td>
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

By default, all of the DPInst-supported languages are enabled if a *DPInst.xml* file does not contain any **language** elements. However, if the *DPInst.xml* file contains **language** elements, only the languages that are explicitly specified by the **language** elements are enabled and all of the other languages are implicitly disabled. To enable all of the languages that are implicitly disabled, set the **enableNotListedLanguages** flag to ON by including an **enableNotListedLanguages** element as a child element of a **dpinst** XML element or use the **/el** command-line switch.

The following code example demonstrates an **enableNotListedLanguages** element.

```
<dpinst>
  ...
  <enableNotListedLanguages/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20enableNotListedLanguages%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





