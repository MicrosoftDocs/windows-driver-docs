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





To register for MSI support, a miniport driver calls the [**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649) function to register an MSI interrupt. The driver allocates and initializes an [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure to specify the interrupt characteristics and function entry points. The driver must set the **MsiSupported** member of the NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS structure to **TRUE**. The driver then passes the structure to **NdisMRegisterInterruptEx**.

You must define the following functions to support MSI interrupts:

-   [*MiniportMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559407)

-   [*MiniportMessageInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff559411)

-   [*MiniportDisableMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559376)

-   [*MiniportEnableMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559383)

The miniport driver should provide entry points for the line-based interrupt functions (which are shown in the following list), even if the driver supports the MSI entry points. If NDIS does not grant an MSI interrupt, it can grant a normal interrupt as a fallback condition.

The line-interrupt functions include the following:

-   [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395)

-   [*MiniportInterruptDPC*](https://msdn.microsoft.com/library/windows/hardware/ff559398)

-   [*MiniportDisableInterruptEx*](https://msdn.microsoft.com/library/windows/hardware/ff559375)

-   [*MiniportEnableInterruptEx*](https://msdn.microsoft.com/library/windows/hardware/ff559380)

Drivers should call the [**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575) function to release resources that were previously allocated with **NdisMRegisterInterruptEx**.

 

 





