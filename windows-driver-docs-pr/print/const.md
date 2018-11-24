---
title: Const (TCP/IP)
description: The TCP/IP Const construct defines the data type and value that must be returned.
ms.assetid: a0ede11d-ada4-4dc4-87a4-68c96635c0fd
keywords:
- Const construct
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Const (TCP/IP)


The TCP/IP Const construct defines the data type and value that must be returned. Const is used for elements that do not change in value. The Const construct is defined in Tcpbidi.xsd.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>name</strong></p></td>
<td><p>The name of the schema value.</p></td>
</tr>
<tr class="even">
<td><p><strong>type</strong></p></td>
<td><p>The type of data in the <strong>value</strong> attribute, a value in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545211" data-raw-source="[&lt;strong&gt;BIDI_TYPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545211)"><strong>BIDI_TYPE</strong></a> enumeration.</p></td>
</tr>
<tr class="odd">
<td><p><strong>value</strong></p></td>
<td><p>A string that contains the constant value.</p></td>
</tr>
</tbody>
</table>

 

### Code Example

The following code example extends the bidi communications schema by adding an `Extension` property to the `Printer` property, and a `Version` property to the `Extension` property. In the example, `Extension` contains a constant **value** entry, `Category`. Also, `Version` has two constant **value** entries, `Major` and `Minor`.

```cpp
<Property name="Printer">
  <Property name="Extension">
    <Const name="Category" type="BIDI_STRING" value="Extension"/>
    <Property name="Version">
      <Const name="Major" type="BIDI_INT" value="1"/>
      <Const name="Minor" type="BIDI_INT" value="0"/>
    </Property>
  </Property>
</Property>
```

The preceding example results in the following queries:

```cpp
\Printer.Extension:Category
\Printer.Extension.Version:Major
\Printer.Extension.Version:Minor
```

 

 




