---
title: Setting Attributes on a Parallel Device
description: Setting Attributes on a Parallel Device
ms.assetid: 10df9a1b-99ec-46b1-b515-10fb20fe2aed
keywords:
- parallel devices WDK , attributes
- attributes WDK parallel devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Attributes on a Parallel Device





A client uses following device control requests to set the indicated operations of a parallel device:

-   [**IOCTL\_PAR\_SET\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddpar/ni-ntddpar-ioctl_par_set_information) initializes a parallel device.

-   [**IOCTL\_SERIAL\_SET\_TIMEOUTS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddser/ni-ntddser-ioctl_serial_set_timeouts) sets time outs for a parallel device.

-   [**IOCTL\_PAR\_SET\_READ\_ADDRESS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddpar/ni-ntddpar-ioctl_par_set_read_address) sets an ECP or EPP read address (channel) for a parallel device.

-   [**IOCTL\_PAR\_SET\_WRITE\_ADDRESS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddpar/ni-ntddpar-ioctl_par_set_write_address) sets an ECP or EPP write address (channel) for a parallel device.

 

 




