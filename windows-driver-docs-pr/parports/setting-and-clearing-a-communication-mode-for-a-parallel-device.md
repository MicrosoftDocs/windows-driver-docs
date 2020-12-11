---
title: Setting and Clearing a Communication Mode for a Parallel Device
description: Setting and Clearing a Communication Mode for a Parallel Device
keywords:
- parallel devices WDK , communication modes
- communication modes WDK parallel devices
- clearing communication modes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting and Clearing a Communication Mode for a Parallel Device





A client can set the communication mode of a parallel device using the following device control requests:

-   [**IOCTL\_IEEE1284\_GET\_MODE**](/windows-hardware/drivers/ddi/ntddpar/ni-ntddpar-ioctl_ieee1284_get_mode) returns the current communication protocols set on the device. The port does not have to be locked to use this request.

-   [**IOCTL\_IEEE1284\_NEGOTIATE**](/windows-hardware/drivers/ddi/ntddpar/ni-ntddpar-ioctl_ieee1284_negotiate) negotiates a new communication mode. The parallel port must be allocated and the IEEE 1284.3 device selected.

-   [**IOCTL\_INTERNAL\_DISCONNECT\_IDLE**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_disconnect_idle) sets the communication mode to IEEE\_COMPATIBLE. The parallel port must be allocated and the IEEE 1284.3 device selected.

A kernel-mode driver can also use the system-supplied [parallel device callback routines](/windows-hardware/drivers/ddi/index). An [**IOCTL\_INTERNAL\_PARCLASS\_CONNECT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parclass_connect) request returns a [**PARCLASS\_INFORMATION**](/windows-hardware/drivers/ddi/parallel/ns-parallel-_parclass_information) structure that includes the following pointers to system-supplied callback routines:

-   The **DetermineIeeeMode** member is a pointer to the [**PDETERMINE\_IEEE\_MODES**](/windows-hardware/drivers/ddi/parallel/nc-parallel-pdetermine_ieee_modes) callback, which determines the IEEE communication modes that the parallel port supports.

-   The **NegotiateIeeeMode** member is a pointer to the [**PNEGOTIATE\_IEEE\_MODE**](/windows-hardware/drivers/ddi/parallel/nc-parallel-pnegotiate_ieee_mode) callback, which sets the fastest IEEE communication mode that the parallel port bus driver supports from among the modes specified by the caller.

-   The **TerminateIeeeMode** member is a pointer to the [**PTERMINATE\_IEEE\_MODE**](/windows-hardware/drivers/ddi/parallel/nc-parallel-pterminate_ieee_mode) callback, which sets the communication mode to IEEE 1284-compatibility mode.

-   The **IeeeFwdToRev** member is a pointer to the [**PPARALLEL\_IEEE\_FWD\_TO\_REV**](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_ieee_fwd_to_rev) callback, which changes the data transfer direction from forward to reverse (from write to read).

-   The **IeeeRevToFwd** member is a pointer to the [**PPARALLEL\_IEEE\_REV\_TO\_FWD**](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_ieee_rev_to_fwd) callback, changes the transfer direction from reverse to forward (from read to write).

For more information about the communication modes that the parallel port bus driver supports, see the modes NONE through ECP\_ANY that are defined in the header file *ntddpar.h* in the Windows Driver Kit (WDK).

 

