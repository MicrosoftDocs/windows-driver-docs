---
title: Setting and Clearing the Communication Mode on a Parallel Port
description: Setting and Clearing the Communication Mode on a Parallel Port
ms.assetid: a22cdeef-4ae7-49f8-b0b5-a4d68feb4235
keywords:
- parallel ports WDK , communication modes
- communication modes WDK parallel ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting and Clearing the Communication Mode on a Parallel Port





A client sets the communication mode on a parallel port by using the following internal device control requests:

[**IOCTL\_INTERNAL\_PARALLEL\_SET\_CHIP\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544031)

[**IOCTL\_INTERNAL\_PARALLEL\_CLEAR\_CHIP\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544017)

A kernel-mode driver can also use the system-supplied [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275) obtained with an [**IOCTL\_INTERNAL\_GET\_PARALLEL\_PNP\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff543997) request. This request returns a [**PARALLEL\_PNP\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544299) structure that includes the following pointers to system-supplied callbacks:

-   The **TrySetChipMode** member is a pointer to a [*PPARALLEL\_SET\_CHIP\_MODE*](https://msdn.microsoft.com/library/windows/hardware/ff544542) callback, which sets the operating mode of a parallel port.

-   The **ClearChipMode** member is a pointer to a [*PPARALLEL\_CLEAR\_CHIP\_MODE*](https://msdn.microsoft.com/library/windows/hardware/ff544398) callback, which clears the operating mode of a parallel port by resetting the communication mode of the host chipset to IEEE 1284-compatibility mode.

A client must first allocate a parallel port before it can set or clear the communication mode.

A client must first clear the communication mode before it can set a new communication mode. Clearing the communication mode returns the host chipset to IEEE 1284-compatibility mode.

To determine the current mode, a client can use the IOCTL\_INTERNAL\_GET\_PARALLEL\_PNP\_INFO request, which returns a PARALLEL\_PNP\_INFORMATION structure that contains information about the current communication mode.

 

 




