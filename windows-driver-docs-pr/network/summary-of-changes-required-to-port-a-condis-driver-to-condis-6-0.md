---
title: Summary of changes to port a CoNDIS driver to CoNDIS 6.0
description: Summary of Changes Required to Port a CoNDIS Driver to CoNDIS 6.0
ms.assetid: 151bdcf8-5f7c-494d-a0a2-d1fac997d82e
keywords:
- porting CoNDIS drivers WDK networking , required changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port a CoNDIS Driver to CoNDIS 6.0





This topic summarizes what you must change to port a connection-oriented NDIS (CoNDIS) 5.*x* driver to CoNDIS 6.0. You can port earlier drivers (before NDIS 5.*x*) in a way similar to porting NDIS 5.*x* drivers.

The following general issues apply to CoNDIS drivers:

-   Except where noted otherwise, connectionless protocol driver and miniport driver porting issues also apply to CoNDIS drivers. Before you read this summary, see [Summary of Changes Required to Port a Protocol Driver to NDIS 6.0](summary-of-changes-required-to-port-a-protocol-driver-to-ndis-6-0.md), [Summary of Changes Required to Port a Miniport Driver to NDIS 6.0](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-0.md), and [Summary of Changes Required to Port an Intermediate Driver to NDIS 6.0](summary-of-changes-required-to-port-an-intermediate-driver-to-ndis-6-0.md).

To run in the CoNDIS 6.0 environment, CoNDIS 5.*x* drivers must be modified in the following areas:

<a href="" id="build-environment"></a>**Build Environment**  
-   Replace the NDIS51\_MINIPORT\_DRIVER preprocessor definition with NDIS60\_MINIPORT\_DRIVER.

-   Replace the NDIS51 preprocessor definition with NDIS60.

<a href="" id="driver-initialization"></a>**Driver Initialization**  
-   To register CoNDIS *ProtocolXxx* and *MiniportXxx* functions, all CoNDIS drivers must call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function.

-   To register its CoNDIS *MiniportXxx* functions, a miniport driver or miniport call manager (MCM) must call the **NdisSetOptionalHandlers** function from its [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function and pass it an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565948) structure. To register call manager *ProtocolXxx* functions, MCMs also provide an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure.

-   To register its CoNDIS *ProtocolXxx* functions, a client or call managers must call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from its [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function and must provide an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566817) structure. Clients must also provide an [**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564884) structure and call managers must also provide an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure.

<a href="" id="registering-and-opening-an-address-family"></a>**Registering and Opening an Address Family**  
-   Replace the client calls to the [**NdisClOpenAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff550895) function with calls to the [**NdisClOpenAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561639) function and replace calls to the [**ProtocolClOpenAfComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562498) function with calls to the [**ProtocolClOpenAfCompleteEx**](https://msdn.microsoft.com/library/windows/hardware/ff570235) function.

-   Replace the call manager calls to the [**NdisCmRegisterAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff551006) function with calls to the [**NdisCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561685) function.

-   Replace the MCM calls to the [**NdisMCmRegisterAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff553429) function with calls to the [**NdisMCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff563554) function.

<a href="" id="closing-an-address-family"></a>**Closing an Address Family**  
-   Remove [OID\_CO\_AF\_CLOSE](https://msdn.microsoft.com/library/windows/hardware/ff569088) OID requests. Instead, call the [**NdisCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561680) function or the [**NdisMCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff563546) function.

-   Clients must register the [**ProtocolClNotifyCloseAf**](https://msdn.microsoft.com/library/windows/hardware/ff570234) function.

-   Call managers and MCMs must register the [**ProtocolCmNotifyCloseAfComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570248) function. NDIS calls *ProtocolCmNotifyCloseAfComplete* if a client completes the address family (AF) close operation by calling the [**NdisClNotifyCloseAddressFamilyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561638) function.

<a href="" id="send-and-receive-code-paths"></a>**Send and Receive Code Paths**  
-   Rewrite the send and receive code paths to use [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

<a href="" id="oid-requests"></a>**OID Requests**  
-   Replace references to the [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structure with references to the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

-   Replace the miniport driver and MCM [**MiniportCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549413) function with the [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function. Replace calls to [**NdisMCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553473) with calls to the [**NdisMCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563568) function.

-   Replace the client and call manager [**ProtocolCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563227) and [**ProtocolCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563225) functions with the [**ProtocolCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570255) and [**ProtocolCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff570254) functions respectively. Replace calls to the [**NdisCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff551884) and [**NdisCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff551877) functions with calls to the [**NdisCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561716) and [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) respectively.

-   Replace MCM calls to the [**NdisMCmRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553443) and [**NdisMCmRequest**](https://msdn.microsoft.com/library/windows/hardware/ff553438) functions with calls to the [**NdisMCmOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563551) and [**NdisMCmOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563548) functions respectively.

-   Use the [**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622) function to cancel OID requests.

<a href="" id="status-indications"></a>**Status Indications**  
-   Replace miniport driver and MCM calls to the [**NdisMCoIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553458) function with calls to the [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) function.

-   Replace the protocol driver [**ProtocolCoStatus**](https://msdn.microsoft.com/library/windows/hardware/ff563235) function with the [**ProtocolCoStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570258) function.

<a href="" id="binding-and-adapter-states"></a>**Binding and Adapter States**  
-   Include NDIS 6.0 pause and restart functionality. For more information about pause and restart, see [Driver Stack Management](driver-stack-management.md).

 

 





