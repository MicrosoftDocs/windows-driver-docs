---
title: Porting Interrupt Registration to NDIS 6.0
description: Porting Interrupt Registration to NDIS 6.0
ms.assetid: 824c8b48-e0d8-45a2-abf9-9713a0f51efe
keywords:
- interrupts WDK networking , registration
- message-signaled interrupts WDK networking , registration
- MSIs WDK networking , registration
- registering interrupts
- unregistering interrupts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Interrupt Registration to NDIS 6.0





NDIS 6.0 drivers do not call the [**NdisMRegisterInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff553596) function. Instead, NDIS 6.0 drivers call the [**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649) function and pass it a pointer to the [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure.

In NDIS 5.x, the miniport driver defines interrupt-related function entry points in the NDIS\_MINIPORT\_CHARACTERISTICS structure. NDIS 6.0 drivers define the entry points for these functions in the NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS structure.

An NDIS 6.0 miniport driver supplies the following interrupt-related functions.

[*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395)

[*MiniportInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff559398)

[*MiniportDisableInterruptEx*](https://msdn.microsoft.com/library/windows/hardware/ff559375)

[*MiniportEnableInterruptEx*](https://msdn.microsoft.com/library/windows/hardware/ff559380)

The following code example shows how a miniport driver can initialize this structure.

```C++
        NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS Interrupt;
        RtlZeroMemory(&Interrupt, sizeof(Interrupt));

        Interrupt.Header.Type = NDIS_OBJECT_TYPE_MINIPORT_INTERRUPT;
        Interrupt.Header.Revision = NDIS_MINIPORT_INTERRUPT_REVISION_1;
        Interrupt.Header.Size = sizeof(NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS);

        Interrupt.InterruptHandler = MiniportInterrupt;
        Interrupt.InterruptDpcHandler = MiniportInterruptDpc;
        Interrupt.DisableInterruptHandler = MiniportDisableInterruptEx;
        Interrupt.EnableInterruptHandler = MiniportEnableInterruptEx;
        
        Status = NdisMRegisterInterruptEx(Adapter->AdapterHandle,
                                          Adapter,
                                          &Interrupt,
                                          &Adapter->NdisInterruptHandle );
```

The miniport driver passes a handle to [**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649) in the **MiniportInterruptContext** member of the [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure. NDIS passes this handle to the driver's interrupt-related functions.

To deregister an interrupt, a miniport driver calls the [**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575) function instead of the [**NdisMDeregisterInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff553501) function.

For more information about registering interrupts, see [Registering and Deregistering Interrupts](registering-and-deregistering-interrupts.md).

 

 





