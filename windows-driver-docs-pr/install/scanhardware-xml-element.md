---
title: scanHardware XML Element
description: scanHardware XML Element
keywords: ["scanHardware XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- scanHardware XML Element
api_type:
- NA
ms.date: 10/17/2018
---

# scanHardware XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](./difx-guidelines.md).\]

The **scanHardware** XML element is an empty element that sets the **scanHardware** flag to ON. Setting this flag to ON configures DPInst to install a [driver package](./driver-packages.md) for a Plug and Play (PnP) function driver only if the driver package matches a device that is configured in a computer and the driver package is a better match for the device than the driver package that is currently installed on the device.

### Element Tag

```cpp
<scanHardware>
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

By default, the **scanHardware** flag is set to OFF. You can set the **scanHardware** flag to ON by including an **scanHardware** XML element as a child element of a **dpinst** XML element in a DPInst descriptor file or by using the **/sh** command-line switch.

The following code example demonstrates a **scanHardware** element.

```cpp
<dpinst>
  ...
  <scanHardware/>
  ...
</dpinst>
```

 

