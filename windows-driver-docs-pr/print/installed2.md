---
title: Installed (TCP/IP)
description: The TCP/IP Installed construct contains the object ID (OID) of the MIB table's row and a list of lookup values.
keywords:
- Installed construct
ms.date: 06/26/2023
---

# Installed (TCP/IP)

The TCP/IP Installed construct contains the object ID (OID) of the MIB table's row and a list of lookup values. If any of the lookup values exists in the row, this algorithm returns **TRUE**. Most queries related to configuration of the printer should determine whether there is a particular value stored in the printer's MIB and then return a Boolean result. The Installed construct is defined in Tcpbidi.xsd.

| Attribute | Description |
|--|--|
| **deviceIndex** | (Optional) A flag that, when **TRUE**, means that the associated algorithm must include the device index in the specified OID; when **FALSE**, a trailing zero is appended to the OID. The default value is **FALSE**. For more information, see the note on the page for <a href="value.md" data-raw-source="[Value](value.md)">Value</a>. |
| **drvPrinterEvent** | (Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A **TRUE** value indicates that the port monitor sends notifications to the driver; **FALSE** indicates that the port monitor does not send notifications to the driver. |
| **name** | The name of the schema value. |
| **oid** | The row of the MIB table, as an OID. |
| **refreshInterval** | The value of the polling interval, in seconds. The default value is 600 seconds. |

## Code Example

In the following code example, the lookup algorithm retrieves the MIB table row from 1.3.6.1.2.1.43.13.4.1.9.&lt;**deviceIndex**&gt;. If this table row contains either 3 or 4, the query returns **TRUE**; otherwise the query returns **FALSE**.

```xml
<Property name="DuplexUnit">
  <Installed name="Installed" oid="1.3.6.1.2.1.43.13.4.1.9" deviceIndex="true">
    <Lookup value="3"/>
    <Lookup value="4"/>
  </Installed>
</Property>
```

The preceding example results in the following query:

```output
\Printer.Configuration.DuplexUnit:Installed
```
