---
title: language XML Element
description: language XML Element
ms.assetid: 1fc6a3b4-379e-4fd3-b526-c4193e9e84c5
keywords: ["language XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- language XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# language XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **language** XML element localizes and customizes the items that DPInst displays on its wizard pages.

### Element Tag

```cpp
<language>
```

### XML Attributes

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Code</strong></p></td>
<td align="left"><p>A language identifier in hexadecimal format or decimal format.</p></td>
</tr>
</tbody>
</table>

 

### **Element Information**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parent elements</strong></p></td>
<td align="left"><p><a href="dpinst-xml-element.md" data-raw-source="[&lt;strong&gt;dpinst&lt;/strong&gt;](dpinst-xml-element.md)"><strong>dpinst</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p><a href="dpinsttitle-xml-element.md" data-raw-source="[&lt;strong&gt;dpinstTitle&lt;/strong&gt;](dpinsttitle-xml-element.md)"><strong>dpinstTitle</strong></a> (zero or one)</p>
<p><a href="eula-xml-element.md" data-raw-source="[&lt;strong&gt;eula&lt;/strong&gt;](eula-xml-element.md)"><strong>eula</strong></a> (zero or one)</p>
<p><a href="eulaheadertitle-xml-element.md" data-raw-source="[&lt;strong&gt;eulaHeaderTitle&lt;/strong&gt;](eulaheadertitle-xml-element.md)"><strong>eulaHeaderTitle</strong></a> (zero or one)</p>
<p><a href="eulanobutton-xml-element.md" data-raw-source="[&lt;strong&gt;eulaNoButton&lt;/strong&gt;](eulanobutton-xml-element.md)"><strong>eulaNoButton</strong></a> (zero or one)</p>
<p><a href="eulayesbutton-xml-element.md" data-raw-source="[&lt;strong&gt;eulaYesButton&lt;/strong&gt;](eulayesbutton-xml-element.md)"><strong>eulaYesButton</strong></a> (zero or one)</p>
<p><a href="finishtext-xml-element.md" data-raw-source="[&lt;strong&gt;finishText&lt;/strong&gt;](finishtext-xml-element.md)"><strong>finishText</strong></a> (zero or one)</p>
<p><a href="finishtitle-xml-element.md" data-raw-source="[&lt;strong&gt;finishTitle&lt;/strong&gt;](finishtitle-xml-element.md)"><strong>finishTitle</strong></a> (zero or one)</p>
<p><a href="headerpath-xml-element.md" data-raw-source="[&lt;strong&gt;headerPath&lt;/strong&gt;](headerpath-xml-element.md)"><strong>headerPath</strong></a> (zero or one)</p>
<p><a href="icon-xml-element.md" data-raw-source="[&lt;strong&gt;icon&lt;/strong&gt;](icon-xml-element.md)"><strong>icon</strong></a> (zero or one)</p>
<p><a href="installheadertitle-xml-element.md" data-raw-source="[&lt;strong&gt;installHeaderTitle&lt;/strong&gt;](installheadertitle-xml-element.md)"><strong>installHeaderTitle</strong></a> (zero or one)</p>
<p><a href="watermarkpath-xml-element.md" data-raw-source="[&lt;strong&gt;watermarkPath&lt;/strong&gt;](watermarkpath-xml-element.md)"><strong>watermarkPath</strong></a> (zero or one)</p>
<p><a href="welcomeintro-xml-element.md" data-raw-source="[&lt;strong&gt;welcomeIntro&lt;/strong&gt;](welcomeintro-xml-element.md)"><strong>welcomeIntro</strong></a> (zero or one)</p>
<p><a href="welcometitle-xml-element.md" data-raw-source="[&lt;strong&gt;welcomeTitle&lt;/strong&gt;](welcometitle-xml-element.md)"><strong>welcomeTitle</strong></a> (zero or one)</p></td>
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

You can use a **language** element to localize and customize text, the icon, and bitmaps that DPInst displays on its wizard pages. The icon represents DPInst on the Microsoft Windows taskbar, and Windows desktop.

DPInst also uses this icon for the entries that are added to **Programs and Features** in Control Panel. These entries represent the [driver packages](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package) that DPInst installs.

**Note**  In versions of Windows earlier than Windows Vista, DPInst added these entries to **Add or Remove Programs** in Control Panel.

 

To customize the items that appear on the wizard pages in the English-only version of DPInst, use a **language** element that specifies the English (Standard) language and include child elements of the **language** element that customize the items. To localize and customize the items that appear on the DPInst wizard pages in the multi-language version of DPInst, use a **language** element that specifies the language and include child elements of the **language** element that customize the items.

The following code example demonstrates a **language** element that specifies the English (Standard) language and includes customized **dpinstTitle** and **welcomeTitle** XML child elements. The text that specifies the custom text is shown in bold font type.

```cpp
<dpinst>
  ...
  <language code="0x0409">
    ...
    <dpinstTitle>Toaster Device Installer</dpinstTitle>
    <welcomeTitle>Welcome to the toaster Installer!</welcomeTitle>
    ...
  </language>
  ...
</dpinst>
```

If a **dpinstTitle** element is not specified, DPInst displays the default title bar text that appears on the default welcome page.

## See also


[**dpinstTitle**](dpinsttitle-xml-element.md)

[**eula**](eula-xml-element.md)

[**eulaHeaderTitle**](eulaheadertitle-xml-element.md)

[**eulaNoButton**](eulanobutton-xml-element.md)

[**eulaYesButton**](eulayesbutton-xml-element.md)

[**finishText**](finishtext-xml-element.md)

[**finishTitle**](finishtitle-xml-element.md)

[**headerPath**](headerpath-xml-element.md)

[**icon**](icon-xml-element.md)

[**installHeaderTitle**](installheadertitle-xml-element.md)

[**watermarkPath**](watermarkpath-xml-element.md)

[**welcomeIntro**](welcomeintro-xml-element.md)

[**welcomeTitle**](welcometitle-xml-element.md)

 

 






