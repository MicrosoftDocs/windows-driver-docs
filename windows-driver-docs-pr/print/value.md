---
title: Value
author: windows-driver-content
description: Value
ms.assetid: 8930e012-88ee-44ff-9abc-a15367f04ca3
keywords: ["Value construct"]
---

# Value


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
<td><p>The type of data in the <code>Value</code> construct, a value in the [<strong>BIDI_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545211) enumeration.</p></td>
</tr>
<tr class="even">
<td><p><strong>xmllang</strong></p></td>
<td><p>(Optional) A boolean value that, when <strong>TRUE</strong>, means that the associated <code>Value</code> construct should be treated as a localizable string value. This means that the XPath query defined above is expected to return a list of nodes differentiated by their xml:lang attributes. The WSD monitor will then search the list of values for the best locale match. The default value is <strong>FALSE</strong>.</p></td>
</tr>
</tbody>
</table>

 

The XPath language is implemented in Windows and provides a convenient way to specify elements in an XML file. See the XML Developer's Guide in the Windows SDK and [XPath Reference](http://go.microsoft.com/fwlink/p/?linkid=33165) in the MSDN Library.

The **xmllang** attribute is used only when the type attribute of the `Value` construct is either "BIDI\_STRING" or "BIDI\_TEXT".

The `Value` construct is defined in WsdBidi.xsd.

### <a href="" id="example"></a> Example

In the following code example, the WSD monitor determines the size, as an integer value, of RAM memory.

```
<Schema xmlns:nprt=&#39;http://schemas.microsoft.com/windows/2005/05/wdp/print&#39;>
  <Property name=&#39;Printer&#39;>
    <Property name=&#39;DeviceInfo&#39;>
      <Value name=&#39;PrinterString&#39; 
 query=&#39;nprt:PrinterDescription&#39;
 filter=&#39;nprt:PrinterDescription/nprt:PrinterName&#39; 
 type=&#39;BIDI_STRING&#39; 
 xmllang=&#39;true&#39;/>
    </Property>
    <Property name=&#39;Configuration&#39;>
      <Property name=&#39;Memory&#39;>
        <Value name=&#39;Size&#39;
          query=&#39;wprt:PrinterConfiguration&#39;
          filter=&#39;wprt:PrinterConfiguration/wprt:Storage/wprt:StorageEntry[wprt:Type="RAM"]/wprt:Size&#39;
          type=&#39;BIDI_INT&#39;/>
      </Property>
    </Property>
   </Property>
</Schema>
```

The preceding example results in the following queries:

```
\Printer.DeviceInfo:PrinterString
\Printer.Configuration.Memory:Size
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Value%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


