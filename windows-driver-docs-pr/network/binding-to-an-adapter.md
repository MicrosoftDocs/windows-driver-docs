---
title: Binding to an Adapter
description: Binding to an Adapter
ms.assetid: 583b7c73-fbc7-4d25-95f7-973cede61ec8
keywords:
- protocol drivers WDK networking , binding to adapter
- NDIS protocol drivers WDK , binding to adapter
- binding operation WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Binding to an Adapter





NDIS calls a protocol driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function to open a binding whenever an underlying adapter to which the driver can bind becomes available. After NDIS calls *ProtocolBindAdapterEx*, the binding enters the Opening state. In the *Opening* state, the protocol driver allocates resources for the binding and opens the adapter.

NDIS passes to *ProtocolBindAdapterEx* the NDIS context for the binding operation as well as a pointer to an [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. This structure contains information about the adapter such as:

-   The name of the adapter.

-   The registry location for parameters specific to this binding under protocol service entry in the registry.

-   The physical device object for the adapter.

To open an adapter, protocol drivers call the [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) function. The protocol driver passes the following to **NdisOpenAdapterEx**:

-   The handle that NDIS returned to the driver at the *NdisProtocolHandle* parameter of the **NdisRegisterProtocolDriver** function.

-   The protocol driver's context for this binding.

-   A pointer to a structure of type [**NDIS\_OPEN\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566734).

[**NDIS\_OPEN\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566734) contains information such as name of the adapter that **NdisOpenAdapterEx** should open, an array of medium types that the protocol driver supports and, optionally, an array of frame types that the driver can receive on this binding.

If a protocol driver returns NDIS\_STATUS\_PENDING from *ProtocolBindAdapterEx*, it must call [**NdisCompleteBindAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561702) with the final status to complete the bind request.

If NDIS returns NDIS\_STATUS\_PENDING from **NdisOpenAdapterEx**, NDIS later calls the protocol driver's [*ProtocolOpenAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570265) function with the final status after the open request has been completed.

After the driver successfully opens the binding to the adapter, the binding is in the Paused state.

A protocol driver calls the [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640) function to close the adapter. The driver can call **NdisCloseAdapterEx** from the *ProtocolBindAdapterEx* function or [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function.

If after opening the adapter and before completing the bind request, *ProtocolBindAdapterEx* encounters a failure and must close the binding to the adapter, it can call **NdisCloseAdapterEx**. For more information about closing an adapter, see [Unbinding from an Adapter](unbinding-from-an-adapter.md).

 

 





