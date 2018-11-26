---
title: Print Schema keywords for 3D manufacturing
description: The Print Schema keywords for 3D manufacturing is a supplemental specification to the Print Schema Specification.
ms.assetid: DC54C326-31AE-43C9-AF0D-A3A64DAEF1F2
ms.date: 05/15/2018
ms.localizationpriority: medium
---

# Print Schema keywords for 3D manufacturing


The Print Schema keywords for 3D manufacturing is a supplemental specification to the [Print Schema Specification](http://download.microsoft.com/download/d/e/c/deca6e6b-3e81-48e7-b7ef-6d92a547d03c/print-schema-spec-2-0.zip). This specification requires understanding of the set of conventions defined in the Print Schema Specification, in particular Part 1 and Part 3 of that specification. This specification contains Print Schema keywords that are the 3D manufacturing analog of Part 2 of the Print Schema Specification. It describes the XML keywords used by developers of 3D manufacturing devices to define their device’s capabilities in the context of the Print Schema.

A primary goal of this specification is to ensure the interoperability of independently created software and hardware systems that produce or consume Print Schema content for 3D manufacturing devices. Typically, these software and hardware systems discover each other through the Windows print infrastructure.

Understanding this specification requires working knowledge of the Extensible Markup Language (XML) and XML Namespace specifications. Full understanding might also require domain knowledge of common terms and procedures within the 3D manufacturing sector, although every effort has been made to minimize such reliance.

The information contained in this specification is subject to change. Every effort has been made to ensure its accuracy at the time of publication.

## How this specification is organized


| Section                                                                      | Description                                                                                                |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [3D manufacturing keywords overview](3d-manufacturing-keywords-overview.md) | Provides basic overview, design, and usage information for the Print Schema keywords for 3D manufacturing. |
| [Device control keywords](device-control-keywords.md)                       | These keywords are used to provide control over the 3D manufacturing device.                               |
| [Material keywords](material-keywords.md)                                   | These keywords describe the raw material in the device used to create 3D objects.                          |
| [Output keywords](output-keywords.md)                                       | These keywords are used to describe the actual output processes for a given 3D manufacturing job.          |
| [Print schema glossary](print-schema-glossary.md)                           | Provides definitions for terms used in this specification.                                                 |
| [PrintCapabilities document example](example-printcapabilities-document.md) | Provides an example PrintCapabilities document.                                                            |
| [PrintTicket document example](example-printticket-document.md)             | Provides an example PrintTicket document.                                                                  |
| [Print schema references](print-schema-references.md)                       | Provides references to industry standards, specifications, and technical articles.                         |


## Document conventions


Except where otherwise noted, syntax descriptions are expressed in the ABNF format as defined in RFC 4234.

Glossary terms are formatted as *italics* type.

Syntax descriptions and code are formatted in `monospace` type.

## Language Notes


In this specification, the words that are used to define the significance of each requirement are written in uppercase. These words are used in accordance with their definitions in RFC 2119, and their respective meanings are reproduced below:

MUST. This word, or the adjective "REQUIRED," means that the item is an absolute requirement of the specification.

SHOULD. This word, or the adjective "RECOMMENDED," means that there may exist valid reasons in particular circumstances to ignore this item, but the full implications should be understood and the case carefully weighed before choosing a different course.

MAY. This word, or the adjective "OPTIONAL," means that this item is truly optional. For example, one implementation may choose to include the item because a particular marketplace or scenario requires it or because it enhances the product. Another implementation may omit the same item.

## Software conformance


Requirements in this document are expressed as format requirements rather than implementation requirements. See the Print Schema Specification for additional requirements demanded for producers and consumers of PrintTicket and PrintCapabilities documents generally.

## Implementation license agreement


See the terms of the SDK License Agreement for more information.






