---
title: Summary of changes to port a protocol driver to NDIS 6.0
description: Summary of Changes Required to Port a Protocol Driver to NDIS 6.0
ms.assetid: a2d17b63-81fc-44c9-a437-cd7c9f04be5b
keywords:
- porting protocol drivers WDK networking , required changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port a Protocol Driver to NDIS 6.0





This topic provides a summary of the changes that are required to port an NDIS 5.x protocol driver to NDIS 6.0. Porting earlier drivers is similar to porting NDIS 5.x drivers. To run in the NDIS 6.0 environment, NDIS 5.*x* protocol drivers must be modified as follows:

<a href="" id="build-environment"></a>**Build Environment**  
Replace the preprocessor definition NDIS51 with NDIS60.

<a href="" id="driver-initialization"></a>**Driver Initialization**  
-   Set the NDIS version to 6.0 in the **MajorNdisVersion** and **MinorNdisVersion** members of the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure (formerly NDIS\_PROTOCOL\_CHARACTERISTICS) that is passed to the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function.

-   Set the protocol driver version in the **MajorDriverVersion** and **MinorDriverVersion** members of the NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS structure to an appropriate driver-specific value.

-   Define new entry points and replace obsolete entry points in the NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS structure. For example, the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function replaces the [**ProtocolBindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff562465) function.

-   If the protocol driver uses optional handlers, add the entry point for the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function to the NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS structure. To register optional handlers, *ProtocolSetOptions* calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function.

-   In the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, replace the call to the [**NdisRegisterProtocol**](https://msdn.microsoft.com/library/windows/hardware/ff554653) function with a call to the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function. If an error occurs after a successful call to **NdisRegisterProtocolDriver**, the driver must call the [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) function before **DriverEntry** returns.

<a href="" id="driver-unload"></a>**Driver Unload**  
-   Optionally create the protocol driver's [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function or, if it exists, update it. The *ProtocolUninstall* entry point is in the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure.

-   To deregister the protocol driver, the driver must call the [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) function from its [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine.

<a href="" id="protocol-bind-and-unbind-operations"></a>**Protocol Bind and Unbind Operations**  
-   In NDIS 6.0, the bind and unbind functions receive all of the required binding information from NDIS. Protocol drivers should not issue OID queries to obtain information that is included in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure.

-   Rewrite the [**ProtocolBindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff562465) function (renamed [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220)) to support the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure.

-   Replace calls to the [**NdisOpenAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff553673) function with calls to the [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) function.

-   Rewrite the [**ProtocolOpenAdapterComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563238) function (renamed [*ProtocolOpenAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570265)).

-   To support the returned status, modify the protocol driver's [**ProtocolUnbindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff563260) function (renamed [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278)).

-   Replace calls to the [**NdisCloseAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff550904) function with calls to the [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640) function.

-   Rewrite the [**ProtocolCloseAdapterComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562502) function (renamed [*ProtocolCloseAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570236)).

<a href="" id="send-and-receive-data-paths"></a>**Send and Receive Data Paths**  
-   Send and receive data paths should support multipacket operations.

-   Rewrite the send and receive code paths to use [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

<a href="" id="oid-requests"></a>**OID Requests**  
-   Protocol drivers should not use OID queries to obtain link status information. Instead, protocol driver should use status indications from underlying drivers for status changes in link parameters.

-   Replace calls to the [**NdisRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554681) function with calls to the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) function.

-   Rewrite the [**ProtocolRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563254) function (renamed [**ProtocolOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570264)) to support the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

-   To cancel OID requests, call the [**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622) function.

<a href="" id="status-indications"></a>**Status Indications**  
-   Use status indications from underlying drivers for status changes in link parameters.

-   Rewrite the [**ProtocolStatus**](https://msdn.microsoft.com/library/windows/hardware/ff563257) function (renamed [**ProtocolStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570270)) to support the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure.

<a href="" id="plug-and-play-events"></a>**Plug and Play Events**  
-   Replace the [**ProtocolPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563243) function with the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function.

<a href="" id="binding-states"></a>**Binding States**  
-   Include NDIS 6.0 protocol binding pause and restart functionality. For more information about binding states, see [Supporting NDIS 6.0 Protocol Binding Pause and Restart Operations](supporting-ndis-6-0-protocol-binding-pause-and-restart-operations.md).

 

 





