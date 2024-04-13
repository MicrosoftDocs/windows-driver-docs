---
title: Obtaining Information About a Parallel Port
description: Obtaining Information About a Parallel Port
keywords:
- parallel ports WDK , obtaining information
ms.date: 03/03/2023
---

# Obtaining Information About a Parallel Port





Before a client uses a parallel port, it can obtain information about the following:

-   Resources used by the parallel port

-   Hardware capabilities of the parallel port

-   [Parallel port callback routines](/windows-hardware/drivers/ddi/_parports/) that a kernel-mode driver can use

A client uses the following internal device control requests to obtain the above information:

[**IOCTL\_INTERNAL\_GET\_PARALLEL\_PORT\_INFO**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_get_parallel_port_info)

[**IOCTL\_INTERNAL\_GET\_MORE\_PARALLEL\_PORT\_INFO**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_get_more_parallel_port_info)

[**IOCTL\_INTERNAL\_GET\_PARALLEL\_PNP\_INFO**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_get_parallel_pnp_info)

A client releases parallel port information by using an [**IOCTL\_INTERNAL\_RELEASE\_PARALLEL\_PORT\_INFO**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_release_parallel_port_info) request.

 

