---
title: Adding a NIC
description: Adding a NIC
ms.assetid: 3da89acc-5504-4362-b148-e8228795721f
keywords:
- NICs WDK networking , adding
- network interface cards WDK networking , adding
- Plug and Play WDK NDIS miniport , adding NIC
- adding NICs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding a NIC





The following description starts with the loading of the miniport driver and describes how a NIC is added. For the initial processing that the PnP manager performs when a NIC is added to a running system, see steps 1-11 of [Adding a PnP Device to a Running System](https://msdn.microsoft.com/library/windows/hardware/ff540535).

1.  If the miniport driver for the NIC is not already loaded, the PnP manager loads the driver and then calls the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818) function. If the driver is already loaded, processing continues with step 4.

2.  From its **DriverEntry** function, the miniport driver registers as a miniport drivers and performs other drivers initialization. For more information about registering as a miniport driver, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

3.  NDIS fills in the following entries in the driver object for the miniport driver:
    -   The entry point for the *AddDevice* routine.
    -   The *DispatchXxx* entry points for handling IRPs.
    -   The entry point for the *Unload* routine.

4.  The PnP manager calls NDIS's *AddDevice* routine. NDIS's *AddDevice* routine creates a functional device object (FDO) for the newly added NIC and attaches this FDO to the device stack for the NIC.

5.  NDIS reads information from the registry to obtain configuration information for the NIC. This information includes binding information and the hardware attributes of the NIC.

6.  The PnP manager assigns resources to the NIC, if necessary.

 

 





