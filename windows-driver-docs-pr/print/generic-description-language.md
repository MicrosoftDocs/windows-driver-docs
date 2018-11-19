---
title: Generic Description Language
description: Generic Description Language
ms.assetid: 818037fd-90bb-46dd-a2e3-239d57ed5fcf
keywords:
- printer configuration WDK , GDL files
- text files WDK GDL files
- Generic Description Language WDK
- GDL WDK
- GDL WDK , about
- generic printer description WDK Unidrv
- GPD WDK
- printer drivers WDK , Generic Description Language
- printer drivers WDK , converting data into XML
- converting data into XML WDK GDL
- transforming data into XML WDK GDL
- GDL WDK , parser
- GDL WDK , snapshots
- snapshots WDK GDL
- GDL WDK , directives
- directives WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Generic Description Language


The Generic Description Language (GDL) defines a syntax with which to express hierarchically structured data. GDL also enables manufacturers and consumers to cooperatively define a schema that can be used to standardize the way in which the data is expressed. This schema can be used to validate the structure and format of the data and to guide the transformation of the data into another format (such as XML).

Microsoft provides the [GDL parser](gdl-parser.md) and associated *parser filters*, which access and process data from a source data file and convert it to hierarchical data that the [GDL syntax](gdl-syntax.md) defines. GDL supports complex data sets, object-oriented schemas that define the structure and processing of this data, and a mechanism for easy extension by vendors.

GDL is designed as a superset of the Generic Printer Description ([GPD](introduction-to-gpd-files.md)) language, which is used to describe printer capabilities for Unidrv minidrivers.

GDL has the following main features:

-   GDL is backwards compatible with GPD legacy format.

-   GDL is arbitrarily extensible. That is, anyone can add custom attributes and constructs.

-   GDL uses templates to provide data structures.

-   GDL uses preprocessor directives and parameter-driven configuration to provide flexible linking and conditions.

-   GDL parses data input and returns an XML stream to the client.

When the data in a [GDL source file](gdl-source-files.md) is parsed by the [GDL parser](gdl-parser.md), the parser maintains a hierarchical data structure. The client accesses the parsed data structure indirectly through a [snapshot](gdl-snapshots.md). The *snapshot* is a representation of the data in a particular state. This state is specified through a [configuration](gdl-configurations.md). In the current implementation of the GDL parser, the snapshot is expressed as XML, and the data in the snapshot can be accessed by using XML tools.

In addition to data entries, the GDL parser recognizes keywords (which are called [directives](gdl-directives.md)). The directives include categories such as [preprocessors](gdl-source-file-preprocessor-directives.md), [macros](gdl-directives-for-macros.md), [namespaces](gdl-directives-for-namespaces.md), [templates](gdl-directives-for-templates.md), and [configurations](gdl-directives-for-configurations.md).

The following sections provide more information about GDL:

[GDL Architecture](gdl-architecture.md)

[GDL Programming Guide](gdl-programming-guide.md)

[GDL Reference](gdl-reference.md)

[GDL Examples](gdl-examples.md)

 

 




