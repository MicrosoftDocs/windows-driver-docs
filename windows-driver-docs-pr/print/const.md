---
title: Const (TCP/IP)
description: The TCP/IP Const construct defines the data type and value that must be returned.
keywords:
- Const construct
ms.date: 06/16/2023
---

# Const (TCP/IP)

The TCP/IP Const construct defines the data type and value that must be returned. Const is used for elements that do not change in value. The Const construct is defined in Tcpbidi.xsd.

| Attribute | Description |
|--|--|
| **name** | The name of the schema value. |
| **type** | The type of data in the **value** attribute, a value in the [**BIDI_TYPE**](/windows-hardware/drivers/ddi/winspool/ne-winspool-bidi_type) enumeration. |
| **value** | A string that contains the constant value. |

## Code example

The following code example extends the bidi communications schema by adding an `Extension` property to the `Printer` property, and a `Version` property to the `Extension` property. In the example, `Extension` contains a constant **value** entry, `Category`. Also, `Version` has two constant **value** entries, `Major` and `Minor`.

```syntax
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

```output
\Printer.Extension:Category
\Printer.Extension.Version:Major
\Printer.Extension.Version:Minor
```
