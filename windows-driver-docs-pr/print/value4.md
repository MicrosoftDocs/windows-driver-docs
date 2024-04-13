---
title: Value (TCP/IP)
description: The TCP/IP Value construct allows you to extend the bidi communications schema with queries that retrieve data from a particular MIB object.
keywords:
- Value construct
ms.date: 02/21/2024
---

# Value (TCP/IP)

The TCP/IP `Value` construct allows you to extend the bidi communications schema with queries that retrieve data from a particular MIB object. The `Value` construct is defined in Tcpbidi.xsd.

| Attribute | Description |
|--|--|
| **deviceIndex** | A flag that, when **TRUE**, means that the associated algorithm must include the device index in the specified OID; when **FALSE**, a trailing zero is appended to the OID. The default value is **FALSE**. For more information, see the note following this table. |
| **drvPrinterEvent** | (Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A **TRUE** value indicates that the port monitor sends notifications to the driver. **FALSE** indicates that the port monitor doesn't send notifications to the driver. |
| **name** | The name of the schema value. |
| **oid** | The address of the MIB object, as an object ID (OID). |
| **refreshInterval** | (Optional) The value of the polling interval, in seconds. The default value is 600 seconds. |
| **type** | The type of data in the Value construct, a value in the [**BIDI_TYPE**](/windows-hardware/drivers/ddi/winspool/ne-winspool-bidi_type) enumeration. |

 A network device that supports the Simple Network Management Protocol (SNMP) protocol can be the host for different subdevices, such as Processor, Network, Printer, and Disk Storage. The MIB tables implemented in network printers have entries that are indexed with device indexes. In order to retrieve data from the MIB table (such as the name of an input bin), the query must have a device index that correctly identifies the subdevice. The standard TCP/IP port monitor allows the device index to be manually configured through the port configuration UI. A bidi extension with **deviceIndex**="true" generates an OID with the appropriate device index obtained from the port configuration UI. In addition, if the `Value` construct is contained in a Property instance, the OID has a zero index appended to its end.

## Example

The following code example extends the bidi communications schema by adding a new property, **System**, to the **Printer** property. The **System** property has a `Value` construct, with **name**, **type**, and **oid** attributes.

```cpp
<Property name="Printer">
  <Property name="System">
    <Value name="Name" type="BIDI_STRING" oid="1.3.6.1.2.1.1.5"/>
  </Property>
</Property>
```

The preceding example results in the following query:

```cpp
\Printer.System:Name
```

Because the `Value` construct is contained in a Property instance rather than an IndexedProperty instance, a trailing zero is automatically appended to the OID.
