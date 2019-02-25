---
title: TCP/IP Indexed Properties and Device Indexes
description: TCP/IP Indexed Properties and Device Indexes
ms.assetid: b26b0c18-1787-43e0-8461-acfbd9fb38f9
keywords:
- TCP/IP indexed properties WDK printer
- indexed properties WDK printer
- device indexes WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TCP/IP Indexed Properties and Device Indexes


An indexed property enables a numerical index to be appended to a schema property name, thereby enabling multiple related properties to share the same name, but with each having a numerical index to identify the individual property. An index value must be a positive integer, but there is no upper bound on its size. The schema query determines the index value that should be associated with a particular element. This mechanism allows you to access data in MIB tables.

The IndexedProperty construct defines an indexed property. The following restrictions apply to this construct.

-   An IndexedProperty construct cannot be the parent of a Property construct. A NonIndexedProperty construct is one that defines a property without an index under an IndexedProperty construct.

-   Neither an IndexedProperty construct nor a NonIndexedProperty construct can be the parent of an Installed construct.

A query can also involve another index: a device index. A network device that supports SNMP can be the host for a variety of subdevices, including printers. The MIB tables in network printers have entries that are indexed according to the device type (a device index). In order for a query to retrieve data from the MIB table, the query must have the correct device index. The standard TCP/IP port monitor allows the device index to be configured by the port configuration UI. A bidi extension in which **deviceIndex** is set to **TRUE** (see the [Value](value.md) and [Installed](installed2.md) constructs) causes an OID to be generated with the device index concatenated to the original OID. The index of an indexed property is concatenated to the OID following the device index, if used.

### Code Example

The following code example extends the TCP/IP bidi communications schema by adding a **Display** property to the **Printer** property. In addition, the **Display** property has an indexed property, **Row**, and has **deviceIndex** set to **TRUE**. The schema shown here produces a query that retrieves text from a particular row of the printer's display.

```cpp
<Property name="Printer">
  <Property name="Display">
    <IndexedProperty name="Row">
      <Value name="Text" type="BIDI_TEXT" 
             oid="1.3.6.1.2.1.43.16.5.1.2" deviceIndex="true"/>
    </IndexedProperty>
  </Property>
</Property>
```

The preceding example results in the following query:

```cpp
\Printer.Display.Row1:Text
```

The OID generated from this example starts out identical to the **oid** attribute in the **Value** property, but has two indexes appended to it. The appended indexes in the example arise from the **deviceIndex** attribute being set to **TRUE** and **Row** being an indexed property. Assuming that the port configuration UI defines the device index to be 111, and that the text in row 1 of the printer's display is of interest, the OID that is generated would be 1.3.6.1.2.1.43.16.5.1.2.111.1. This OID is identical to the original, except for the device index (111) and property index (1) at the end. If **deviceIndex** had been set to **FALSE** or had been omitted, then the resulting OID would have been 1.3.6.1.2.1.43.16.5.1.2.1. To display text from row *n* of the display, use a property index of *n*.

 

 




