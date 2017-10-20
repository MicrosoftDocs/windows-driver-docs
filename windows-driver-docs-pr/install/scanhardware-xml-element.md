---
title: scanHardware XML Element
description: scanHardware XML Element
ms.assetid: c1af7238-97e9-4c5f-95ea-fbc9f3cc8279
keywords: ["scanHardware XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- scanHardware XML Element
api_type:
- NA
---

# scanHardware XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **scanHardware** XML element is an empty element that sets the **scanHardware** flag to ON. Setting this flag to ON configures DPInst to install a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) for a Plug and Play (PnP) function driver only if the driver package matches a device that is configured in a computer and the driver package is a better match for the device than the driver package that is currently installed on the device.

### Element Tag

```
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
<td align="left"><p>[<strong>dpinst</strong>](dpinst-xml-element.md)</p></td>
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

```
<dpinst>
  ...
  <scanHardware/>
  ...
</dpinst>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20scanHardware%20XML%20Element%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




