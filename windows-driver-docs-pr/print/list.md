---
title: List
description: List
ms.assetid: 4cf1c1ea-f890-4f9d-96ea-b79790f6bc60
keywords:
- List construct
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

The XPath language, implemented in Windows beginning with Microsoft XML (MSXML) 2.6, provides a convenient way to specify elements in an XML file. See the XML Developer's Guide in the Windows SDK and [XPath Reference](http://go.microsoft.com/fwlink/p/?linkid=33165) for more information.

The `List` construct is defined in WsdBidi.xsd.

### Code Example

In the following code example, a comma-separated list is composed that contains the allowable number of page images per sheet for N-up printing, for instance "1,2,4".

```cpp
<Property name='Layout'>
  <Property name='NumberUp'>
    <Property name='PagesPerSheet'>
      <List name='Supported
        query='wprt:PrinterCapabilities'
        filter='wprt:PrinterCapabilites/wprt:JobValues/wprt:DocumentProcessing/wprt:NumberUp/wprt:NUpPagesPerSheet/wprt:AllowedValue'/>
    </Property>
  </Property>
</Property>
```

The preceding example results in the following query:

```cpp
\Printer.Layout.NumberUp.PagesPerSheet:Supported
```

 

 




