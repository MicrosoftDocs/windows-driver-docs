---
title: Unbinding from an Adapter
description: Unbinding from an Adapter
ms.assetid: cea2ce45-df0c-4c75-a780-5810ea01b987
keywords:
- protocol drivers WDK networking , unbinding
- NDIS protocol drivers WDK , unbinding
- unbinding from adapter WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unbinding from an Adapter





NDIS calls a protocol driver's [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function to request that the driver unbind from an underlying adapter. As the reciprocal of [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220), NDIS calls *ProtocolUnbindAdapterEx* to close the binding to the adapter and to release the resources that the driver allocated for the binding.

In *ProtocolUnbindAdapterEx*, a protocol driver calls [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640) to close the binding to an underlying adapter. The protocol driver passes **NdisCloseAdapterEx** the handle that [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) provided at its *NdisBindingHandle* parameter. This handle identifies the binding that NDIS should close.

Protocol drivers must close an adapter from the *ProtocolBindAdapterEx* function or *ProtocolUnbindAdapterEx* function.

If a protocol driver must initiate an operation to close a binding, the driver can call [**NdisUnbindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff564630). **NdisUnbindAdapter** schedules a work item that results in an NDIS call to *ProtocolUnbindAdapterEx*. This work item can run before the call to **NdisUnbindAdapter** returns. Therefore, driver writers must assume that the binding handle is invalid after **NdisUnbindAdapter** returns.

If a protocol driver returns NDIS\_STATUS\_PENDING from *ProtocolUnbindAdapterEx*, it must call [**NdisCompleteUnbindAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561708) with the final status to complete the bind request.

If NDIS returns NDIS\_STATUS\_PENDING from **NdisCloseAdapterEx**, NDIS later calls the protocol driver's [*ProtocolCloseAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570236) function.

NDIS can call *ProtocolUnbindAdapterEx* if the binding is in the Paused state.

After all the unbind operations are complete, the binding is in the Unbound state.

 

 





