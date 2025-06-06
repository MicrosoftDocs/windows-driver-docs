---
title: Introduction to I/O Control Codes
description: Provides an introduction to I/O control codes.
keywords: ["I/O control codes WDK kernel , about I/O control codes", "control codes WDK IOCTLs , about I/O control codes", "IOCTLs WDK kernel , about I/O control codes", "private IOCTLs WDK kernel", "public IOCTLs WDK kernel", "IOCTLs WDK user-mode", "user-mode components WDK IOCTLs", "I/O control codes WDK user-mode", "control codes WDK user-mode"]
ms.date: 02/21/2025
ms.topic: concept-article
---

# Introduction to I/O control codes

I/O control codes (IOCTLs) are used for communication between user-mode applications and drivers, or for communication internally among drivers in a stack. I/O control codes are sent using IRPs.

User-mode applications send IOCTLs to drivers by calling [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), which is described in Microsoft Windows SDK documentation. Calls to **DeviceIoControl** cause the I/O manager to create an [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md) request and send it to the topmost driver.

Additionally, upper-level drivers can send IOCTLs to lower-level drivers by creating and sending **IRP_MJ_DEVICE_CONTROL** or [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](./irp-mj-internal-device-control.md) requests. Drivers process these requests in [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and [*DispatchInternalDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines. (User-mode applications can't send **IRP_MJ_INTERNAL_DEVICE_CONTROL** requests.)

Some IOCTLs are public and some are private. Public IOCTLs are typically system-defined and documented by Microsoft, in either the Windows Driver Kit (WDK) or the Windows SDK. They might be sent with a user-mode component's calls to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), or they might be sent from one kernel-mode driver to another, using **IRP_MJ_DEVICE_CONTROL** or **IRP_MJ_INTERNAL_DEVICE_CONTROL** requests. 

Private IOCTLs, on the other hand, are meant to be used exclusively by a vendor's software components to communicate with each other. Private IOCTLs are typically defined in a vendor-supplied header file and aren't publicly documented. Like public IOCTLs, they might be sent with a user-mode component's calls to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), or they might be sent from one kernel-mode driver to another, using **IRP_MJ_DEVICE_CONTROL** or **IRP_MJ_INTERNAL_DEVICE_CONTROL** requests.

There's no difference between the coding of public and private IOCTLs. There are, however, differences in the internal codes that can be used in vendor-defined IOCTLs, compared with those that are used for system-defined IOCTLs. If the available public IOCTLs don't fit your needs, you can define new private IOCTLs that your software components can use to communicate with one another. For more information, see [Defining I/O Control Codes](defining-i-o-control-codes.md).
