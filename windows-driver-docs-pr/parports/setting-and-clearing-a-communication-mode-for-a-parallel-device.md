---
title: Setting and Clearing a Communication Mode for a Parallel Device
description: Setting and Clearing a Communication Mode for a Parallel Device
ms.assetid: 2ff53ed0-dbb7-4c8f-b6e4-5f7d20124a7c
keywords:
- parallel devices WDK , communication modes
- communication modes WDK parallel devices
- clearing communication modes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting and Clearing a Communication Mode for a Parallel Device





A client can set the communication mode of a parallel device using the following device control requests:

-   [**IOCTL\_IEEE1284\_GET\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff543975) returns the current communication protocols set on the device. The port does not have to be locked to use this request.

-   [**IOCTL\_IEEE1284\_NEGOTIATE**](https://msdn.microsoft.com/library/windows/hardware/ff543978) negotiates a new communication mode. The parallel port must be allocated and the IEEE 1284.3 device selected.

-   [**IOCTL\_INTERNAL\_DISCONNECT\_IDLE**](https://msdn.microsoft.com/library/windows/hardware/ff543993) sets the communication mode to IEEE\_COMPATIBLE. The parallel port must be allocated and the IEEE 1284.3 device selected.

A kernel-mode driver can also use the system-supplied [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275). An [**IOCTL\_INTERNAL\_PARCLASS\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff544040) request returns a [**PARCLASS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544334) structure that includes the following pointers to system-supplied callback routines:

-   The **DetermineIeeeMode** member is a pointer to the [**PDETERMINE\_IEEE\_MODES**](https://msdn.microsoft.com/library/windows/hardware/ff544365) callback, which determines the IEEE communication modes that the parallel port supports.

-   The **NegotiateIeeeMode** member is a pointer to the [**PNEGOTIATE\_IEEE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544386) callback, which sets the fastest IEEE communication mode that the parallel port bus driver supports from among the modes specified by the caller.

-   The **TerminateIeeeMode** member is a pointer to the [**PTERMINATE\_IEEE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544773) callback, which sets the communication mode to IEEE 1284-compatibility mode.

-   The **IeeeFwdToRev** member is a pointer to the [**PPARALLEL\_IEEE\_FWD\_TO\_REV**](https://msdn.microsoft.com/library/windows/hardware/ff544524) callback, which changes the data transfer direction from forward to reverse (from write to read).

-   The **IeeeRevToFwd** member is a pointer to the [**PPARALLEL\_IEEE\_REV\_TO\_FWD**](https://msdn.microsoft.com/library/windows/hardware/ff544528) callback, changes the transfer direction from reverse to forward (from read to write).

For more information about the communication modes that the parallel port bus driver supports, see the modes NONE through ECP\_ANY that are defined in the header file *ntddpar.h* in the Windows Driver Kit (WDK).

 

 




