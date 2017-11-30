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
---

# language XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **language** XML element localizes and customizes the items that DPInst displays on its wizard pages.

### Element Tag

```
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
<td align="left"><p>[<strong>dpinst</strong>](dpinst-xml-element.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>[<strong>dpinstTitle</strong>](dpinsttitle-xml-element.md) (zero or one)</p>
<p>[<strong>eula</strong>](eula-xml-element.md) (zero or one)</p>
<p>[<strong>eulaHeaderTitle</strong>](eulaheadertitle-xml-element.md) (zero or one)</p>
<p>[<strong>eulaNoButton</strong>](eulanobutton-xml-element.md) (zero or one)</p>
<p>[<strong>eulaYesButton</strong>](eulayesbutton-xml-element.md) (zero or one)</p>
<p>[<strong>finishText</strong>](finishtext-xml-element.md) (zero or one)</p>
<p>[<strong>finishTitle</strong>](finishtitle-xml-element.md) (zero or one)</p>
<p>[<strong>headerPath</strong>](headerpath-xml-element.md) (zero or one)</p>
<p>[<strong>icon</strong>](icon-xml-element.md) (zero or one)</p>
<p>[<strong>installHeaderTitle</strong>](installheadertitle-xml-element.md) (zero or one)</p>
<p>[<strong>watermarkPath</strong>](watermarkpath-xml-element.md) (zero or one)</p>
<p>[<strong>welcomeIntro</strong>](welcomeintro-xml-element.md) (zero or one)</p>
<p>[<strong>welcomeTitle</strong>](welcometitle-xml-element.md) (zero or one)</p></td>
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20language%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





