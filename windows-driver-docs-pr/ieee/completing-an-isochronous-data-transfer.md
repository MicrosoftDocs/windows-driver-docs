---
title: Completing an Isochronous Data Transfer
description: Completing an Isochronous Data Transfer
keywords:
- isochronous I/O WDK IEEE 1394 bus , completing transfers
ms.date: 03/03/2023
---

# Completing an Isochronous Data Transfer





Once a device no longer needs to transfer data, the driver must inform the bus that the operation is complete, and then deallocate the isochronous resources it allocated when setting up.

Drivers must follow these steps to clean up:

1.  If the driver has begun an isochronous operation through the [**REQUEST_ISOCH_LISTEN**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) or [**REQUEST_ISOCH_TALK**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) bus requests, it must issue the [**REQUEST_ISOCH_STOP**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) request to signal the bus driver to stop the isochronous operation.

2.  Any buffers that remain attached to a resource handle must be detached by using the [**REQUEST_ISOCH_DETACH_BUFFERS**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) request.

3.  If the driver has allocated a resource handle, it must deallocate it through the [**REQUEST_ISOCH_FREE_RESOURCES**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) request.

4.  If the driver has a channel allocated, it must deallocate it through the [**REQUEST_ISOCH_FREE_CHANNEL**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) request.

5.  The driver must deallocate any bandwidth it has allocated by using the [**REQUEST_ISOCH_FREE_BANDWIDTH**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) request.



 




