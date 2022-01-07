---
title: List (WSD)
description: The Web Services for Devices (WSD) `List` construct is a string type that composes a comma-separated list of values specified by the XPath filter query.
keywords:
- List construct
ms.date: 09/08/2021
---

# List (WSD)

The Web Services for Devices (WSD) `List` construct is a string type that composes a comma-separated list of values specified by the XPath filter query. The `List` construct is defined in WsdBidi.xsd.

| Attribute | Description |
|--|--|
| **drvPrinterEvent** | (Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A **TRUE** value indicates that the port monitor sends notifications to the driver; **FALSE** indicates that the port monitor does not send notifications to the driver. |
| **filter** | The XPath query that the WSD monitor applies to the XML document that is specified by the query. See the discussion later in this topic. |
| **name** | The name of the schema value. |
| **query** | The type of query that the WSD monitor performs. |

The XPath language, implemented in Windows beginning with Microsoft XML (MSXML) 2.6, provides a convenient way to specify elements in an XML file. See the [XPath Reference](/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100)) for more information.

The `List` construct is defined in WsdBidi.xsd.

## Code Example

In the following code example, a comma-separated list is composed that contains the allowable number of page images per sheet for N-up printing, for instance "1,2,4".

```xml
<Property name='Layout'>
  <Property name='NumberUp'>
    <Property name='PagesPerSheet'>
      <List name='Supported
        query='wprt:PrinterCapabilities'
        filter='wprt:PrinterCapabilites/wprt:JobValues/wprt:DocumentProcessing/wprt:NumberUp/wprt:NUpPagesPerSheet/wprt:AllowedValue'/>
    </Property>
  </Property>
</Property>
```

The preceding example results in the following query:

```console
\Printer.Layout.NumberUp.PagesPerSheet:Supported
```
