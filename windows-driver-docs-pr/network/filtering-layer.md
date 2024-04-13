---
title: Filtering Layer
description: Filtering Layer
keywords:
- filtering layer WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# Filtering Layer


A *filtering layer* is a point in the TCP/IP network stack where network data is passed to the [filter engine](filter-engine.md) for matching against the current set of filters. Each filtering layer in the network stack is identified by a unique [filtering layer identifier](management-filtering-layer-identifiers.md).

When a [filter](filter.md) is added to the filter engine, it is added at a designated filtering layer where it will filter the network data. Specific [data fields](./data-field-identifiers.md) are made available at each filtering layer for processing by the filters that have been added to the filter engine at that layer. If the filter engine passes the network data to a [callout](callout.md) for additional processing, it includes these data fields and any [metadata](metadata-field-identifiers.md) that is available at that filtering layer.

[Run-time Filtering Layer Identifiers](./run-time-filtering-layer-identifiers.md) (FWPS\_*XXX*) are used by kernel-mode callout drivers. [Management Filtering Layer Identifiers](./management-filtering-layer-identifiers.md) (FWPM\_*XXX*) are used by **Fwpm<em>Xxx</em>** functions that interact with the Base Filtering Engine (BFE) from either user mode or kernel mode (for example, [**FwpmFilterAdd0**](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfilteradd0)).

The FWPS data types are smaller than their FWPM counterparts: the FWPM filtering layer identifiers are GUIDs (128 bits), whereas the FWPS filtering layer identifiers are [**LUIDs**](/windows-hardware/drivers/ddi/igpupvdev/ns-igpupvdev-_luid)(64 bits). The smaller size for FWPS data types improves system performance because integer comparisons are faster than GUID comparisons for real-time traffic, and the kernel memory handles FWPS types more efficiently.

 

