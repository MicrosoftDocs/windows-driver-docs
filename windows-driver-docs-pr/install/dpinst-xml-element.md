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
ms.localizationpriority: medium
---

# dpinst XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **dpinst** XML element is the root XML element in a DPInst descriptor file that contains the child elements that customize driver installation.

### Element Tag

```cpp
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

```cpp
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

 

 






