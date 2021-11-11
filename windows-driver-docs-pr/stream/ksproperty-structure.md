---
title: KSPROPERTY structure (ks.h)
description: The KSPROPERTY structure specifies a single kernel streaming property within a property set.
ms.date: 07/07/2021
ms.custom: contperf-fy22q1
ms.localizationpriority: medium
---

# KSPROPERTY structure

The **KSPROPERTY** structure specifies a single kernel streaming property within a property set.

The [**KSEVENT**](ksevent-structure.md), [**KSMETHOD**](ksmethod-structure.md), and **KSPROPERTY** structures are aliases for the [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) structure. As such, their definitions are identical.

## Syntax

```cpp
struct KSPROPERTY {
  GUID  Set;
  ULONG Id;
  ULONG Flags;
};
```

## Members

`Set`

Specifies a GUID that identifies a kernel streaming property set. For more information about property set GUIDs, see the **Remarks** section below.

`Id`

Specifies the member of the property set.

`Flags`

Specifies the request type. If you are writing a stream class minidriver, also see [**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) for class-specific flag information.

*Flags* should be one of the values listed in the following table. Some of the flags may be combined using a bitwise OR operation.

| Value | Description |
|--|--|
| KSPROPERTY_TYPE_GET | Retrieves the value of the specified property item. |
| KSPROPERTY_TYPE_SET | Sets the value of the specified property item. |
| KSPROPERTY_TYPE_SETSUPPORT | Queries if the driver supports this property set. |
| KSPROPERTY_TYPE_BASICSUPPORT | Queries the request types that the driver handles for this property item. Returns *KSPROPERTY_TYPE_GET* or *KSPROPERTY_TYPE_SET* or both. All property sets must support this flag. |
| KSPROPERTY_TYPE_DEFAULTVALUES | Queries the default values for the specified property item. Returns a structure of type [**KSPROPERTY_VALUES**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_values). |
| KSPROPERTY_TYPE_RELATIONS | Queries all properties with dependencies on the current setting of this property. Specifies that the property relations list is to be returned, or the amount of buffer room required by such a list if the return buffer is the size of a ULONG. Each element is on **FILE_QUAD_ALIGNMENT**, preceded by a **KSMULTIPLE_ITEM** structure. This is not valid when querying support of the property set in general. All property sets must support this flag. |
| KSPROPERTY_TYPE_SERIALIZESET | Serialize the property set, using the standard **KSPROPERTY_SERIALHDR** and **KSPROPERTY_SERIAL** structures. |
| KSPROPERTY_TYPE_UNSERIALIZESET | Unserialize the property set, using the standard **KSPROPERTY_SERIALHDR** and **KSPROPERTY_SERIAL** structures. |
| KSPROPERTY_TYPE_SERIALIZESIZE | Returns a ULONG specifying size of the property data when serialized as part of a *KSPROPERTY_TYPE_SERIALIZESET* request. A size of zero indicates that a property does not need to be serialized. |
| KSPROPERTY_TYPE_SERIALIZERAW | Specifies that the properties in this set should be serialized by the property set support handler, if one exists. If not, the call fails. The serialization format is private. This operation must be the inverse of *KSPROPERTY_TYPE_UNSERIALIZERAW*. |
| KSPROPERTY_TYPE_TOPOLOGY | Property passed is of type [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node), where NodeId indicates the numeric ID of the topology node. Do not set this flag on its own; instead, OR it with other flags in this table. |
| KSPROPERTY_TYPE_UNSERIALIZERAW | Specifies that the provided buffer contains a group of properties that belong to this set that should be unserialized by the property set support handler, if one exists. If not, the call fails. The serialization format is private. This operation must be the inverse of *KSPROPERTY_TYPE_SERIALIZERAW*. |

## Remarks

The size of the output buffer passed determines what data is returned from a KSPROPERTY_TYPE_BASICSUPPORT request. If the output buffer is the size of a ULONG, only the access flags are returned. If the output buffer is the size of the [**KSPROPERTY_DESCRIPTION**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_description) structure, the structure is filled with the access flags, the inclusive size of the entire values information, the property value type information, and the number of member lists that correspond to the structure.

For a KSPROPERTY_TYPE_RELATIONS request, data returned also depends on the size of the output buffer. If the output buffer size is zero, the size required to return the related properties is returned in **BytesReturned** with a warning status of STATUS_BUFFER_OVERFLOW. If the buffer is the size of a [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure, both the byte size and count of relations is returned. Otherwise, the buffer is expected to be long enough to return the KSMULTIPLE_ITEM structure and all related property identifiers, which is returned as a list of [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) structures.

*KSPROPERTY_TYPE_SERIALIZESET* and *KSPROPERTY_TYPE_UNSERIALIZESET* requests allow interaction with multiple properties with a single call from the client. If the kernel streaming handler is being used to process property requests, these are broken up into multiple calls by the [**KsPropertyHandler**](/windows-hardware/drivers/ddi/ks/nf-ks-kspropertyhandler) function. When using this handler, the property set definition controls which properties are to be serialized.

For serialization requests, the **SerializedSize** member of the relevant [**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) structure is checked for a nonzero value that indicates the size, in bytes, of the property. If the value of the SerializedSize member is 1, it is unknown and must be queried (all unknown properties begin with a KSMULTIPLE_ITEM structure that can be queried separately). To query for the total size a serialization would take, the client passes a zero length buffer in the call to **DeviceIoControl**. **BytesReturned** then returns the size, in bytes, that the buffer must be to serialize the set, and a warning status of STATUS_BUFFER_OVERFLOW. A buffer allocated that size can then be filled with the serialized data.

The format of the serialization buffer is a [**KSPROPERTY_SERIALHDR**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_serialhdr), followed by serialized properties. Each property that follows contains a header ([**KSPROPERTY_SERIAL**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_serial)), followed by the property data, with the start of each property on **FILE_LONG_ALIGNMENT**. Note that the serial header structure is defined to be on **FILE_LONG_ALIGNMENT**.

*KSPROPERTY_TYPE_SERIALIZERAW* and *KSPROPERTY_TYPE_UNSERIALIZERAW* are supported if a property item handler exists. The **KsPropertyHandler** function invokes the handler provided by the minidriver. The buffer size required for serialization can also be queried by passing a zero-length buffer to a serialize raw request. Because handlers are attached to property items rather than the property set, a specific item within the property set must be specified in the **Property** parameter. This handler may deal with multiple properties within the set.

Microsoft provides several system-defined property set GUIDs. Minidrivers specify one of these GUIDs in the **Set** member. Kernel streaming property sets typically begin with either a *KSPROPSETID* or a *PROPSETID* prefix. Kernel streaming property sets are defined in *ks.h*, *ksmedia.h*, *bdamedia.h*, and possibly other header files.

For more information about kernel streaming events, see [KS Properties, Events, and Methods](ks-properties--events--and-methods.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSEVENT**](ksevent-structure.md)

[**KSMETHOD**](ksmethod-structure.md)

[**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSMETHOD_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_item)

[**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node)

[**KSPROPERTY_DESCRIPTION**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_description)

[**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item)

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KsPropertyHandler**](/windows-hardware/drivers/ddi/ks/nf-ks-kspropertyhandler)

[**KSPROPERTY_SERIALHDR**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_serialhdr)

[**KSPROPERTY_SERIAL**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_serial)
