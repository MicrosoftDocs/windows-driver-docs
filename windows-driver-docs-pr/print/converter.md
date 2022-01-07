---
title: Converter (TCP/IP)
description:  Extends the bidi communications schema with queries that retrieve data from a particular MIB object.
ms.date: 09/08/2021
---

# Converter (TCP/IP)

The TCP/IP Converter construct enables you to extend the [bidi communications](bidirectional-communication.md) schema with queries that retrieve data from a particular MIB (SNMP Management Information Base) object and then convert the data to a string value that is based on a list of value pairs that are specified in Conversion elements. The Converter construct is defined in Tcpbidi.xsd.

| Attribute | Description |
|--|--|
| **deviceIndex** | (Optional) A Boolean value that, when **TRUE**, means that the associated algorithm must include the device index in the specified OID; when this attribute **FALSE**, a trailing zero is appended to the OID. The default value is **FALSE**. For more information, see the note following this table. |
| **drvPrinterEvent** | (Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A **TRUE** value indicates that the port monitor sends notifications to the driver; **FALSE** indicates that the port monitor does not send notifications to the driver. |
| **name** | A string value that represents the name of the schema element. |
| **oid** | A string value that represents the address of the MIB object, as an object ID (OID). |
| **refreshInterval** | (Optional) An integer value of the polling interval, in seconds. The default value is 600 seconds. |
| **useFirstIndex** | (Optional) A Boolean value that can be set to read the first entry in a MIB table. This attribute is used only when the Converter construct is within a Property instance. |

> [!NOTE]
> A network device that supports the SNMP protocol can be the host for different subdevices, such as Processor, Network, Printer, and Disk Storage. The MIB tables that are implemented in network printers have entries that are indexed by device indexes. To retrieve data from the MIB table (such as the name of an input bin), the query must have a device index that correctly identifies the subdevice. The standard TCP/IP port monitor allows the device index to be manually configured through the port configuration UI. A bidi extension with the **deviceIndex** attribute set to **TRUE** generates an OID with the appropriate device index that is obtained from the port configuration UI. In addition, if the Converter construct is contained in a Property instance and the **deviceIndex** attribute is missing or set to **FALSE**, the OID will have a zero index appended to its end.

The following MIB data types are supported by the conversion routines:

- INTEGER

- Integer32

- Gauge32

- Counter32

- TimeTicks

- Unsigned32

- Counter64

- Opaque

- OCTET STRING

- OBJECT IDENTIFIER

## Conversion Element

Each Converter construct will include one or more Conversion elements to define the mapping of values read from the MIB elements into Bidi schema values.

| Attribute | Description |
|--|--|
| mibValue | (Optional) A string value that represents one possible data value that could be read from the MIB. |
| bidiValue | (Optional) A string value that represents the bidi value that is returned if the data matches the **mibValue** attribute for this Conversion element. |

## Code example

The following code example extends the bidi communications schema by adding new properties and Converter constructs.

```xml
<Property name="Printer">
  <Property name="Layout">
    <Property name="InputBins">
      <IndexedProperty name="Bin">
        <Converter name="BinType" oid="1.3.6.1.2.1.43.8.2.1.2" deviceIndex="true">
          <Conversion mibValue="2" bidiValue="Unknown"/>
          <Conversion mibValue="3" bidiValue="SheetFeedAutoRemovableTray"/>
          <Conversion mibValue="4" bidiValue="SheetFeedAutoNonRemovableTray"/>
          <Conversion mibValue="5" bidiValue="SheetFeedManual"/>
          <Conversion mibValue="6" bidiValue="ContinuousRoll"/>
          <Conversion mibValue="7" bidiValue="ContinuousFanFold"/>
        </Converter>
      </IndexedProperty>
    </Property>
    <Property name="Orientation">
      <Converter name="CurrentValue" oid="1.3.6.1.2.1.43.15.1.1.7" deviceIndex="true" useFirstIndex="true">
        <Conversion mibValue="3" bidiValue="Portrait"/>
        <Conversion mibValue="4" bidiValue="Landscape"/>
     </Converter>
   </Property>
 </Property>
 <Property name="Custom">
    <Property name="HostResourceMIB">
      <Converter name="InterfaceName" oid="1.3.6.1.2.1.2.1">
      <Conversion mibValue="1" bidiValue="InterfaceOne"/>
    <Conversion mibValue="2" bidiValue="InterfaceTwo"/>
     </Converter>
  </Property>
 </Property
</Property>
```

The preceding example results in the following queries.

```xml
\Printer.Layout.InputBins.Bin###:BinType
\Printer.Layout.Orientation:CurrentValue
\Printer.Custom.HostResourceMIB:InterfaceName
```

The Converter construct for `BinType` is contained in an IndexedProperty instance, and, as a result, the current MIB table row entry is automatically appended to the OID.

Because the Converter construct for `CurrentValue` is contained in a Property instance and the **useFirstIndex** attribute is set to "true", a trailing "1" is automatically appended to the OID.

The Converter construct for `InterfaceName` is contained in a Property instance, so a trailing zero automatically being appended to the OID.
