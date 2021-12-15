---
title: Value (WSD)
description: The WSD Value construct allows you to extend the bidi communications schema with queries that retrieve data from a particular schema element.
keywords:
- Value construct
ms.date: 06/12/2020
---

# Value (WSD)

The WSD `Value` construct allows you to extend the bidi communications schema with queries that retrieve data from a particular schema element in the Web service interface.

| Attribute | Description |
|--|--|
| **drvPrinterEvent** | (Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A **TRUE** value indicates that the port monitor sends notifications to the driver; **FALSE** indicates that the port monitor does not send notifications to the driver. |
| **filter** | The XPath query that the WSD monitor will apply to the XML document that is specified by the query. See the discussion later in this topic. |
| **name** | The name of the schema value. |
| **query** | The type of query that the WSD monitor will perform. |
| **type** | The type of data in the `Value` construct, a value in the [**BIDI_TYPE**](/windows-hardware/drivers/ddi/winspool/ne-winspool-bidi_type) enumeration. |
| **xmllang** | (Optional) A boolean value that, when **TRUE**, means that the associated `Value` construct should be treated as a localizable string value. This means that the XPath query defined above is expected to return a list of nodes differentiated by their xml:lang attributes. The WSD monitor will then search the list of values for the best locale match. The default value is **FALSE**. |

The XPath language is implemented in Windows and provides a convenient way to specify elements in an XML file. See the [XPath Reference](/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100)) for more information.

The **xmllang** attribute is used only when the type attribute of the `Value` construct is either "BIDI\_STRING" or "BIDI\_TEXT".

The `Value` construct is defined in WsdBidi.xsd.

## Example

In the following code example, the WSD monitor determines the size, as an integer value, of RAM memory.

```xml
<Schema xmlns:nprt='https://schemas.microsoft.com/windows/2005/05/wdp/print'>
  <Property name='Printer'>
    <Property name='DeviceInfo'>
      <Value name='PrinterString'
 query='nprt:PrinterDescription'
 filter='nprt:PrinterDescription/nprt:PrinterName'
 type='BIDI_STRING'
 xmllang='true'/>
    </Property>
    <Property name='Configuration'>
      <Property name='Memory'>
        <Value name='Size'
          query='wprt:PrinterConfiguration'
          filter='wprt:PrinterConfiguration/wprt:Storage/wprt:StorageEntry[wprt:Type="RAM"]/wprt:Size'
          type='BIDI_INT'/>
      </Property>
    </Property>
   </Property>
</Schema>
```

The preceding example results in the following queries:

```console
\Printer.DeviceInfo:PrinterString
\Printer.Configuration.Memory:Size
```
