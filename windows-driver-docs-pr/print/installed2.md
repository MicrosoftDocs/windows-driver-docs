---
title: Installed (TCP/IP)
author: windows-driver-content
description: The TCP/IP Installed construct contains the object ID (OID) of the MIB table's row and a list of lookup values.
ms.assetid: 4e14d8c1-7c66-4035-845d-f3f92dad8c4f
keywords:
- Installed construct
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>(Optional) A flag that, when <strong>TRUE</strong>, means that the associated algorithm must include the device index in the specified OID; when <strong>FALSE</strong>, a trailing zero is appended to the OID. The default value is <strong>FALSE</strong>. For more information, see the note on the page for [Value](value.md).</p></td>
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

```
<Property name="DuplexUnit">
  <Installed name="Installed" oid="1.3.6.1.2.1.43.13.4.1.9" deviceIndex="true">
    <Lookup value="3"/>
    <Lookup value="4"/>
  </Installed>
</Property>
```

The preceding example results in the following query:

```
\Printer.Configuration.DuplexUnit:Installed
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installed%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


