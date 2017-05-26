---
title: Generic Description Language
author: windows-driver-content
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Generic%20Description%20Language%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


