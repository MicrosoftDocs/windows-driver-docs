---
title: Initialization of Storage Virtual Miniport Drivers
description: Initialization of Storage Virtual Miniport Drivers
keywords:
- storage virtual miniport drivers WDK , initialization
- miniport drivers WDK storage
- initializing WDK storage , virtual miniport drivers
ms.date: 04/20/2017
---

# Initialization of Storage Virtual Miniport Drivers


The Storport virtual miniport (VMiniport) driver has three stages of initialization. In the first, the VMiniport (typically in its [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine) calls [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize), which points to a [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure.

In this structure, the VMiniport sets the following fields to point to callback routines:

**HwFindAdapter**. This routine is required for the second stage of initialization.

**HwInitialize**. This routine is required for the third stage of initialization.

**HwInitializeTracing**. This routine is optional, and is unique to a Storport virtual miniport driver.

**HwStartIo**. This routine is required. In a virtual miniport driver, the **HwStorBuildIo** interface is not called prior to calling. [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio). No locks are held prior to calling. **HwStorStartIo**. The default queue depth for each logical unit that is exposed through the virtual miniport interface is 250.

**HwAdapterControl**. This routine is required.

**HwResetBus**. This routine is required. The meaning of "bus" can be defined by the virtual miniport driver developer.

**HwProcessServiceRequest**. This routine is optional, and is unique to a Storport virtual miniport driver. This routine receives a "reverse-callback" IRP, which will be completed when the VMiniport updates the caller (such as a user-mode application or kernel-mode driver) or requires the caller to do something on the VMiniport's behalf.

**HwCompleteServiceIrp**. This routine is optional, and is unique to a Storport virtual miniport driver. However, this routine is required when **HwProcessServiceRequest** points to a callback routine. **HwCompleteServiceIrp** is called when the virtual adapter is being removed so that the VMiniport can complete any reverse-callback IRPs that might be pending.

**HwFreeAdapterResources**. This routine is required, and is unique to a Storport virtual miniport driver. This routine is called when the virtual adapter is being removed so that the VMiniport can free any resources that are allocated during initialization.

**HwCleanupTracing**. This routine is optional, and is unique to a Storport virtual miniport driver. However, this routine is required when **HwInitializeTracing** points to a callback routine.

The virtual miniport driver must also set the following in the same structure:

**HwInitializationDataSize** = **sizeof**(VIRTUAL\_HW\_INITIALIZATION\_DATA).

**AdapterInterfaceType** = **Internal**.

The Storport virtual miniport driver sets other fields as needed. Unused fields must be set to zero.

Without holding any locks and at PASSIVE\_LEVEL, the virtual miniport driver calls [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize) with a pointer to the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure and then checks the status that is returned. The Storport driver retains its own copy of the information in this structure and the miniport driver need not retain this structure after **StorPortInitialize** returns.

[**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) appears in Storport.h.

 

