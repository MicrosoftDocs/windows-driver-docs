---
title: Converter
author: windows-driver-content
description: Converter
ms.assetid: eadbbaf5-3fe3-484f-b3f1-3d543ddc817f
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Converter


The TCP/IP Converter construct enables you to extend the [bidi communications](bidirectional-communication.md) schema with queries that retrieve data from a particular MIB (SNMP Management Information Base) object and then convert the data to a string value that is based on a list of value pairs that are specified in Conversion elements. The Converter construct is defined in Tcpbidi.xsd.

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
<td><p>(Optional) A Boolean value that, when <strong>TRUE</strong>, means that the associated algorithm must include the device index in the specified OID; when this attribute <strong>FALSE</strong>, a trailing zero is appended to the OID. The default value is <strong>FALSE</strong>. For more information, see the note following this table.</p></td>
</tr>
<tr class="even">
<td><p><strong>drvPrinterEvent</strong></p></td>
<td><p>(Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A <strong>TRUE</strong> value indicates that the port monitor sends notifications to the driver; <strong>FALSE</strong> indicates that the port monitor does not send notifications to the driver.</p></td>
</tr>
<tr class="odd">
<td><p><strong>name</strong></p></td>
<td><p>A string value that represents the name of the schema element.</p></td>
</tr>
<tr class="even">
<td><p><strong>oid</strong></p></td>
<td><p>A string value that represents the address of the MIB object, as an object ID (OID).</p></td>
</tr>
<tr class="odd">
<td><p><strong>refreshInterval</strong></p></td>
<td><p>(Optional) An integer value of the polling interval, in seconds. The default value is 600 seconds.</p></td>
</tr>
<tr class="even">
<td><p><strong>useFirstIndex</strong></p></td>
<td><p>(Optional) A Boolean value that can be set to read the first entry in a MIB table. This attribute is used only when the Converter construct is within a Property instance.</p></td>
</tr>
</tbody>
</table>

 

**Note**   A network device that supports the SNMP protocol can be the host for different subdevices, such as Processor, Network, Printer, and Disk Storage. The MIB tables that are implemented in network printers have entries that are indexed by device indexes. To retrieve data from the MIB table (such as the name of an input bin), the query must have a device index that correctly identifies the subdevice. The standard TCP/IP port monitor allows the device index to be manually configured through the port configuration UI. A bidi extension with the **deviceIndex** attribute set to **TRUE** generates an OID with the appropriate device index that is obtained from the port configuration UI. In addition, if the Converter construct is contained in a Property instance and the **deviceIndex** attribute is missing or set to **FALSE**, the OID will have a zero index appended to its end.

 

The following MIB data types are supported by the conversion routines:

INTEGER

Integer32

Gauge32

Counter32

TimeTicks

Unsigned32

Counter64

Opaque

OCTET STRING

OBJECT IDENTIFIER

### <a href="" id="conversion-element"></a> Conversion Element

Each Converter construct will include one or more Conversion elements to define the mapping of values read from the MIB elements into Bidi schema values.

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
<td><p>mibValue</p></td>
<td><p>(Optional) A string value that represents one possible data value that could be read from the MIB.</p></td>
</tr>
<tr class="even">
<td><p>bidiValue</p></td>
<td><p>(Optional) A string value that represents the bidi value that is returned if the data matches the <strong>mibValue</strong> attribute for this Conversion element..</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="code-example"></a> Code Example

The following code example extends the bidi communications schema by adding new properties and Converter constructs.

```
<Property name="Printer">
  <Property name="Layout">
    <Property name="InputBins">
      <IndexedProperty name="Bin">
        <Converter name="BinType" oid="1.3.6.1.2.1.43.8.2.1.2" deviceIndex="true">
          <Conversion mibValue="2" bidiValue="Unknown"/>
          <Conversion mibValue="3" bidiValue="SheetFeedAutoRemoveableTray"/>
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
    <Property name="HostRescourceMIB">
      <Converter name="InterfaceName" oid="1.3.6.1.2.1.2.1">
      <Conversion mibValue="1" bidiValue="InterfaceOne"/>
    <Conversion mibValue="2" bidiValue="InterfaceTwo"/>
     </Converter>
  </Property>
 </Property
</Property>
```

The preceding example results in the following queries.

```
\Printer.Layout.InputBins.Bin###:BinType
\Printer.Layout.Orientation:CurrentValue
\Printer.Custom.HostResourceMIB:InterfaceName
```

The Converter construct for `BinType` is contained in an IndexedProperty instance, and, as a result, the current MIB table row entry is automatically appended to the OID.

Because the Converter construct for `CurrentValue `is contained in a Property instance and the **useFirstIndex** attribute is set to "true", a trailing "1" is automatically appended to the OID.

The Converter construct for `InterfaceName` is contained in a Property instance, so a trailing zero automatically being appended to the OID.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Converter%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


