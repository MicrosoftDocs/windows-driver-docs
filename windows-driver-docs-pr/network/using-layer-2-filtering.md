---
title: Using Layer 2 Filtering
description: Using Layer 2 Filtering
ms.assetid: 679E6DE2-4EFB-44F6-936D-2BF611BC9726
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Layer 2 Filtering

Layer 2 filtering is supported in Windows 8 and later versions of Windows.

This WFP feature allows filtering on fields of the layer 2 MAC header. These layers are invoked on a per-packet basis for all packets that are sent or received by the host machine. The layers are invoked prior to packet reassembly on the inbound path and after packet fragmentation on the outbound path. These layers are accessed from an NDIS lightweight filter (LWF) driver.

> [!NOTE]
> A callout should not inject packets at a layer if it does not already have a corresponding filter at that layer. The injection of the [NET\_BUFFER\_LIST](net-buffer-list-structure.md) structures should be coordinated with the filter addition and removal so that injection is only performed when the filter exists in the corresponding layer. In addition, providers should not remove filters that belong to other providers. 

This section includes the following topics:

-   [Injecting MAC Frames](#injecting-mac-frames)
-   [Classifying Chained Network Buffer Lists](#classifying-chained-network-buffer-lists)
-   [WFP Layer 2 Layers and Fields](#wfp-layer-2-layers-and-fields)

## Injecting MAC Frames

A callback driver calls the [**FwpsInjectMacReceiveAsync0**](https://msdn.microsoft.com/library/windows/hardware/hh439588) function to reinject a previously absorbed MAC frame (or a clone of the frame) back to the layer 2 inbound data path it was intercepted from, or to inject an invented MAC frame in the inbound data path.

A callback driver calls the [**FwpsInjectMacSendAsync0**](https://msdn.microsoft.com/library/windows/hardware/hh439593) function to reinject a previously absorbed MAC frame (or a clone of the frame) back to the layer 2 outbound data path it was intercepted from, or to inject an invented MAC frame in the outbound data path.

The *netBufferLists* parameter can be a [NET\_BUFFER\_LIST](net-buffer-list-structure.md) chain. However the completion function could be invoked multiple times each, completing a segment (or single NET\_BUFFER\_LIST) of the chain.

Injected frames could get classified again if the packets match the same filter as originally classified. Therefore, as with callouts at IP layers, layer 2 callouts must also protect against infinite packet inspection by calling [**FwpsQueryPacketInjectionState0**](https://msdn.microsoft.com/library/windows/hardware/ff551202).

Also, you must have callouts at the layer where you inject. Otherwise, your injected [NET\_BUFFER\_LIST](net-buffer-list-structure.md) will not be completed to your completion function, and the NET\_BUFFER\_LIST will go further up the stack. In this case, the behavior is undefined, because NDIS will try to pass the injected NET\_BUFFER\_LIST to the next component in the stack.

The [NET\_BUFFER\_LIST](net-buffer-list-structure.md)**Status** member contains the stack injection’s status result. The stack injection’s status result is the status that the stack puts in the NET\_BUFFER\_LIST after a WFP injection function returns **STATUS\_SUCCESS**. You should use the **NT\_SUCCESS** macro to check the stack injection's status in the **Status** member. If the **Status** value is **STATUS\_SUCCESS**, the injection succeeded with no further information. **Status** member values that are greater than **STATUS\_SUCCESS** mean that the injection succeeded, but there might be more information about the injection that should be considered. **Status** member values that are less than **STATUS\_SUCCESS** mean that the injection failed for the reason specified in the **Status** member.

## Classifying Chained Network Buffer Lists

By default, a callout driver can only classify network buffer lists individually. However, a callout driver can classify [NET\_BUFFER\_LIST](net-buffer-list-structure.md) chains for better performance, if it does both of the following:

-   Specifies the **FWP\_CALLOUT\_FLAG\_ALLOW\_L2\_BATCH\_CLASSIFY** flag in the **Flags** member of the [**FWPS\_CALLOUT2**](https://msdn.microsoft.com/library/windows/hardware/hh439700) structure.
-   Registers a [*classifyFn2*](https://msdn.microsoft.com/library/windows/hardware/hh439337) function that can classify [NET\_BUFFER\_LIST](net-buffer-list-structure.md) chains.

> [!WARNING]
> However, if a callout driver does set the **FWP_CALLOUT_FLAG_ALLOW_L2_BATCH_CLASSIFY** flag, it cannot use the following functions to modify NET_BUFFER_LISTs.
> 
> - [FwpsReferenceNetBufferList0](https://msdn.microsoft.com/library/windows/hardware/ff551206)
> - [FwpsDereferenceNetBufferList0](https://msdn.microsoft.com/library/windows/hardware/ff551159)
> - [FwpsAllocateCloneNetBufferList0](https://msdn.microsoft.com/library/windows/hardware/ff551134)
> - [FwpsFreeCloneNetBufferList0](https://msdn.microsoft.com/library/windows/hardware/ff551170)
>
> With this flag set, **FwpsAllocateCloneNetBufferList0** will always return an **INVALID_PARAMETER** error. This may unexpectedly cause a 3rd party callout driver to fail to manage the reference count of NET\_BUFFER\_LISTs, causing send and receive operations to stop.

## WFP Layer 2 Layers and Fields

Run-time Filtering Layer Identifiers for virtual switch filtering include:

**FWPS\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET**

**FWPS\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET**

**FWPS\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE**

**FWPS\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE**

Data Field Identifiers for virtual switch filtering include:

[**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_ETHERNET**](https://msdn.microsoft.com/library/windows/hardware/ff551291)

[**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_ETHERNET**](https://msdn.microsoft.com/library/windows/hardware/ff551334)

[**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_NATIVE**](https://msdn.microsoft.com/library/windows/hardware/hh439728)

[**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_NATIVE**](https://msdn.microsoft.com/library/windows/hardware/hh439757)

 

 





