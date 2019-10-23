---
title: Registering and Deregistering an MSI Interrupt
description: Registering and Deregistering an MSI Interrupt
ms.assetid: 61bdcf8c-b56e-4ef9-b9db-407591ff2f95
keywords:
- MSI-X WDK networking , registering interrupts
- message-signaled interrupts WDK networking , registering interrupts
- MSIs WDK networking , registering interrupts
- interrupts WDK networking , registering
- MSI-X WDK networking , deregistering interrupts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering and Deregistering an MSI Interrupt





To register for MSI support, a miniport driver calls the [**NdisMRegisterInterruptEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterinterruptex) function to register an MSI interrupt. The driver allocates and initializes an [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_interrupt_characteristics) structure to specify the interrupt characteristics and function entry points. The driver must set the **MsiSupported** member of the NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS structure to **TRUE**. The driver then passes the structure to **NdisMRegisterInterruptEx**.

You must define the following functions to support MSI interrupts:

-   [*MiniportMessageInterrupt*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt)

-   [*MiniportMessageInterruptDpc*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt_dpc)

-   [*MiniportDisableMessageInterrupt*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_disable_message_interrupt)

-   [*MiniportEnableMessageInterrupt*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_enable_message_interrupt)

The miniport driver should provide entry points for the line-based interrupt functions (which are shown in the following list), even if the driver supports the MSI entry points. If NDIS does not grant an MSI interrupt, it can grant a normal interrupt as a fallback condition.

The line-interrupt functions include the following:

-   [*MiniportInterrupt*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr)

-   [*MiniportInterruptDPC*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc)

-   [*MiniportDisableInterruptEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_disable_interrupt)

-   [*MiniportEnableInterruptEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_enable_interrupt)

Drivers should call the [**NdisMDeregisterInterruptEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex) function to release resources that were previously allocated with **NdisMRegisterInterruptEx**.

 

 





