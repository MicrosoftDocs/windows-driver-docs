---
title: Callout Driver Programming Considerations
description: Callout Driver Programming Considerations
ms.assetid: e470202a-bc3b-41ac-8156-8aac8cd976cd
keywords:
- Windows Filtering Platform callout drivers WDK , programming considerations
- callout drivers WDK Windows Filtering Platform , programming considerations
- ALE flow established filtering layers WDK Windows Filtering Platform
- kernel-mode callout drivers WDK Windows Filtering Platform
- user-mode callout drivers WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Callout Driver Programming Considerations


Consider the following topics when you program a Windows Filtering Platform callout driver.

### <a href="" id="user-mode-vs--kernel-mode"></a>User Mode vs. Kernel Mode

If the desired filtering can be done by using the standard filtering functionality that is built in to the Windows Filtering Platform, independent software vendors (ISVs) should write user-mode management applications to configure the filter engine instead of writing kernel-mode callout drivers. A kernel-mode callout driver should only be written when you must process the network data in ways that cannot be handled by the standard, built-in filtering functionality. For information about how to write a user-mode Windows Filtering Platform management application, see the [Windows Filtering Platform](http://go.microsoft.com/fwlink/p/?linkid=90220) documentation in the Microsoft Windows SDK.

### Choice of Filtering Layer

A callout driver should filter the network data at the highest possible filtering layer in the network stack. For example, if the desired filtering task can be handled at the stream layer, it should not be implemented at the network layer. For more information about recommendations of the filtering layers your driver should use to guarantee compatibility with IPsec in Windows, see [Developing IPsec-Compatible Callout Drivers](developing-ipsec-compatible-callout-drivers.md).

### <a href="" id="blocking-at-the-application-layer-enforcement--ale--flow-established-l"></a>Blocking at the Application Layer Enforcement (ALE) Flow Established Layers

Usually, if a callout has been added to the filter engine at one of the *ALE flow established* filtering layers (FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4 or FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V6), its [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function should never return FWP\_ACTION\_BLOCK for the action. A decision to authorize or reject a connection should not be made at one of the ALE flow established filtering layers. Such a decision should always be made at one of the other ALE filtering layers.

The only valid reason for such a [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function to return FWP\_ACTION\_BLOCK for the action is if an error occurs that could pose a potential security risk if the established connection is not ended. In this case, returning FWP\_ACTION\_BLOCK for the action closes the connection to prevent the potential security risk from being exploited.

### Callout Function Execution Time

Because the filter engine typically calls a callout's callout functions at IRQL = DISPATCH\_LEVEL, make sure that these functions complete their execution as quickly as possible to keep the system running efficiently. Extended execution at IRQL = DISPATCH\_LEVEL can adversely affect the overall performance of the system.

### Injecting Into the Receive Data Path

Callouts should recalculate IP checksums before they call [packet injection functions](packet-injection-functions.md) that inject into the receive data path because the checksum in the original packet might not be correct when the packet is reassembled from IP packet fragments. There is no reliable mechanism that indicates whether a net buffer list is reassembled from fragments.

### Inline Injection of TCP Packet from Transport Layers

Because of the TCP stack's locking behavior, a callout at the transport layer cannot inject a new or cloned TCP packet from the [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function. If inline injection is desired, the callout must queue a DPC to perform the injection.

### Outgoing IP Header Alignment

The MDL that describes the IP header in a net buffer list ([**NET\_BUFFER\_CURRENT\_MDL**](https://msdn.microsoft.com/library/windows/hardware/ff568379)([**NET\_BUFFER\_LIST\_FIRST\_NB**](https://msdn.microsoft.com/library/windows/hardware/ff568394)(*netBufferList*))) must be pointer-aligned when one of the [packet injection functions](packet-injection-functions.md) is used to inject packet data into an outgoing path. Because an incoming packet's IP header MDL may be pointer-aligned, a callout must rebuild the IP header (if not already aligned) when injecting an incoming packet into an outgoing path.

## Related topics


[Windows Filtering Platform Callout Drivers](windows-filtering-platform-callout-drivers2.md)

 

 






