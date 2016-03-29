---
title: Printer Attribute Format
description: Printer Attribute Format
ms.assetid: 676e9220-4990-4581-8f23-79083afc311c
keywords: ["printer attributes WDK Unidrv , formats", "formats WDK printer attributes"]
---

# Printer Attribute Format


## <a href="" id="ddk-printer-attribute-format-gg"></a>


To specify a printer attribute entry in a GPD file, use the following format:

\* *AttributeName* : *AttributeValue*

where *AttributeName* is a predefined name belonging to one of the [attribute types](attribute-types.md), and *AttributeValue* is one of the [GPD value types](gpd-value-types.md).

For example, the \*ModelName attribute is used for specifying a text string that describes your printer hardware. To assign a value to this attribute, you could place the following line in your GPD file:

```
*ModelName: "Canon Bubble-Jet BJC-600"
```

All attribute names are predefined and are recognized by Unidrv's GPD parser.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Attribute%20Format%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




