---
title: Starting a Device in a Bus Driver
description: Starting a Device in a Bus Driver
ms.assetid: 1babeabb-1866-4ca5-b5a3-380c246596e5
keywords: ["bus drivers WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Starting a Device in a Bus Driver





A bus driver starts a child device (child [*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) with a procedure such as the following in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine:

1.  Start the device.

    The exact steps vary from device to device.

    For example, the PCI bus driver programs its mapping registers to enable requests on the PCI bus. The PnP ISA bus driver enables the PnP ISA card so the function driver can access it.

2.  Complete the IRP.

    If the bus driver's start operations were successful, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS and calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) specifying a priority boost of IO\_NO\_INCREMENT. The bus driver returns STATUS\_SUCCESS from its *DispatchPnP* routine.

    If the bus driver encounters an error during its start operations, the driver sets an error status in the IRP, calls **IoCompleteRequest** with IO\_NO\_INCREMENT, and returns the error from its *DispatchPnP* routine.

If a bus driver requires some time to start the device, it can mark the IRP as pending and return STATUS\_PENDING.

 

 




