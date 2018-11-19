---
title: Const (WSD)
description: The Web Services for Devices (WSD) Const construct defines the data type and value that must be returned.
ms.assetid: e9bcf007-0117-48a9-9873-a9bbc5702e29
keywords:
- Const construct
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Const (WSD)


The Web Services for Devices (WSD) Const construct defines the data type and value that must be returned. Const is used for elements that do not change in value. The Const construct is defined in WsdBidi.xsd.

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

The following code example returns a constant value that has been defined in the bidi extension file for the particular bidi schema query.

```cpp
<Property name="Printer">
  <Property name="Extension">
    <Const name="Version" type="BIDI_INT">1</Const>
  </Property>
</Property>
```

This example results in the following query:

```cpp
\Printer.Extension.Version:1
```

 

 




