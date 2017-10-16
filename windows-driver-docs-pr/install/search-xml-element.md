---
title: search XML Element
description: search XML Element
ms.assetid: 34eff240-a96a-4b73-a001-5ea698e9f7ae
keywords: ["search XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- search XML Element
api_type:
- NA
---

# search XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **search** XML element directs DPInst to search recursively for INF files in specified subdirectories under the DPInst working directory. Subdirectories are specified by one or more [**subDirectory child elements**](subdirectory-xml-element.md).

### Element Tag

```
<search>
```

### XML Attributes

None

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
<td align="left"><p>[<strong>subDirectory</strong>](subdirectory-xml-element.md) (zero or more)</p></td>
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

The following code example demonstrates a **search** element that contains one **subDirectory** XML element that specifies the *i386* subdirectory. DPInst will recursively search for [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840) in the *i386* subdirectory of the DPInst working directory. The text that specifies the custom subdirectory is shown in bold font style.

```
<dpinst>
  ...
  <search>
    <subDirectory>i386</subDirectory>
  </search>
  ...
</dpinst>
```

**Note**  Because duplicate child elements are not permitted, each **subDirectory** child element of a **search** element must be unique.

 

## See also


[**dpinst**](dpinst-xml-element.md)

[**subDirectory**](subdirectory-xml-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20search%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





