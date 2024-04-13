---
title: Const (WSD)
description: The Web Services for Devices (WSD) Const construct defines the data type and value that must be returned.
keywords:
- Const construct
ms.date: 06/16/2023
---

# Const (WSD)

The Web Services for Devices (WSD) Const construct defines the data type and value that must be returned. Const is used for elements that do not change in value. The Const construct is defined in WsdBidi.xsd.

| Attribute | Description |
|--|--|
| **name** | The name of the schema value. |
| **type** | The type of data in the **value** attribute, a value in the [**BIDI_TYPE**](/windows-hardware/drivers/ddi/winspool/ne-winspool-bidi_type) enumeration. |
| **value** | A string that contains the constant value. |

## Code example

The following code example returns a constant value that has been defined in the bidi extension file for the particular bidi schema query.

```syntax
<Property name="Printer">
  <Property name="Extension">
    <Const name="Version" type="BIDI_INT">1</Const>
  </Property>
</Property>
```

This example results in the following query:

```output
\Printer.Extension.Version:1
```
