---
title: Setting Attributes on a Parallel Device
description: Setting Attributes on a Parallel Device
keywords:
- parallel devices WDK , attributes
- attributes WDK parallel devices
ms.date: 03/03/2023
---

# Setting Attributes on a Parallel Device





A client uses following device control requests to set the indicated operations of a parallel device:

-   [**IOCTL\_PAR\_SET\_INFORMATION**](/windows-hardware/drivers/ddi/ntddpar/ni-ntddpar-ioctl_par_set_information) initializes a parallel device.

-   [**IOCTL\_SERIAL\_SET\_TIMEOUTS**](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_timeouts) sets time outs for a parallel device.

-   [**IOCTL\_PAR\_SET\_READ\_ADDRESS**](/windows-hardware/drivers/ddi/ntddpar/ni-ntddpar-ioctl_par_set_read_address) sets an ECP or EPP read address (channel) for a parallel device.

-   [**IOCTL\_PAR\_SET\_WRITE\_ADDRESS**](/windows-hardware/drivers/ddi/ntddpar/ni-ntddpar-ioctl_par_set_write_address) sets an ECP or EPP write address (channel) for a parallel device.

 

