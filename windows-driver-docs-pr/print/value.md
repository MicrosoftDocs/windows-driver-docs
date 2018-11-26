---
title: Value (WSD)
description: The WSD Value construct allows you to extend the bidi communications schema with queries that retrieve data from a particular schema element.
ms.assetid: 8930e012-88ee-44ff-9abc-a15367f04ca3
keywords:
- Value construct
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Value (WSD)


The WSD `Value` construct allows you to extend the bidi communications schema with queries that retrieve data from a particular schema element in the Web service interface.

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
<td><p><strong>drvPrinterEvent</strong></p></td>
<td><p>(Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A <strong>TRUE</strong> value indicates that the port monitor sends notifications to the driver; <strong>FALSE</strong> indicates that the port monitor does not send notifications to the driver.</p></td>
</tr>
<tr class="even">
<td><p><strong>filter</strong></p></td>
<td><p>The XPath query that the WSD monitor will apply to the XML document that is specified by the query. See the discussion later in this topic.</p></td>
</tr>
<tr class="odd">
<td><p><strong>name</strong></p></td>
<td><p>The name of the schema value.</p></td>
</tr>
<tr class="even">
<td><p>query</p></td>
<td><p>The type of query that the WSD monitor will perform.</p></td>
</tr>
<tr class="odd">
<td><p><strong>type</strong></p></td>
<td><p>The type of data in the <code>Value</code> construct, a value in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545211" data-raw-source="[&lt;strong&gt;BIDI_TYPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545211)"><strong>BIDI_TYPE</strong></a> enumeration.</p></td>
</tr>
<tr class="even">
<td><p><strong>xmllang</strong></p></td>
<td><p>(Optional) A boolean value that, when <strong>TRUE</strong>, means that the associated <code>Value</code> construct should be treated as a localizable string value. This means that the XPath query defined above is expected to return a list of nodes differentiated by their xml:lang attributes. The WSD monitor will then search the list of values for the best locale match. The default value is <strong>FALSE</strong>.</p></td>
</tr>
</tbody>
</table>

 

The XPath language is implemented in Windows and provides a convenient way to specify elements in an XML file. See the XML Developer's Guide in the Windows SDK and [XPath Reference](http://go.microsoft.com/fwlink/p/?linkid=33165) for more information.

The **xmllang** attribute is used only when the type attribute of the `Value` construct is either "BIDI\_STRING" or "BIDI\_TEXT".

The `Value` construct is defined in WsdBidi.xsd.

### <a href="" id="example"></a> Example

In the following code example, the WSD monitor determines the size, as an integer value, of RAM memory.

```cpp
<Schema xmlns:nprt='http://schemas.microsoft.com/windows/2005/05/wdp/print'>
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

```cpp
\Printer.DeviceInfo:PrinterString
\Printer.Configuration.Memory:Size
```

 

 




