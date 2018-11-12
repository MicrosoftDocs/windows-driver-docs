---
title: Summary of changes to port an intermediate driver to NDIS 6.0
description: Summary of Changes Required to Port an Intermediate Driver to NDIS 6.0
ms.assetid: 4992cf66-7775-434a-b9ff-3e9ef10d938f
keywords:
- porting intermediate drivers WDK networking , required changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port an Intermediate Driver to NDIS 6.0





This topic summarizes the changes that are required to port an NDIS 5.*x* intermediate driver to NDIS 6.0. Porting earlier drivers is similar to porting NDIS 5.*x* drivers.

The following general issues apply to intermediate drivers:

-   Except where noted otherwise, protocol driver and miniport driver changes also apply to intermediate drivers. Before you read this summary, see the protocol driver porting summary at [Summary of Changes Required to Port a Protocol Driver to NDIS 6.0](summary-of-changes-required-to-port-a-protocol-driver-to-ndis-6-0.md) and the miniport driver porting summary at [Summary of Changes Required to Port a Miniport Driver to NDIS 6.0](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-0.md).

-   If the intermediate driver is a filter intermediate driver, rewrite it as an NDIS 6.0 filter driver, because filter intermediate drivers are not supported in NDIS 6.0. For more information about filter drivers, see [NDIS 6.0 Filter Drivers](ndis-filter-drivers.md).

To run in the NDIS 6.0 environment, NDIS 5.*x* intermediate drivers must be modified as follows:

<a href="" id="build-environment"></a>Build Environment  
-   Replace the NDIS51\_MINIPORT\_DRIVER preprocessor definition with NDIS60\_MINIPORT\_DRIVER.

-   Replace the NDIS51 preprocessor definition with NDIS60.

<a href="" id="driver-initialization-------"></a>**Driver Initialization**   
-   Remove calls to the [**NdisIMRegisterLayeredMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff552205) function.

-   To register its *MiniportXxx* functions, an intermediate driver must call the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function with the NDIS\_INTERMEDIATE\_DRIVER flag set.

<a href="" id="driver-unload"></a>**Driver Unload**  
-   Optional. Create the intermediate driver's [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function. This function is called [**ProtocolUnload**](https://msdn.microsoft.com/library/windows/hardware/ff563261) in NDIS 5.*x*. For NDIS 6.0, the *ProtocolUninstall* entry point is in the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure (previously known as NDIS\_PROTOCOL\_CHARACTERISTICS).

-   Call the [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) function from the [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function.

<a href="" id="check-for-hang-and-reset-------"></a>**Check for Hang and Reset**   
-   The [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) function (previously known as [**MiniportCheckForHang**](https://msdn.microsoft.com/library/windows/hardware/ff549367)) is not required for intermediate drivers, so intermediate drivers should set its entry point to **NULL**.

-   The [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function (previously known as [*MiniportReset*](https://msdn.microsoft.com/library/windows/hardware/ff550502)) is not required for intermediate drivers, so intermediate drivers should set its entry point to **NULL**.

<a href="" id="send-and-receive-code-paths-------"></a>**Send and Receive Code Paths**   
-   Rewrite the send and receive code paths to use [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

-   Specify the intermediate driver's backfill size requirements. The driver receives backfill requirements from underlying drivers in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) or restart attributes. The driver adds its backfill size requirements to the size that the underlying drivers reported. The driver specfies backfill size requirements for its virtual miniports in the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure or restart attributes.

-   Optional. Use the clone, fragment, and reassemble interfaces when handling NET\_BUFFER\_LIST structures. For more information about handling NET\_BUFFER\_LIST structures, see [Derived NET\_BUFFER\_LIST Structures](derived-net-buffer-list-structures.md).

-   Remove code, if any, that handles "packet stacking" special cases. Instead, use the [**NET\_BUFFER\_LIST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure and related interfaces to create and manage context space.

<a href="" id="oid-requests-------"></a>**OID Requests**   
-   Use the [**NdisAllocateCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff560706) function to allocate and forward OID requests.

-   Use the [**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622) function to cancel OID requests.

<a href="" id="status-indications-------"></a>**Status Indications**   
-   Similar to NDIS 5.*x*. For interface changes, see [Summary of Changes Required to Port a Protocol Driver to NDIS 6.0](summary-of-changes-required-to-port-a-protocol-driver-to-ndis-6-0.md) and [Summary of Changes Required to Port a Miniport Driver to NDIS 6.0](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-0.md).

<a href="" id="plug-and-play-events-------"></a>**Plug and Play Events**   
-   Similar to NDIS 5.*x*. For interface changes, see [Summary of Changes Required to Port a Protocol Driver to NDIS 6.0](summary-of-changes-required-to-port-a-protocol-driver-to-ndis-6-0.md) and [Summary of Changes Required to Port a Miniport Driver to NDIS 6.0](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-0.md).

-   Use the [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) function to propagate a network Plug and Play or Power Management event notification to overlying drivers.

<a href="" id="binding-and-adapter--------states-------"></a>**Binding and Adapter States**   
-   Include NDIS 6.0 pause and restart functionality. Optionally include support for pause and restart of virtual miniports when NDIS pauses an underlying driver stack. For more information about pause and restart, see [Driver Stack Management](driver-stack-management.md).

 

 





