---
title: Obtaining Information About a Parallel Port
description: Obtaining Information About a Parallel Port
ms.assetid: d8ae2296-05b6-419a-93cc-00fcb12d41fe
keywords:
- parallel ports WDK , obtaining information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Information About a Parallel Port





Before a client uses a parallel port, it can obtain information about the following:

-   Resources used by the parallel port

-   Hardware capabilities of the parallel port

-   [Parallel port callback routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index) that a kernel-mode driver can use

A client uses the following internal device control requests to obtain the above information:

[**IOCTL\_INTERNAL\_GET\_PARALLEL\_PORT\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/parallel/ni-parallel-ioctl_internal_get_parallel_port_info)

[**IOCTL\_INTERNAL\_GET\_MORE\_PARALLEL\_PORT\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/parallel/ni-parallel-ioctl_internal_get_more_parallel_port_info)

[**IOCTL\_INTERNAL\_GET\_PARALLEL\_PNP\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/parallel/ni-parallel-ioctl_internal_get_parallel_pnp_info)

A client releases parallel port information by using an [**IOCTL\_INTERNAL\_RELEASE\_PARALLEL\_PORT\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/parallel/ni-parallel-ioctl_internal_release_parallel_port_info) request.

 

 




