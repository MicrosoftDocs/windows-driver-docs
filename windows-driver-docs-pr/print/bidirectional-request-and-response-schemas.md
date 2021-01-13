---
title: Bidirectional Request and Response Schemas
description: The Bidirectional Request and Response Schemas provide an XML-formatted set of queries and responses that can be used for bidirectional communication between applications and printers.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bidirectional Request and Response Schemas


The Bidirectional Request and Response Schemas provide an XML-formatted set of queries and responses that can be used for bidirectional communication between applications and printers. Using these queries, applications can retrieve any printer configuration and status data that is stored in accordance with the [Bidirectional Communication Schema](bidirectional-communication-schema.md). They can also set any writable printer properties. You can use either the [**IBidiSpl2::SendRecvXMLStream**](/windows-hardware/drivers/ddi/bidispl/nf-bidispl-ibidispl2-sendrecvxmlstream) or the [**IBidiSpl2::SendRecvXMLString**](/windows-hardware/drivers/ddi/bidispl/nf-bidispl-ibidispl2-sendrecvxmlstring) function to communicate with the printer.

There are several request schemas and corresponding response schemas. The formal definition of each, and an example of each, are located in the following topics:

[Get Request and Response Schemas](get-request-and-response-schemas.md)

[EnumSchema Request and Response Schemas](enumschema-request-and-response-schemas.md)

[Set Request and Response Schemas](set-request-and-response-schemas.md)

[GetWithArgument Request and Response Schemas](getwithargument-request-and-response-schemas.md)

The root element of any request or response identifies its type. The &lt;EnumSchema&gt; request and response are used to retrieve a list of accessible printer properties. The &lt;Get&gt; and &lt;Set&gt; requests allow multiple queries. A &lt;Set&gt; "query" is simply an identification of the property to be set and the value to write to it.

Each &lt;Query&gt; has a schema= attribute that points to the property or property value that is being read/written. The values of these schema= attributes are paths in the tree of the Bidirectional Communications Schema.

For example, each &lt;Get&gt; response repeats the original set of queries and adds a result to each of them. Each &lt;Set&gt; response repeats the original set of "queries," but provides nothing more for queries that succeed. If any query fails for either a &lt;Get&gt; or &lt;Set&gt; request, the result is an error message.

For more information about constructing requests, see [Constructing a Bidi Communications Schema Query](constructing-a-bidi-communication-schema-query.md).

For detailed information about the Bidirectional Communication Schema, see the [Bidirectional Communications Schema Hierarchy](bidirectional-communication-schema-hierarchy.md) and [Bidi Communications Schema Reference](./bidi-communications-schema-reference.md) topics.

 

