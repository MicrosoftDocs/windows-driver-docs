---
title: Initializing the Display Miniport Driver
description: Initializing the Display Miniport Driver
keywords:
- miniport drivers WDK display , initializing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing the Display Miniport Driver


After the operating system has loaded the display miniport driver, the following steps occur to initialize the display miniport driver:

1.  The operating system calls the display miniport driver's [**DriverEntry**](./driverentry-of-display-miniport-driver.md) function.

2.  **DriverEntry** allocates a [**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure and populates the **Version** member of DRIVER\_INITIALIZATION\_DATA with DXGKDDI\_INTERFACE\_VERSION and the remaining members of DRIVER\_INITIALIZATION\_DATA with pointers to the display miniport driver's other entry point functions (that is, the functions that the display miniport driver implements).

3.  **DriverEntry** calls the [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize) function to load the Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) and to supply the DirectX graphics kernel subsystem with pointers to the display miniport driver's other entry point functions.

4.  After **DxgkInitialize** returns, **DriverEntry** propagates the return value of **DxgkInitialize** back to the operating system. Display miniport driver writers should make no assumptions about the value that **DxgkInitialize** returns.

