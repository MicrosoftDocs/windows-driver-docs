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
ms.date: 10/17/2018
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
<td align="left"><p><a href="enablenotlistedlanguages-xml-element.md" data-raw-source="[&lt;strong&gt;enableNotListedLanguages&lt;/strong&gt;](enablenotlistedlanguages-xml-element.md)"><strong>enableNotListedLanguages</strong></a> (zero or one)</p>
<p><a href="deletebinaries-xml-element.md" data-raw-source="[&lt;strong&gt;deleteBinaries&lt;/strong&gt;](deletebinaries-xml-element.md)"><strong>deleteBinaries</strong></a> (zero or one)</p>
<p><a href="forceifdriverisnotbetter-xml-element.md" data-raw-source="[&lt;strong&gt;forceIfDriverIsNotBetter&lt;/strong&gt;](forceifdriverisnotbetter-xml-element.md)"><strong>forceIfDriverIsNotBetter</strong></a> (zero or one)</p>
<p><a href="group-xml-element.md" data-raw-source="[&lt;strong&gt;group&lt;/strong&gt;](group-xml-element.md)"><strong>group</strong></a> (zero or more)</p>
<p><a href="headerpath-xml-element.md" data-raw-source="[&lt;strong&gt;headerPath&lt;/strong&gt;](headerpath-xml-element.md)"><strong>headerPath</strong></a> (zero or one)</p>
<p><a href="icon-xml-element.md" data-raw-source="[&lt;strong&gt;icon&lt;/strong&gt;](icon-xml-element.md)"><strong>icon</strong></a> (zero or one)</p>
<p><a href="installallornone-xml-element.md" data-raw-source="[&lt;strong&gt;installAllOrNone&lt;/strong&gt;](installallornone-xml-element.md)"><strong>installAllOrNone</strong></a> (zero or one)</p>
<p><a href="language-xml-element.md" data-raw-source="[&lt;strong&gt;language&lt;/strong&gt;](language-xml-element.md)"><strong>language</strong></a> (zero or more)</p>
<p><a href="legacymode-xml-element.md" data-raw-source="[&lt;strong&gt;legacyMode&lt;/strong&gt;](legacymode-xml-element.md)"><strong>legacyMode</strong></a> (zero or one)</p>
<p><a href="promptifdriverisnotbetter-xml-element.md" data-raw-source="[&lt;strong&gt;promptIfDriverIsNotBetter&lt;/strong&gt;](promptifdriverisnotbetter-xml-element.md)"><strong>promptIfDriverIsNotBetter</strong></a> (zero or one)</p>
<p><a href="quietinstall-xml-element.md" data-raw-source="[&lt;strong&gt;quietInstall&lt;/strong&gt;](quietinstall-xml-element.md)"><strong>quietInstall</strong></a> (zero or one)</p>
<p><a href="scanhardware-xml-element.md" data-raw-source="[&lt;strong&gt;scanHardware&lt;/strong&gt;](scanhardware-xml-element.md)"><strong>scanHardware</strong></a> (zero or one)</p>
<p><a href="search-xml-element.md" data-raw-source="[&lt;strong&gt;search&lt;/strong&gt;](search-xml-element.md)"><strong>search</strong></a> (zero or more)</p>
<p><a href="suppressaddremoveprograms-xml-element.md" data-raw-source="[&lt;strong&gt;suppressAddRemovePrograms&lt;/strong&gt;](suppressaddremoveprograms-xml-element.md)"><strong>suppressAddRemovePrograms</strong></a> (zero or one)</p>
<p><a href="watermarkpath-xml-element.md" data-raw-source="[&lt;strong&gt;watermarkPath&lt;/strong&gt;](watermarkpath-xml-element.md)"><strong>watermarkPath</strong></a> (zero or one)</p></td>
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

 

 






