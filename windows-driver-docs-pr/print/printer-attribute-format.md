---
title: Printer Attribute Format
description: Printer Attribute Format
ms.assetid: 676e9220-4990-4581-8f23-79083afc311c
keywords:
- printer attributes WDK Unidrv , formats
- formats WDK printer attributes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Attribute Format





To specify a printer attribute entry in a GPD file, use the following format:

\* *AttributeName* : *AttributeValue*

where *AttributeName* is a predefined name belonging to one of the [attribute types](attribute-types.md), and *AttributeValue* is one of the [GPD value types](gpd-value-types.md).

For example, the \*ModelName attribute is used for specifying a text string that describes your printer hardware. To assign a value to this attribute, you could place the following line in your GPD file:

```cpp
*ModelName: "Canon Bubble-Jet BJC-600"
```

All attribute names are predefined and are recognized by Unidrv's GPD parser.

 

 




