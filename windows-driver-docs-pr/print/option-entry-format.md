---
title: Option Entry Format
author: windows-driver-content
description: Option Entry Format
ms.assetid: defc035a-d571-4bf1-abeb-c7528ba23b81
keywords: ["printer options WDK Unidrv , entry format", "formats WDK printer options"]
---

# Option Entry Format


## <a href="" id="ddk-option-entry-format-gg"></a>


To specify a printer option entry in a GPD file, use the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*<strong>Option</strong>: <em>OptionName</em> { <em>OptionAttributes</em> }</p></td>
</tr>
</tbody>
</table>

 

where *OptionName* is either the name of one of the predefined [standard options](standard-options.md) or a customized option name, and *OptionAttributes* is a set of [option attributes](option-attributes.md).

For an example of a set of \***Option** entries associated with a feature, see [Feature Entry Format](feature-entry-format.md).

If you repeat an option specification, for example by specifying two or more \***Option** entries for the **PaperSize** feature's LETTER option, each duplicate option attribute within the \***Option** entry overwrites the previous one, and the GPD parser only retains the last one encountered. On the other hand, if the GPD parser encounters two or more \*Feature entries for the **PaperSize** (or any other) feature, \***Option** entries not previously specified are added to the parser's database.

You can control the order in which options are displayed to the user. See [Specifying Feature and Option Display Order](specifying-feature-and-option-display-order.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Option%20Entry%20Format%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


