---
title: Bidirectional Request and Response Schemas
author: windows-driver-content
description: The Bidirectional Request and Response Schemas provide an XML-formatted set of queries and responses that can be used for bidirectional communication between applications and printers.
ms.assetid: C005D90D-DCDB-410C-BD6F-83111849547E
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bidirectional Request and Response Schemas


The Bidirectional Request and Response Schemas provide an XML-formatted set of queries and responses that can be used for bidirectional communication between applications and printers. Using these queries, applications can retrieve any printer configuration and status data that is stored in accordance with the [Bidirectional Communication Schema](bidirectional-communication-schema.md). They can also set any writable printer properties. You can use either the [**IBidiSpl2::SendRecvXMLStream**](https://msdn.microsoft.com/library/windows/hardware/dd144983) or the [**IBidiSpl2::SendRecvXMLString**](https://msdn.microsoft.com/library/windows/hardware/dd144984) function to communicate with the printer.

There are several request schemas and corresponding response schemas. The formal definition of each, and an example of each, are located in the following topics:

[Get Request and Response Schemas](get-request-and-response-schemas.md)

[EnumSchema Request and Response Schemas](enumschema-request-and-response-schemas.md)

[Set Request and Response Schemas](set-request-and-response-schemas.md)

[GetWithArgument Request and Response Schemas](getwithargument-request-and-response-schemas.md)

The root element of any request or response identifies its type. The &lt;EnumSchema&gt; request and response are used to retrieve a list of accessible printer properties. The &lt;Get&gt; and &lt;Set&gt; requests allow multiple queries. A &lt;Set&gt; "query" is simply an identification of the property to be set and the value to write to it.

Each &lt;Query&gt; has a schema= attribute that points to the property or property value that is being read/written. The values of these schema= attributes are paths in the tree of the Bidirectional Communications Schema.

For example, each &lt;Get&gt; response repeats the original set of queries and adds a result to each of them. Each &lt;Set&gt; response repeats the original set of of "queries," but provides nothing more for queries that succeed. If any query fails for either a &lt;Get&gt; or &lt;Set&gt; request, the result is an error message.

For more information about constructing requests, see [Constructing a Bidi Communications Schema Query](constructing-a-bidi-communication-schema-query.md).

For detailed information about the Bidirectional Communication Schema, see the [Bidirectional Communications Schema Hierarchy](bidirectional-communication-schema-hierarchy.md) and [Bidi Communications Schema Reference](https://msdn.microsoft.com/library/windows/hardware/ff545175) topics.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bidirectional%20Request%20and%20Response%20Schemas%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


