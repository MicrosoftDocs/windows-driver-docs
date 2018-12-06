---
title: Introduction to I/O Control Codes
description: Introduction to I/O Control Codes
ms.assetid: 8b9e09ef-56f9-42b9-9b65-04bc380f3a1e
keywords: ["I/O control codes WDK kernel , about I/O control codes", "control codes WDK IOCTLs , about I/O control codes", "IOCTLs WDK kernel , about I/O control codes", "private IOCTLs WDK kernel", "public IOCTLs WDK kernel", "IOCTLs WDK user-mode", "user-mode components WDK IOCTLs", "I/O control codes WDK user-mode", "control codes WDK user-mode"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to I/O Control Codes





I/O control codes (IOCTLs) are used for communication between user-mode applications and drivers, or for communication internally among drivers in a stack. I/O control codes are sent using IRPs.

User-mode applications send IOCTLs to drivers by calling [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), which is described in Microsoft Windows SDK documentation. Calls to **DeviceIoControl** cause the I/O manager to create an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request and send it to the topmost driver.

Additionally, upper-level drivers can send IOCTLs to lower-level drivers by creating and sending **IRP\_MJ\_DEVICE\_CONTROL** or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests. Drivers process these requests in [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) and [*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326) routines. (User-mode applications cannot send **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests.)

Some IOCTLs are "public" and some are "private". Public IOCTLs are typically system-defined and documented by Microsoft, in either the Windows Driver Kit (WDK) or the Windows SDK. They might be sent by means of a user-mode component's calls to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), or they might be sent from one kernel-mode driver to another, using **IRP\_MJ\_DEVICE\_CONTROL** or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. Examples of public IOCTLs include [SCSI Port I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565367) and [I8042prt Mouse Internal Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff539982).

Private IOCTLs, on the other hand, are meant to be used exclusively by a vendor's software components to communicate with each other. Private IOCTLs are typically defined in a vendor-supplied header file and are not publicly documented. Like public IOCTLs, they might be sent by means of a user-mode component's calls to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), or they might be sent from one kernel-mode driver to another, using **IRP\_MJ\_DEVICE\_CONTROL** or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests.

There is no difference between the coding of public and private IOCTLs. There are, however, differences in the internal codes that can be used in vendor-defined IOCTLs, compared with those that are used for system-defined IOCTLs. If the available public IOCTLs do not fit your needs, you can define new private IOCTLs that your software components can use to communicate with one another. For more information, see [Defining I/O Control Codes](defining-i-o-control-codes.md).

 

 




