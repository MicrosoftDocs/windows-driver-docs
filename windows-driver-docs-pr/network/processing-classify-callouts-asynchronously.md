---
title: Processing Classify Callouts Asynchronously
description: Processing Classify Callouts Asynchronously
ms.assetid: 1026f917-7b21-4b01-8cfd-4d14e92106fe
keywords:
- asynchronous processing of WFP classify callouts WDK Windows Filtering Platform
- Windows Filtering Platform Callout Drivers WDK , asynchronous processing of classify callouts
- pending WFP classify callouts WDK Windows Filtering Platform
- classify callouts WDK Windows Filtering Platform , asynchronous processing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Classify Callouts Asynchronously


A WFP callout driver can authorize or deny a network operation, or admit or discard a network packet, by returning the action types **FWP\_ACTION\_PERMIT**, **FWP\_ACTION\_CONTINUE**, or **FWP\_ACTION\_BLOCK** from the [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function. Frequently a callout driver cannot return an inspection decision from its *classifyFn* function until the indicated information, such as classifiable fields, metadata, or packets, can be forwarded for processing to another component, such as a user-mode application. In these cases a decision may have to be made asynchronously at some later time.

### General Rules for Asynchronous Processing

WFP supports asynchronous processing of the *classifyFn* callout function. However, the mechanism for doing this differs according to the different layers.

<a href="" id="asynchronous-ale-classify-------"></a>**Asynchronous ALE Classify**   
A callout driver must call the [**FwpsPendOperation0**](https://msdn.microsoft.com/library/windows/hardware/ff551199) function from *classifyFn*. The asynchronous operation must be completed with a call to the [**FwpsCompleteOperation0**](https://msdn.microsoft.com/library/windows/hardware/ff551152) function.

<a href="" id="asynchronous-packet-classify-------"></a>**Asynchronous Packet Classify**   
A callout driver should return **FWP\_ACTION\_BLOCK** from the *classifyFn* function, with the **FWPS\_CLASSIFY\_OUT\_FLAG\_ABSORB** flag set. Network packets must be referenced or cloned. The asynchronous operation is completed by either reinjecting the cloned or modified packet or by silently discarding the packet.

<a href="" id="asynchronous-ale-classify-that-includes-packets-------"></a>**Asynchronous ALE Classify That Includes Packets**   
A combination of the previous two procedures is used: the classify operation is pended and the packet is referenced or cloned, and at some time later the call to *classifyFn* is completed and the cloned packet is reinjected or discarded.

### Special Cases and Considerations

<a href="" id="ale-connect-vs--receive-accept-layers-------"></a>**ALE Connect vs. Receive/Accept Layers**   
When **FwpsCompleteOperation0** is called to complete a pended classify operation at an ALE connect layer (**FWPS\_LAYER\_ALE\_AUTH\_CONNECT\_V4** or **FWPS\_LAYER\_ALE\_AUTH\_CONNECT\_V6**), an ALE reauthorization classify operation is triggered at the respective ALE connect layer. The callout driver should return an inspection decision from this reauthorization classify operation. You can detect an ALE reauthorization classify operation by checking whether the **FWP\_CONDITION\_FLAG\_IS\_REAUTHORIZE** flag is set.

The callout driver must maintain a unique state for each pended ALE\_AUTH\_CONNECT classify operation in such a way that the inspection decision for each classify operation can be looked up during a **FwpsCompleteOperation0**-triggered reauthorization. If packets are referenced or cloned during a pended ALE\_AUTH\_CONNECT classify operation (for example, for non-TCP connections), they can be reinjected after reauthorization occurs.

When **FwpsCompleteOperation0** is called during with a classify operation at an ALE receive/accept layer (**FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4** or **FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V6**), **FwpsCompleteOperation0** does not trigger an ALE reauthorization. Instead a new call to *classifyFn* is made again when the cloned packet is reinjected incoming if the modification was not significant enough to bypass the filter. Permitting the self-injected clone from the ALE\_RECV\_ACCEPT layer effectively authorizes the incoming connection. If the incoming connection is not to be allowed, discard the incoming packet after it calls **FwpsCompleteOperation0**.

<a href="" id="ale-reauthorization-------"></a>**ALE Reauthorization**   
A callout driver can be reclassified at an ALE connect or receive/accept layer for events such as a policy change (for example, adding or removing a filter at the layer), detecting a new arrival interface, and re-keying a connection by using IPsec. Such a reauthorization cannot be pended by calling **FwpsCompleteOperation0**, and it is not necessary to do so. A callout driver should use the rules listed previously to process packets that are indicated during reauthorization.

Be aware that both incoming and outgoing packet can be reauthorized at ALE\_AUTH\_CONNECT or ALE\_RECV\_ACCEPT layers. For example, an incoming packet can be reauthorized at the ALE\_AUTH\_CONNECT layer. A callout driver must not assume that the direction of the packet is the same as the direction of the connection.

<a href="" id="ale-flow-established-layers-------"></a>**ALE\_FLOW\_ESTABLISHED Layers**   
Asynchronous processing is not supported at these layers (**FWPS\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4** or **FWPS\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V6**).

<a href="" id="inbound-transport-layers-------"></a>**INBOUND\_TRANSPORT Layers**   
A callout driver must not perform asynchronous processing of packets that require ALE classify processing at an incoming (inbound) transport layer (**FWPS\_LAYER\_INBOUND\_TRANSPORT\_V4** or **FWPS\_LAYER\_INBOUND\_TRANSPORT\_V6**). Doing this can interfere with flow creation. When WFP calls the *classifyFn* callout function at an incoming transport layer, it sets the **FWPS\_METADATA\_FIELD\_ALE\_CLASSIFY\_REQUIRED** flag for those packets that require ALE classify processing. A callout driver should permit such packets from an INBOUND\_TRANSPORT layer and should defer processing them until they reach an ALE\_RECV\_ACCEPT layer.

<a href="" id="stream-layers-------"></a>**STREAM Layers**   
At a stream layer (**FWPS\_LAYER\_STREAM\_V4** or **FWPS\_LAYER\_STREAM\_V6**), TCP data segments are indicated instead of an IP or TCP header. The stream layer is also where a chain of net buffer lists can be indicated in one call to the *classifyFn* callout function. WFP makes available specialized clone and injection functions, [**FwpsCloneStreamData0**](https://msdn.microsoft.com/library/windows/hardware/ff551149) and [**FwpsStreamInjectAsync0**](https://msdn.microsoft.com/library/windows/hardware/ff551213), for stream layer callouts to use.

Because of the ordered delivery nature of stream layer data, a callout driver must continue to clone and absorb data as long any stream data is still pending. Mixing asynchronous and synchronous operations for a given stream flow can result in undefined behavior.

 

 





