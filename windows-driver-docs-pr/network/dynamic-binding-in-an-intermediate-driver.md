---
title: Dynamic Binding in an Intermediate Driver
description: Dynamic Binding in an Intermediate Driver
keywords:
- intermediate drivers WDK networking , binding
- NDIS intermediate drivers WDK , binding
- dynamic binding WDK networking
- binding operations WDK networking
ms.date: 04/20/2017
---

# Dynamic Binding in an Intermediate Driver





An intermediate driver must support dynamic binding to underlying miniport adapters by providing both a [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) and a [*ProtocolUnbindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex) function.

When a miniport adapter becomes available, NDIS calls the *ProtocolBindAdapterEx* function of any intermediate driver that can bind to that miniport adapter. As part of the binding operation, the intermediate driver should initialize a virtual miniport that is associated with that miniport adapter. When a miniport adapter is removed, NDIS calls the *ProtocolUnbindAdapterEx* function of any intermediate driver that is bound to that miniport adapter.

The following topics contain additional information about dynamic binding operations in intermediate drivers:

[Intermediate Driver Binding Operations](intermediate-driver-binding-operations.md)

[Opening an Adapter Underlying an Intermediate Driver](opening-an-adapter-underlying-an-intermediate-driver.md)

[Initializing Virtual Miniports](initializing-virtual-miniports.md)

[Intermediate Driver Unbinding Operations](intermediate-driver-unbinding-operations.md)

 

