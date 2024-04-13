---
title: Half-Duplex Mode Not Appropriate for Shipped Products
description: Half-Duplex Mode Not Appropriate for Shipped Products
ms.date: 04/20/2017
---

# Half-Duplex Mode: Not Appropriate for Shipped Products


Half-duplex mode is intended for use only during the initial porting of a miniport from the SCSI port driver model to the Storport driver model. It restricts the port/miniport synchronization to that of SCSI port miniports, where a lock is used to synchronize the execution of its [**StartIo**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) and interrupt service routines. This results in spending more time at device IRQL (DIRQL), and reduces concurrency in I/O processing, which leads to lower performance. It is not compatible with the newer Storport interfaces and optimizations, and is therefore not appropriate for use in shipping products.

If you continue to ship a half-duplex miniport, you risk compatibility issues with future revisions of Storport.

 

