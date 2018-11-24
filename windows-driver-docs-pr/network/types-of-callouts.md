---
title: Types of Callouts
description: Types of Callouts
ms.assetid: d9539403-7657-4e95-8791-309673d1207d
keywords:
- pending packets WDK Windows Filtering Platform
- callout types WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Types of Callouts


The following types of callouts can be used with WFP:

<a href="" id="inline-inspection-callout-------"></a>**Inline Inspection Callout**   
This type of callout always returns **FWP\_ACTION\_CONTINUE** from the [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) function and does not modify the network traffic in any way. A callout that collects network statistics is an example of this type of callout.

For this type of callout, the filter action type (specified by the **Type** member of the [**FWPS\_ACTION0**](https://msdn.microsoft.com/library/windows/hardware/ff551215) structure) should be set to **FWP\_ACTION\_CALLOUT\_INSPECTION**.

<a href="" id="out-of-band-inspection-callout-------"></a>**Out-of-band Inspection Callout**   
This type of callout does not modify network traffic. Instead, it defers any inspection to be done outside the *classifyFn* function by "pending" the indicated data and then reinjecting the pended data back into the TCP/IP stack with one of the [packet injection functions](packet-injection-functions.md). Pending is implemented by first cloning the indicated data, followed by returning **FWP\_ACTION\_BLOCK** from the *classifyFn* function that has the **FWPS\_CLASSIFY\_OUT\_FLAG\_ABSORB** bit set.

<a href="" id="inline-modification-callout-------"></a>**Inline Modification Callout**   
This type of callout modifies network traffic by first making a clone of the indicated data, then modifying the clone, and finally injecting the modified clone back into the TCP/IP stack from the *classifyFn* function. This type of callout also returns **FWP\_ACTION\_BLOCK** from the *classifyFn* function that has the **FWPS\_CLASSIFY\_OUT\_FLAG\_ABSORB** bit set.

The filter action type for this type of callout should be set to **FWP\_ACTION\_CALLOUT\_TERMINATING**.

<a href="" id="out-of-band-modification-callout-------"></a>**Out-of-band Modification Callout**   
This type of callout first references the indicated packet by using the [**FwpsReferenceNetBufferList0**](https://msdn.microsoft.com/library/windows/hardware/ff551206) function that has the *intentToModify* parameter set to **TRUE**. The callout then returns **FWP\_ACTION\_BLOCK** with the **FWPS\_CLASSIFY\_OUT\_FLAG\_ABSORB** bit set from the *classifyFn* function. When the packet is ready to be modified outside *classifyFn*, the callout clones the referenced packet (as soon as it is cloned, the original packet can then be dereferenced). The callout then modifies the clone and injects the modified packet back into the TCP/IP stack.

The filter action type for this type of callout should be set to **FWP\_ACTION\_CALLOUT\_TERMINATING**.

<a href="" id="redirection-callout"></a>**Redirection Callout**  
For more information about this type of callout, see [Using Bind or Connect Redirection](using-bind-or-connect-redirection.md).

There are two types of redirection callouts:

-   A bind redirection callout allows the callout driver to modify the local address and local port of a socket.
-   A connect redirection callout allows the callout driver to modify the remote address and remote port of a connection.

The filter action type for this type of callout should be set to **FWP\_ACTION\_PERMIT**.

For more information about **FWPS\_CLASSIFY\_OUT\_FLAG\_ABSORB**, see [**FWPS\_CLASSIFY\_OUT0**](https://msdn.microsoft.com/library/windows/hardware/ff551229). This flag is not valid at any WFP discard layer. Returning **FWP\_ACTION\_BLOCK** with the **FWPS\_CLASSIFY\_OUT\_FLAG\_ABSORB** flag set from the *classifyFn* function causes the packet to be silently discarded, in such a way that the packet will not hit any of the WFP discard layers, nor will it cause audit events to be generated.

Although cloned net buffer lists can be modified, for example, by adding or removing net buffers or MDLs, or both, callouts must undo such modifications before they call the [**FwpsFreeCloneNetBufferList0**](https://msdn.microsoft.com/library/windows/hardware/ff551170) function.

To coexist with other callouts that perform packet inspection, packet modification, or connection redirection, before a packet is pended with the reference/clone-drop-reinject mechanism, a callout must "hard"-drop the original packet by clearing the **FWPS\_RIGHT\_ACTION\_WRITE** flag in the **rights** member of the [**FWPS\_CLASSIFY\_OUT0**](https://msdn.microsoft.com/library/windows/hardware/ff551229) structure returned by the *classifyFn* function. If the **FWPS\_RIGHT\_ACTION\_WRITE** flag is set when *classifyFn* is called (which means that the packet could be pended and later reinjected or modified), the callout must not pend the indication and should not change the current action type; and it must wait for a higher-weight callout to inject the clone that might be modified.

The **FWPS\_RIGHT\_ACTION\_WRITE** flag should be set whenever a callout pends a classification. Your callout driver should test for the **FWPS\_RIGHT\_ACTION\_WRITE** flag to check the rights for your callout to return an action. If this flag is not set, your callout can still return a **FWP\_ACTION\_BLOCK** action in order to veto a **FWP\_ACTION\_PERMIT** action that was returned by a previous callout. In the example shown in [Using a Callout for Deep Inspection](using-a-callout-for-deep-inspection.md), the function just exits if the flag is not set.

The [**FwpsPendOperation0**](https://msdn.microsoft.com/library/windows/hardware/ff551199) function is used to pend packets that originate from the **FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_**<em>XXX</em>, **FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_**<em>XXX</em>, or **FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_**<em>XXX</em> [management filtering layers](https://msdn.microsoft.com/library/windows/hardware/ff557101).

The [**FwpsPendClassify0**](https://msdn.microsoft.com/library/windows/hardware/ff551197) function is used to pend packets that originate from the following [run-time filtering layers](https://msdn.microsoft.com/library/windows/hardware/ff570731):

FWPS\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V4
FWPS\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V6
FWPS\_LAYER\_ALE\_CONNECT\_REDIRECT\_V4
FWPS\_LAYER\_ALE\_CONNECT\_REDIRECT\_V6
FWPS\_LAYER\_ALE\_BIND\_REDIRECT\_V4
FWPS\_LAYER\_ALE\_BIND\_REDIRECT\_V6
 

 





