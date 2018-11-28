---
title: Installed (TCP/IP)
description: The TCP/IP Installed construct contains the object ID (OID) of the MIB table's row and a list of lookup values.
ms.assetid: 4e14d8c1-7c66-4035-845d-f3f92dad8c4f
keywords:
- Installed construct
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installed (TCP/IP)


The TCP/IP Installed construct contains the object ID (OID) of the MIB table's row and a list of lookup values. If any of the lookup values exists in the row, this algorithm returns **TRUE**. Most queries related to configuration of the printer should determine whether there is a particular value stored in the printer's MIB and then return a Boolean result. The Installed construct is defined in Tcpbidi.xsd.

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
<td><p>(Optional) A flag that, when <strong>TRUE</strong>, means that the associated algorithm must include the device index in the specified OID; when <strong>FALSE</strong>, a trailing zero is appended to the OID. The default value is <strong>FALSE</strong>. For more information, see the note on the page for <a href="value.md" data-raw-source="[Value](value.md)">Value</a>.</p></td>
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
<td><p>The row of the MIB table, as an OID.</p></td>
</tr>
<tr class="odd">
<td><p><strong>refreshInterval</strong></p></td>
<td><p>The value of the polling interval, in seconds. The default value is 600 seconds.</p></td>
</tr>
</tbody>
</table>

 

### Code Example

In the following code example, the lookup algorithm retrieves the MIB table row from 1.3.6.1.2.1.43.13.4.1.9.&lt;**deviceIndex**&gt;. If this table row contains either 3 or 4, the query returns **TRUE**; otherwise the query returns **FALSE**.

```cpp
<Property name="DuplexUnit">
  <Installed name="Installed" oid="1.3.6.1.2.1.43.13.4.1.9" deviceIndex="true">
    <Lookup value="3"/>
    <Lookup value="4"/>
  </Installed>
</Property>
```

The preceding example results in the following query:

```cpp
\Printer.Configuration.DuplexUnit:Installed
```

 

 




