---
title: Completing an Isochronous Data Transfer
description: Completing an Isochronous Data Transfer
ms.assetid: 1fc98e1b-4dd5-4358-aa23-86fcbbf33967
keywords:
- isochronous I/O WDK IEEE 1394 bus , completing transfers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing an Isochronous Data Transfer





Once a device no longer needs to transfer data, the driver must inform the bus that the operation is complete, and then deallocate the isochronous resources it allocated when setting up.

Drivers must follow these steps to clean up:

1.  If the driver has begun an isochronous operation through the [**REQUEST\_ISOCH\_LISTEN**](https://msdn.microsoft.com/library/windows/hardware/ff537655) or [**REQUEST\_ISOCH\_TALK**](https://msdn.microsoft.com/library/windows/hardware/ff537660) bus requests, it must issue the [**REQUEST\_ISOCH\_STOP**](https://msdn.microsoft.com/library/windows/hardware/ff537659) request to signal the bus driver to stop the isochronous operation.

2.  Any buffers that remain attached to a resource handle must be detached by using the [**REQUEST\_ISOCH\_DETACH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff537651) request.

3.  If the driver has allocated a resource handle, it must deallocate it through the [**REQUEST\_ISOCH\_FREE\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff537654) request.

4.  If the driver has a channel allocated, it must deallocate it through the [**REQUEST\_ISOCH\_FREE\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537653) request.

5.  The driver must deallocate any bandwidth it has allocated by using the [**REQUEST\_ISOCH\_FREE\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537652) request.

 

 




