---
title: promptIfDriverIsNotBetter XML Element
description: promptIfDriverIsNotBetter XML Element
ms.assetid: e5808c64-daa8-4aad-9a63-7ff79b0c2e49
keywords: ["promptIfDriverIsNotBetter XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- promptIfDriverIsNotBetter XML Element
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# promptIfDriverIsNotBetter XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **promptIfDriverIsNotBetter** XML element is an empty element that sets the **promptIfDriverIsNotBetter** flag to ON, which configures DPInst to display a dialog box if a new driver is not a better match to a device than a driver that is currently installed on the device. The dialog box informs a user of this situation and provides an option to replace the driver that is currently installed on the device with the new driver.

### Element Tag

```cpp
<promptIfDriverIsNotBetter>
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

By default, the **promptIfDriverIsNotBetter** flag is set to OFF. You can set the **promptIfDriverIsNotBetter** flag to ON by including a **promptIfDriverIsNotBetter** XML element in a *DPInst.xml* file or by using the **/p** command-line switch.

The following code example demonstrates a **promptIfDriverIsNotBetter** element.

```cpp
<dpinst>
  ...
  <promptIfDriverIsNotBetter/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

 

 






