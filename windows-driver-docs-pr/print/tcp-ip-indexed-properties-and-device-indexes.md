---
title: TCP/IP Indexed Properties and Device Indexes
author: windows-driver-content
description: TCP/IP Indexed Properties and Device Indexes
ms.assetid: b26b0c18-1787-43e0-8461-acfbd9fb38f9
keywords:
- TCP/IP indexed properties WDK printer
- indexed properties WDK printer
- device indexes WDK printer
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TCP/IP Indexed Properties and Device Indexes


An indexed property enables a numerical index to be appended to a schema property name, thereby enabling multiple related properties to share the same name, but with each having a numerical index to identify the individual property. An index value must be a positive integer, but there is no upper bound on its size. The schema query determines the index value that should be associated with a particular element. This mechanism allows you to access data in MIB tables.

The IndexedProperty construct defines an indexed property. The following restrictions apply to this construct.

-   An IndexedProperty construct cannot be the parent of a Property construct. A NonIndexedProperty construct is one that defines a property without an index under an IndexedProperty construct.

-   Neither an IndexedProperty construct nor a NonIndexedProperty construct can be the parent of an Installed construct.

A query can also involve another index: a device index. A network device that supports SNMP can be the host for a variety of subdevices, including printers. The MIB tables in network printers have entries that are indexed according to the device type (a device index). In order for a query to retrieve data from the MIB table, the query must have the correct device index. The standard TCP/IP port monitor allows the device index to be configured by the port configuration UI. A bidi extension in which **deviceIndex** is set to **TRUE** (see the [Value](value.md) and [Installed](installed2.md) constructs) causes an OID to be generated with the device index concatenated to the original OID. The index of an indexed property is concatenated to the OID following the device index, if used.

### Code Example

The following code example extends the TCP/IP bidi communications schema by adding a **Display** property to the **Printer** property. In addition, the **Display** property has an indexed property, **Row**, and has **deviceIndex** set to **TRUE**. The schema shown here produces a query that retrieves text from a particular row of the printer's display.

```
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

```
\Printer.Display.Row1:Text
```

The OID generated from this example starts out identical to the **oid** attribute in the **Value** property, but has two indexes appended to it. The appended indexes in the example arise from the **deviceIndex** attribute being set to **TRUE** and **Row** being an indexed property. Assuming that the port configuration UI defines the device index to be 111, and that the text in row 1 of the printer's display is of interest, the OID that is generated would be 1.3.6.1.2.1.43.16.5.1.2.111.1. This OID is identical to the original, except for the device index (111) and property index (1) at the end. If **deviceIndex** had been set to **FALSE** or had been omitted, then the resulting OID would have been 1.3.6.1.2.1.43.16.5.1.2.1. To display text from row *n* of the display, use a property index of *n*.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TCP/IP%20Indexed%20Properties%20and%20Device%20Indexes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


