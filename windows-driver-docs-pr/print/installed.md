---
title: Installed (WSD)
description: The Web Services for Devices (WSD) Installed construct indicates whether a printer feature that matches a given set of criteria has been installed.
keywords:
- Installed construct
ms.date: 06/05/2020
---

# Installed (WSD)

The Web Services for Devices (WSD) Installed construct indicates whether a printer feature that matches a given set of criteria has been installed. If an XPath filter obtains a valid XML result when applied to the given criteria, this algorithm returns **TRUE**. The Installed construct is defined in WsdBidi.xsd.

| Attribute | Description |
| --- | --- |
| **drvPrinterEvent** | (Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A **TRUE** value indicates that the port monitor sends notifications to the driver; **FALSE** indicates that the port monitor does not send notifications to the driver. |
| **filter** | The XPath query that the WSD monitor applies to the XML document that is specified by the query. See the discussion later in this topic. |
| **name** | The name of the schema value. |
| **query** | The type of query that the WSD monitor will perform. |

The XPath language, implemented in Windows beginning with Microsoft XML (MSXML) 2.6, provides a convenient way to specify elements in an XML file. See the [XPath Reference](/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100)) for more information.

The behavior of an Installed construct depends on the definition of its parent nodes. If an Installed construct is specified without the use of a Parameter, the schema will always exist when queried. If an Installed construct is specified with the use of a Parameter, the schema will exist only if the associated Parameter value is found in the current WSD device queries. The software that is making the queries must be able to handle the case where the Installed schema is not returned.

The Installed construct is defined in WsdBidi.xsd.

## Code Example

In the following code example, the filter lookup algorithm uses an XPath query to confirm that a hard disk is installed.

```xml
<Schema>
  <Property name='Printer'>
    <Property name='Configuration'>
      <Property name='HardDisk'>
        <Installed name='Installed'
            query='wprt:PrinterConfiguration'
            filter='wprt:PrinterConfiguration/wprt:Storage/wprt:StorageEntry[wprt:Type="HardDisk"]'/>
      </Property>
    </Property>
  </Property>
</Schema>
```

The preceding example results in the following query:

```cpp
\Printer.Configuration.HardDisk:Installed
```
