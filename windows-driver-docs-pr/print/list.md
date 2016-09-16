---
title: List
author: windows-driver-content
description: List
MS-HAID:
- 'autocfg\_b09207bc-8ac6-4303-9a3c-ef15f5a64523.xml'
- 'print.list'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4cf1c1ea-f890-4f9d-96ea-b79790f6bc60
keywords: ["List construct"]
---

# List


The Web Services for Devices (WSD) `List` construct is a string type that composes a comma-separated list of values specified by the XPath filter query. The `List` construct is defined in WsdBidi.xsd.

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
<td><p>The XPath query that the WSD monitor applies to the XML document that is specified by the query. See the discussion later in this topic.</p></td>
</tr>
<tr class="odd">
<td><p><strong>name</strong></p></td>
<td><p>The name of the schema value.</p></td>
</tr>
<tr class="even">
<td><p><strong>query</strong></p></td>
<td><p>The type of query that the WSD monitor performs.</p></td>
</tr>
</tbody>
</table>

 

The XPath language, implemented in Windows beginning with Microsoft XML (MSXML) 2.6, provides a convenient way to specify elements in an XML file. See the XML Developer's Guide in the Windows SDK and [XPath Reference](http://go.microsoft.com/fwlink/p/?linkid=33165) in the MSDN Library.

The `List` construct is defined in WsdBidi.xsd.

### Code Example

In the following code example, a comma-separated list is composed that contains the allowable number of page images per sheet for N-up printing, for instance "1,2,4".

```
<Property name=&#39;Layout&#39;>
  <Property name=&#39;NumberUp&#39;>
    <Property name=&#39;PagesPerSheet&#39;>
      <List name=&#39;Supported
        query=&#39;wprt:PrinterCapabilities&#39;
        filter=&#39;wprt:PrinterCapabilites/wprt:JobValues/wprt:DocumentProcessing/wprt:NumberUp/wprt:NUpPagesPerSheet/wprt:AllowedValue&#39;/>
    </Property>
  </Property>
</Property>
```

The preceding example results in the following query:

```
\Printer.Layout.NumberUp.PagesPerSheet:Supported
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20List%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


