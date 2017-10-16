---
title: dpinst XML Element
description: dpinst XML Element
ms.assetid: d825afb4-a459-4b69-93cb-db57adab3c80
keywords: ["dpinst XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- dpinst XML Element
api_type:
- NA
---

# dpinst XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **dpinst** XML element is the root XML element in a DPInst descriptor file that contains the child elements that customize driver installation.

### Element Tag

```
<dpinst>
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
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>[<strong>enableNotListedLanguages</strong>](enablenotlistedlanguages-xml-element.md) (zero or one)</p>
<p>[<strong>deleteBinaries</strong>](deletebinaries-xml-element.md) (zero or one)</p>
<p>[<strong>forceIfDriverIsNotBetter</strong>](forceifdriverisnotbetter-xml-element.md) (zero or one)</p>
<p>[<strong>group</strong>](group-xml-element.md) (zero or more)</p>
<p>[<strong>headerPath</strong>](headerpath-xml-element.md) (zero or one)</p>
<p>[<strong>icon</strong>](icon-xml-element.md) (zero or one)</p>
<p>[<strong>installAllOrNone</strong>](installallornone-xml-element.md) (zero or one)</p>
<p>[<strong>language</strong>](language-xml-element.md) (zero or more)</p>
<p>[<strong>legacyMode</strong>](legacymode-xml-element.md) (zero or one)</p>
<p>[<strong>promptIfDriverIsNotBetter</strong>](promptifdriverisnotbetter-xml-element.md) (zero or one)</p>
<p>[<strong>quietInstall</strong>](quietinstall-xml-element.md) (zero or one)</p>
<p>[<strong>scanHardware</strong>](scanhardware-xml-element.md) (zero or one)</p>
<p>[<strong>search</strong>](search-xml-element.md) (zero or more)</p>
<p>[<strong>suppressAddRemovePrograms</strong>](suppressaddremoveprograms-xml-element.md) (zero or one)</p>
<p>[<strong>watermarkPath</strong>](watermarkpath-xml-element.md) (zero or one)</p></td>
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

The following code example demonstrates an XML declaration element, followed by a **dpinst** element, which contains zero or more child elements.

```
<?xml version="1.0" ?>
<dpinst>
  ...
</dpinst>
```

**Note**  Because duplicate child elements are not permitted, each **search** child element and **language** element of a **dpinst** element must be unique.

 

## See also


[**deleteBinaries**](deletebinaries-xml-element.md)

[**enableNotListedLanguages**](enablenotlistedlanguages-xml-element.md)

[**forceIfDriverIsNotBetter**](forceifdriverisnotbetter-xml-element.md)

[**group**](group-xml-element.md)

[**headerPath**](headerpath-xml-element.md)

[**icon**](icon-xml-element.md)

[**installAllOrNone**](installallornone-xml-element.md)

[**language**](language-xml-element.md)

[**legacyMode**](legacymode-xml-element.md)

[**promptIfDriverIsNotBetter**](promptifdriverisnotbetter-xml-element.md)

[**quietInstall**](quietinstall-xml-element.md)

[**scanHardware**](scanhardware-xml-element.md)

[**search**](search-xml-element.md)

[**suppressAddRemovePrograms**](suppressaddremoveprograms-xml-element.md)

[**watermarkPath**](watermarkpath-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20dpinst%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





