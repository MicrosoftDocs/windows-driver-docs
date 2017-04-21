---
title: Installed (WSD)
author: windows-driver-content
description: The Web Services for Devices (WSD) Installed construct indicates whether a printer feature that matches a given set of criteria has been installed.
ms.assetid: f05add2a-d37e-4eb5-8408-dd5eeef4b13c
keywords:
- Installed construct
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

The XPath language, implemented in Windows beginning with Microsoft XML (MSXML) 2.6, provides a convenient way to specify elements in an XML file. See the XML Developer's Guide in the Windows SDK and [XPath Reference](http://go.microsoft.com/fwlink/p/?linkid=33165) in the MSDN Library.

The behavior of an Installed construct depends on the definition of its parent nodes. If an Installed construct is specified without the use of a Parameter, the schema will always exist when queried. If an Installed construct is specified with the use of a Parameter, the schema will exist only if the associated Parameter value is found in the current WSD device queries. The software that is making the queries must be able to handle the case where the Installed schema is not returned.

The Installed construct is defined in WsdBidi.xsd.

### Code Example

In the following code example, the filter lookup algorithm uses an XPath query to confirm that a hard disk is installed.

```
<Schema>
  <Property name=&#39;Printer&#39;>
    <Property name=&#39;Configuration&#39;>
      <Property name=&#39;HardDisk&#39;>
        <Installed name=&#39;Installed&#39;
            query=&#39;wprt:PrinterConfiguration&#39;
            filter=&#39;wprt:PrinterConfiguration/wprt:Storage/wprt:StorageEntry[wprt:Type="HardDisk"]&#39;/>
      </Property>
    </Property>
  </Property>
</Schema>
```

The preceding example results in the following query:

```
\Printer.Configuration.HardDisk:Installed
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installed%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


