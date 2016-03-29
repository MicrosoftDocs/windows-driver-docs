---
title: Const
description: Const
ms.assetid: e9bcf007-0117-48a9-9873-a9bbc5702e29
keywords: ["Const construct"]
---

# Const


The Web Services for Devices (WSD) Const construct defines the data type and value that must be returned. Const is used for elements that do not change in value. The Const construct is defined in WsdBidi.xsd.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>name</strong></p></td>
<td align="left"><p>The name of the schema value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>type</strong></p></td>
<td align="left"><p>The type of data in the <strong>value</strong> attribute, a value in the [<strong>BIDI_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545211) enumeration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>value</strong></p></td>
<td align="left"><p>A string that contains the constant value.</p></td>
</tr>
</tbody>
</table>

 

### Code Example

The following code example returns a constant value that has been defined in the bidi extension file for the particular bidi schema query.

```
<Property name="Printer">
  <Property name="Extension">
    <Const name="Version" type="BIDI_INT">1</Const>
  </Property>
</Property>
```

This example results in the following query:

```
\Printer.Extension.Version:1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Const%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




