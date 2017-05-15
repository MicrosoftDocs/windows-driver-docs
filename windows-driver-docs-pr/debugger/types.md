---
title: Types
description: Types
ms.assetid: 234f4f36-ccd3-426a-a361-33727e9ece5a
keywords: ["symbols, types", "types"]
---

# Types


## <span id="ddk_types_dbx"></span><span id="DDK_TYPES_DBX"></span>


Type information from a module's symbol file is identified by two pieces of information: a type ID and the base address of the module to which the type belongs. The following methods can be used to find a type ID:

-   [**GetTypeId**](https://msdn.microsoft.com/library/windows/hardware/ff549376) returns the type ID for a given type name.

-   [**GetSymbolTypeId**](https://msdn.microsoft.com/library/windows/hardware/ff549173) returns the type ID for the type of a symbol with the given name.

-   [**GetOffsetTypeId**](https://msdn.microsoft.com/library/windows/hardware/ff548062) returns the type ID for the symbol found at the given location.

The name and size of a type are returned by [**GetTypeName**](https://msdn.microsoft.com/library/windows/hardware/ff549408) and [**GetTypeSize**](https://msdn.microsoft.com/library/windows/hardware/ff549457), respectively.

The following convenience methods can be used for reading and writing typed data in the target's physical and virtual memory:

[**ReadTypedDataPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff554344)

[**WriteTypedDataPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff561463)

[**ReadTypedDataVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff554345)

[**WriteTypedDataVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff561466)

### <span id="printing_typed_data"></span><span id="PRINTING_TYPED_DATA"></span>Printing Typed Data

To format typed data and send it to the output callbacks, use [*OutputTypedDataPhysical*](https://msdn.microsoft.com/library/windows/hardware/ff553269) and [*OutputTypedDataVirtual*](https://msdn.microsoft.com/library/windows/hardware/ff553274) for data in the target's physical and virtual memory respectively.

The type options described in [**DEBUG\_TYPEOPTS\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541712) affect how the engine formats typed data before sending it to the output callbacks.

The type options may be turned on by using [**AddTypeOptions**](https://msdn.microsoft.com/library/windows/hardware/ff537949), and turned off by using [**RemoveTypeOptions**](https://msdn.microsoft.com/library/windows/hardware/ff554551).

[**GetTypeOptions**](https://msdn.microsoft.com/library/windows/hardware/ff549428) returns the current type options. To set all the type options at once, use [**SetTypeOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556874).

### <span id="interpreting_raw_data_using_type_information"></span><span id="INTERPRETING_RAW_DATA_USING_TYPE_INFORMATION"></span>Interpreting Raw Data Using Type Information

The debugger engine API supports interpreting typed data. This provides a way to walk object hierarchies on the target, including finding members of structures, dereferencing pointers, and locating array elements.

Typed data is described by instances of the [**DEBUG\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff541706) structure and represents regions of memory on the target cast to a particular type. The [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](https://msdn.microsoft.com/library/windows/hardware/ff541547)**Request** operation is used to manipulate these instances. They can be initialized to the result of expressions or by casting regions of memory to a specified type. For a list of all the sub-operations that the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI **Request** operation supports, see [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529).

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details on output callbacks, see [Input and Output](using-input-and-output.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Types%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




