---
title: Customizing the Printer Port Monitors
description: Customizing the Printer Port Monitors
ms.assetid: e5d4166a-2593-43fd-b476-c54642e2d099
keywords:
- in-box autoconfiguration support WDK printer , customizing printer port monitors
- bidi extension files WDK printer autoconfig
- in-box autoconfiguration support WDK printer , bidi extension files
- customizing printer port monitors WDK
- port monitors WDK print , customizing
- WinSNMP conversion to Bidi data type WDK printer
- bidirectional communication WDK print
- bidi communication WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customizing the Printer Port Monitors


You can define new schemas for print devices that have capabilities above and beyond the standard [bidi communications schema](bidirectional-communication-schema.md) by customizing the standard TCP/IP or Web Services for Devices (WSD) port monitors that are supplied with Windows Vista. You must create a bidi extension file, an XML file that defines new schemas specific to that driver. This extension file is installed when the driver is installed. When the TCP/IP or WSD port monitor identifies this extension file, the monitor loads the file and can then use the additional bidi schemas.

The schemas in a bidi extension file are a subset of the standard print schema. Such schemas must adhere to the structure of the Tcpbidi.xsd or WsdBidi.xsd files supplied with the WDK.

**Note**  If the [bidi communications schema](bidirectional-communication-schema.md) meets your requirements, you do not need to create a bidi extension file and therefore have no need to customize the print port monitors.

 

You should create a bidi extension file and associate it with a printer driver if any of the following conditions apply:

1.  The printer driver needs information from the printer that cannot be found in the standard print schema. To obtain this information, you must extend the supported schema with additional queries. Any other client that enumerates a supported schema for a specific port gets additional queries but usually cannot understand them.

2.  You plan to include queries from the standard print schema that are not supported in the standard TCP/IP or WSD port monitors because the queries need driver-specific information. In this case, you must extend the print schema. Typically, you should extend the parts of the print schema related to input and output bins for print media. You should also provide a mapping between the names for bins defined in the bidi schema and those in the printer's management information base (MIB).

3.  You intend to customize the way standard queries work, such as by setting a custom object identifier (OID) or changing the refresh interval. For example, the standard TCP/IP port monitor polls devices that do not support Web Services Eventing at a default interval of 600 seconds (10 minutes). You can change the polling interval by creating a bidi extension that sets the refreshInterval attribute in a [Value](value.md) construct associated with the device. (See the `Memory` property in the following code example.)

If the driver has no associated bidi extension file, the bidi communication support in the standard print schema cannot respond to queries that require driver-specific data (such as data related to input and output bins).

**Note**   Network routing compartments in Windows Vista allow well-trusted processes connect to different network interfaces (whether virtual or physical), while keeping the various interfaces isolated from one another. For example, Windows Vista uses these compartments to enforce VPN policies that do not allow simultaneous access to both the VPN and a user's local network and Internet. During printing, the spooler impersonates the user when opening a TCP printer port. Consequently, the spooler cannot print to a local network printer while a user is connected to a VPN.

 

### Structure of a Bidi Extension File

A bidi extension file is well-formed XML that must be valid according to the Tcpbidi.xsd or WsdBidi.xsd files supplied with the Microsoft Windows Driver Kit (WDK). Constructs defined in these .xsd files enable you to define new schemas.

The following is an incomplete example of a TCP/IP bidi extension file that shows its basic structure. The structure of a WSD bidi extension file is similar.

```cpp
<?xml version="1.0" encoding="US-ASCII"?>
<bidi:Schema xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Schema>
    <Property name="Printer">
      <Property name="Configuration">
        <Property name= "Memory">
          <Value name="Size" type="BIDI_INT" oid="1.3.6.1.2.1.25.2.2" refreshInterval="600" drvPrinterEvent="true" />
          .
          .
          .
        </Property>
      </Property>
    </Property>
  </Schema>
</bidi:Schema>
```

In the preceding code example, note that:

-   The Root element contains exactly one Schema element. The hierarchy of the schema begins with the Schema element.

-   The Schema element has Property elements as nodes and Value elements as leaves.

-   Each Value element defines a particular technique by which the data can be retrieved.

### Conversion of WinSNMP to Bidi Data Types

The correspondence between Simple Network Management Protocol (SNMP) types and bidi types is given in the [**BIDI\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff545211) enumeration topic.

The remainder of this section contains the following topics to help you create your own bidi schema extensions.

[TCP/IP Schema Extensions](tcp-ip-schema-extensions.md)

[WSD Schema Extensions](wsd-schema-extensions-for-driver-specific-queries.md)

 

 




