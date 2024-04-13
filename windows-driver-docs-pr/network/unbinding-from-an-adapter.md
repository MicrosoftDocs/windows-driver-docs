---
title: Unbinding from an Adapter
description: Unbinding from an Adapter
keywords:
- protocol drivers WDK networking , unbinding
- NDIS protocol drivers WDK , unbinding
- unbinding from adapter WDK networking
ms.date: 04/20/2017
---

# Unbinding from an Adapter





NDIS calls a protocol driver's [*ProtocolUnbindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex) function to request that the driver unbind from an underlying adapter. As the reciprocal of [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex), NDIS calls *ProtocolUnbindAdapterEx* to close the binding to the adapter and to release the resources that the driver allocated for the binding.

In *ProtocolUnbindAdapterEx*, a protocol driver calls [**NdisCloseAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseadapterex) to close the binding to an underlying adapter. The protocol driver passes **NdisCloseAdapterEx** the handle that [**NdisOpenAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenadapterex) provided at its *NdisBindingHandle* parameter. This handle identifies the binding that NDIS should close.

Protocol drivers must close an adapter from the *ProtocolBindAdapterEx* function or *ProtocolUnbindAdapterEx* function.

If a protocol driver must initiate an operation to close a binding, the driver can call [**NdisUnbindAdapter**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisunbindadapter). **NdisUnbindAdapter** schedules a work item that results in an NDIS call to *ProtocolUnbindAdapterEx*. This work item can run before the call to **NdisUnbindAdapter** returns. Therefore, driver writers must assume that the binding handle is invalid after **NdisUnbindAdapter** returns.

If a protocol driver returns NDIS\_STATUS\_PENDING from *ProtocolUnbindAdapterEx*, it must call [**NdisCompleteUnbindAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscompleteunbindadapterex) with the final status to complete the bind request.

If NDIS returns NDIS\_STATUS\_PENDING from **NdisCloseAdapterEx**, NDIS later calls the protocol driver's [*ProtocolCloseAdapterCompleteEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_close_adapter_complete_ex) function.

NDIS can call *ProtocolUnbindAdapterEx* if the binding is in the Paused state.

After all the unbind operations are complete, the binding is in the Unbound state.

 

