---
title: Types
description: Types
keywords: ["symbols, types", "types"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Types


## <span id="ddk_types_dbx"></span><span id="DDK_TYPES_DBX"></span>


Type information from a module's symbol file is identified by two pieces of information: a type ID and the base address of the module to which the type belongs. The following methods can be used to find a type ID:

-   [**GetTypeId**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-gettypeid) returns the type ID for a given type name.

-   [**GetSymbolTypeId**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymboltypeid) returns the type ID for the type of a symbol with the given name.

-   [**GetOffsetTypeId**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getoffsettypeid) returns the type ID for the symbol found at the given location.

The name and size of a type are returned by [**GetTypeName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-gettypename) and [**GetTypeSize**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-gettypesize), respectively.

The following convenience methods can be used for reading and writing typed data in the target's physical and virtual memory:

[**ReadTypedDataPhysical**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-readtypeddataphysical)

[**WriteTypedDataPhysical**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-writetypeddataphysical)

[**ReadTypedDataVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-readtypeddatavirtual)

[**WriteTypedDataVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-writetypeddatavirtual)

### <span id="printing_typed_data"></span><span id="PRINTING_TYPED_DATA"></span>Printing Typed Data

To format typed data and send it to the output callbacks, use [*OutputTypedDataPhysical*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-outputtypeddataphysical) and [*OutputTypedDataVirtual*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-outputtypeddatavirtual) for data in the target's physical and virtual memory respectively.

The type options described in [**DEBUG\_TYPEOPTS\_XXX**](debug-typeopts-xxx.md) affect how the engine formats typed data before sending it to the output callbacks.

The type options may be turned on by using [**AddTypeOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-addtypeoptions), and turned off by using [**RemoveTypeOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-removetypeoptions).

[**GetTypeOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-gettypeoptions) returns the current type options. To set all the type options at once, use [**SetTypeOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-settypeoptions).

### <span id="interpreting_raw_data_using_type_information"></span><span id="INTERPRETING_RAW_DATA_USING_TYPE_INFORMATION"></span>Interpreting Raw Data Using Type Information

The debugger engine API supports interpreting typed data. This provides a way to walk object hierarchies on the target, including finding members of structures, dereferencing pointers, and locating array elements.

Typed data is described by instances of the [**DEBUG\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_debug_typed_data) structure and represents regions of memory on the target cast to a particular type. The [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)**Request** operation is used to manipulate these instances. They can be initialized to the result of expressions or by casting regions of memory to a specified type. For a list of all the sub-operations that the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI **Request** operation supports, see [**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop).

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details on output callbacks, see [Input and Output](using-input-and-output.md).

 

