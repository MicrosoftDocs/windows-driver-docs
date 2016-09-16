---
title: Value
author: windows-driver-content
description: Value
MS-HAID:
- 'autocfg\_3bbe982a-9be4-40c6-8ba3-6d1fbd2225b0.xml'
- 'print.value4'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 46b24830-10a1-405b-9c12-b5804f76d668
keywords: ["Value construct"]
---

# Value


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
<td><p>The type of data in the<code> Value</code> construct, a value in the [<strong>BIDI_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545211) enumeration.</p></td>
</tr>
</tbody>
</table>

 

**Note**  A network device that supports the SNMP protocol can be the host for different subdevices, such as Processor, Network, Printer, and Disk Storage. The MIB tables implemented in network printers have entries that are indexed by device indexes. In order to retrieve data from the MIB table (such as the name of an input bin), the query must have a device index that correctly identifies the subdevice. The standard TCP/IP port monitor allows the device index to be manually configured through the port configuration UI. A bidi extension with **deviceIndex**="true" generates an OID with the appropriate device index obtained from the port configuration UI. In addition, if the `Value` construct is contained in a Property instance, the OID will have a zero index appended to its end.

 

### <a href="" id="code-example"></a> Code Example

The following code example extends the bidi communications schema by adding a new property, **System**, to the **Printer** property. The **System** property has a `Value` construct, with **name**, **type**, and **oid** attributes.

```
<Property name="Printer">
  <Property name="System">
    <Value name="Name" type="BIDI_STRING" oid="1.3.6.1.2.1.1.5"/>
  </Property>
</Property>
```

The preceding example results in the following query:

```
\Printer.System:Name
```

Note that because the `Value` construct is contained in a Property instance rather than an IndexedProperty instance, a trailing zero is automatically appended to the OID.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Value%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


