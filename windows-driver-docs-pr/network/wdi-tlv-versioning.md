---
title: WDI TLV versioning
description: To maintain backwards compatibility, both WDI and the miniport use the TLV stream as a versioning boundary.
ms.date: 03/02/2023
---

# WDI TLV versioning


To maintain backwards compatibility, both WDI and the miniport use the TLV stream as a versioning boundary. The producer of the TLV byte stream must always generate a backwards compatible TLV and not include any newly added fields. This is accomplished by adding a **PeerVersion** to the *Context* parameter. This field should be initialized by the caller to the *WdiVersion* received during initialization.

Here is the type definition of the *Context* parameter, which is passed into every Parse and Generate API.

```C++
typedef struct _TLV_CONTEXT
{
    ULONG_PTR   AllocationContext;
    ULONG       PeerVersion;
} TLV_CONTEXT, *PTLV_CONTEXT;
typedef const TLV_CONTEXT * PCTLV_CONTEXT;
```

**AllocationContext** is unmodified by the Parse and Generate APIs and continues to be passed through to the miniport-provided operator `new` callback. For more information, see [WDI TLV generator/parser memory interface](wdi-tlv-generator-parser-memory-interface.md).

If a WDI-based single-binary driver runs against an older version of WDI, the generator in the miniport uses the **PeerVersion** to generate the older byte stream. Conversely, the parser consumes the older byte stream based on the **PeerVersion** and converts it into the new data structures.

If a miniport driver does not use the TLV parser generator library and instead writes their own TLV parser and generator, and the desire is to have a single binary running only older OS versions (and thus old versions of WDI), they must include this capability also. Their parser must accept the TLV grammar produced by older WDI, and their generator must only generate TLVs according to the older grammar.

The XML has been augmented to support this versioning with two attributes allowed on containerRefs: *versionAdded* and *versionRemoved*. This is what drives the parser and generator to adjust the byte stream according to the peer version.

**Note**  The parser and generator assume that they are always linked with WDI\_VERSION\_LATEST. The miniport should always pass WDI\_VERSION\_LATEST for [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics)::**WdiVersion** when calling [**NdisMRegisterWdiMiniportDriver**](/windows-hardware/drivers/ddi/dot11wdi/nf-dot11wdi-ndismregisterwdiminiportdriver) rather than using a specific version, like WDI\_VERSION\_1\_0, as they will become out of date and cause problems with the TLV parser generator because the other end might send a byte stream that is unexpected.

 

 

