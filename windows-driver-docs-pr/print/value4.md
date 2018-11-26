---
title: Value (TCP/IP)
description: The TCP/IP Value construct allows you to extend the bidi communications schema with queries that retrieve data from a particular MIB object.
ms.assetid: 46b24830-10a1-405b-9c12-b5804f76d668
keywords:
- Value construct
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Value (TCP/IP)


The TCP/IP `Value` construct allows you to extend the bidi communications schema with queries that retrieve data from a particular MIB object. The `Value` construct is defined in Tcpbidi.xsd.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>deviceIndex</strong></p></td>
<td><p>A flag that, when <strong>TRUE</strong>, means that the associated algorithm must include the device index in the specified OID; when <strong>FALSE</strong>, a trailing zero is appended to the OID. The default value is <strong>FALSE</strong>. For more information, see the note following this table.</p></td>
</tr>
<tr class="even">
<td><p><strong>drvPrinterEvent</strong></p></td>
<td><p>(Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A <strong>TRUE</strong> value indicates that the port monitor sends notifications to the driver; <strong>FALSE</strong> indicates that the port monitor does not send notifications to the driver.</p></td>
</tr>
<tr class="odd">
<td><p><strong>name</strong></p></td>
<td><p>The name of the schema value.</p></td>
</tr>
<tr class="even">
<td><p><strong>oid</strong></p></td>
<td><p>The address of the MIB object, as an object ID (OID).</p></td>
</tr>
<tr class="odd">
<td><p><strong>refreshInterval</strong></p></td>
<td><p>(Optional) The value of the polling interval, in seconds. The default value is 600 seconds.</p></td>
</tr>
<tr class="even">
<td><p><strong>type</strong></p></td>
<td><p>The type of data in the<code> Value</code> construct, a value in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545211" data-raw-source="[&lt;strong&gt;BIDI_TYPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545211)"><strong>BIDI_TYPE</strong></a> enumeration.</p></td>
</tr>
</tbody>
</table>

 

**Note**  A network device that supports the SNMP protocol can be the host for different subdevices, such as Processor, Network, Printer, and Disk Storage. The MIB tables implemented in network printers have entries that are indexed by device indexes. In order to retrieve data from the MIB table (such as the name of an input bin), the query must have a device index that correctly identifies the subdevice. The standard TCP/IP port monitor allows the device index to be manually configured through the port configuration UI. A bidi extension with **deviceIndex**="true" generates an OID with the appropriate device index obtained from the port configuration UI. In addition, if the `Value` construct is contained in a Property instance, the OID will have a zero index appended to its end.

 

### <a href="" id="code-example"></a> Code Example

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

Note that because the `Value` construct is contained in a Property instance rather than an IndexedProperty instance, a trailing zero is automatically appended to the OID.

 

 




