---
title: Installed (WSD)
description: The Web Services for Devices (WSD) Installed construct indicates whether a printer feature that matches a given set of criteria has been installed.
ms.assetid: f05add2a-d37e-4eb5-8408-dd5eeef4b13c
keywords:
- Installed construct
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installed (WSD)


The Web Services for Devices (WSD) Installed construct indicates whether a printer feature that matches a given set of criteria has been installed. If an XPath filter obtains a valid XML result when applied to the given criteria, this algorithm returns **TRUE**. The Installed construct is defined in WsdBidi.xsd.

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
<td><p>The type of query that the WSD monitor will perform.</p></td>
</tr>
</tbody>
</table>

 

The XPath language, implemented in Windows beginning with Microsoft XML (MSXML) 2.6, provides a convenient way to specify elements in an XML file. See the XML Developer's Guide in the Windows SDK and [XPath Reference](http://go.microsoft.com/fwlink/p/?linkid=33165) for more information.

The behavior of an Installed construct depends on the definition of its parent nodes. If an Installed construct is specified without the use of a Parameter, the schema will always exist when queried. If an Installed construct is specified with the use of a Parameter, the schema will exist only if the associated Parameter value is found in the current WSD device queries. The software that is making the queries must be able to handle the case where the Installed schema is not returned.

The Installed construct is defined in WsdBidi.xsd.

### Code Example

In the following code example, the filter lookup algorithm uses an XPath query to confirm that a hard disk is installed.

```cpp
<Schema>
  <Property name='Printer'>
    <Property name='Configuration'>
      <Property name='HardDisk'>
        <Installed name='Installed'
            query='wprt:PrinterConfiguration'
            filter='wprt:PrinterConfiguration/wprt:Storage/wprt:StorageEntry[wprt:Type="HardDisk"]'/>
      </Property>
    </Property>
  </Property>
</Schema>
```

The preceding example results in the following query:

```cpp
\Printer.Configuration.HardDisk:Installed
```

 

 




