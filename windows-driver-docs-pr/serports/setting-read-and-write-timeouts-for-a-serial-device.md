---
title: Setting Read and Write Timeouts for a Serial Device
description: Setting Read and Write Timeouts for a Serial Device
keywords:
- Serial driver WDK , time-outs
- time-outs WDK serial devices
- serial devices WDK , time-outs
- read time-outs WDK serial devices
- write time-outs WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Read and Write Timeouts for a Serial Device

A client can use an [**IOCTL\_SERIAL\_SET\_TIMEOUTS**](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_timeouts) request to set time-out values that the system-supplied Serial.sys driver uses for read and write requests. Serial.sys continues to transfer bytes until the requested number of bytes are transferred or a time-out event occurs.

The time-out operation in Serial.sys is compliant with the user-mode operation of [COM ports](configuration-of-com-ports.md) that is supported by the communication functions that are supported by the Windows Base Services in the Microsoft Windows SDK.

Note that the time-out operation is not applied to a pending request while it is queued. The time-out operation is applied to a request after the request becomes current (that is, Serial.sys starts to process the request).

For more information about the read and write time-outs, see the following:

- The [**SERIAL\_TIMEOUTS**](/windows-hardware/drivers/ddi/ntddser/ns-ntddser-_serial_timeouts) structure in the Ntddser.h header file in the Windows Driver Kit (WDK).

- The [**SetCommTimeouts**](/windows/win32/api/winbase/nf-winbase-setcommtimeouts) function and the [**COMMTIMEOUTS**](/windows/win32/api/winbase/ns-winbase-commtimeouts) structure that are supported by the Windows Base Services in the Windows SDK.
