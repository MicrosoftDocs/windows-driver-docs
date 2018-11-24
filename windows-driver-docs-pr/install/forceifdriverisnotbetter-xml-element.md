---
title: forceIfDriverIsNotBetter XML Element
description: forceIfDriverIsNotBetter XML Element
ms.assetid: ba83c8fd-cc8e-44fd-96ed-855bb42c2493
keywords: ["forceIfDriverIsNotBetter XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- forceIfDriverIsNotBetter XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# forceIfDriverIsNotBetter XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **forceIfDriverIsNotBetter** XML element is an empty element that sets the **forceIfDriverIsNotBetter** flag to ON, which configures DPInst to install a driver on a device even if the driver that is currently installed on the device is a better match than the new driver.

### Element Tag

```cpp
<forceIfDriverIsNotBetter>
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
<td align="left"><p><a href="dpinst-xml-element.md" data-raw-source="[&lt;strong&gt;dpinst&lt;/strong&gt;](dpinst-xml-element.md)"><strong>dpinst</strong></a></p></td>
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

By default, the **forceIfDriverIsNotBetter** flag is set to OFF. You can set the **forceIfDriverIsNotBetter** flag to ON by including a **forceIfDriverIsNotBetter** element as a child element of a [**dpinst XML element**](dpinst-xml-element.md) in a DPinst descriptor file or by using the **/f** command-line switch.

The following code example demonstrates a **forceIfDriverIsNotBetter** element.

```cpp
<dpinst>
  ...
  <forceIfDriverIsNotBetter/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

 

 






