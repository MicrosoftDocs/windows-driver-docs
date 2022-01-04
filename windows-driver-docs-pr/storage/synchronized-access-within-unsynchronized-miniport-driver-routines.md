---
title: Synchronized Access within Miniport Driver Routines
description: Even when a miniport driver executes in full-duplex mode or has unsynchronized processing of SRBs, it might still require synchronized access.
ms.date: 04/20/2017
---

# Synchronized Access within Miniport Driver Routines


## <span id="ddk_synchronized_access_within_unsynchronized_miniport_driver_routines"></span><span id="DDK_SYNCHRONIZED_ACCESS_WITHIN_UNSYNCHRONIZED_MINIPORT_DRIVER_ROUTINES"></span>


Even when a miniport driver executes in full-duplex mode or does unsynchronized processing of SRBs in an [**HwStorBuildIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_buildio) routine, it might still require synchronized access to its device extension. The library of support routines provided by the Storport driver includes [**StorPortSynchronizeAccess**](/windows-hardware/drivers/ddi/storport/nf-storport-storportsynchronizeaccess), a routine that allows miniport drivers to synchronize access to critical data structures such as the device extension.

When the miniport driver calls **StorPortSynchronizeAccess**, it must supply the routine with a pointer to a callback routine. The callback routine contains the part of the SRB's processing that must be synchronized with the host bus adapter's interrupt handler. For better performance, write your driver to spend as little time as possible executing the callback routine.

 

