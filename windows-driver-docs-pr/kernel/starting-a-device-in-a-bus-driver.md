---
title: Starting a Device in a Bus Driver
description: Starting a Device in a Bus Driver
keywords: ["bus drivers WDK PnP"]
ms.date: 06/16/2017
---

# Starting a Device in a Bus Driver





A bus driver starts a child device (child *PDO*) with a procedure such as the following in its [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine:

1.  Start the device.

    The exact steps vary from device to device.

    For example, the PCI bus driver programs its mapping registers to enable requests on the PCI bus. The PnP ISA bus driver enables the PnP ISA card so the function driver can access it.

2.  Complete the IRP.

    If the bus driver's start operations were successful, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS and calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) specifying a priority boost of IO\_NO\_INCREMENT. The bus driver returns STATUS\_SUCCESS from its *DispatchPnP* routine.

    If the bus driver encounters an error during its start operations, the driver sets an error status in the IRP, calls **IoCompleteRequest** with IO\_NO\_INCREMENT, and returns the error from its *DispatchPnP* routine.

If a bus driver requires some time to start the device, it can mark the IRP as pending and return STATUS\_PENDING.

 

