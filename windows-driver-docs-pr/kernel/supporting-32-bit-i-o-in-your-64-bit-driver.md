---
title: Supporting 32-Bit I/O in Your 64-Bit Driver
description: Supporting 32-Bit I/O in Your 64-Bit Driver
keywords: ["32-bit I/O support WDK 64-bit", "64-bit WDK kernel , 32-bit I/O support", "thunking WDK", "WOW64 thunking layer WDK", "converting parameters to fixed-precision types", "32-bit I/O support WDK 64-bit , about 32-bit I/O support in 64-bit", "control codes WDK 64-bit", "I/O control codes WDK kernel , 32-bit I/O in 64-bit drivers", "IOCTLs WDK kernel , 32-bit I/O in 64-bit drivers", "file system control codes WDK 64-bit", "FSCTL WDK 64-bit", "buffer pointers WDK 64-bit"]
ms.date: 06/16/2017
---

# Supporting 32-Bit I/O in Your 64-Bit Driver





Windows on Windows (WOW64) enables Microsoft Win32 user-mode applications to run on 64-bit Windows. It does this by intercepting Win32 function calls and converting parameters from 32-bit pointer types to 64-bit pointer types as appropriate before making the transition to the 64-bit kernel. This conversion, which is called *thunking*, is done automatically for all Win32 functions, with one important exception: the data buffers passed to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol). The contents of these buffers, which are pointed to by the *InputBuffer* and *OutputBuffer* parameters, are not thunked, because their structure is driver-specific.

**Note**   Although the buffer *contents* are not thunked, the buffer *pointers* are converted into 64-bit pointers.

 

User-mode applications call [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) to send an I/O request directly to a specified kernel-mode driver. This request contains an I/O control code (IOCTL) or file system control code (FSCTL) and pointers to input and output data buffers. The format of these data buffers is specific to the IOCTL or FSCTL, which in turn is defined by the kernel-mode driver. Because the buffer format is arbitrary, and because it is known to the driver and not WOW64, the task of thunking the data is left to the driver.

Your 64-bit driver must support 32-bit I/O if all of the following are true:

-   The driver exposes an IOCTL (or FSCTL) to user-mode applications.

-   At least one of the I/O buffers used by the IOCTL contains pointer-precision data types.

-   Your IOCTL code cannot easily be rewritten to eliminate the use of pointer-precision buffer data types.

 

