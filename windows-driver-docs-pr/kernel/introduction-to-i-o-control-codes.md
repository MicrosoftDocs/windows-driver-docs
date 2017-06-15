---
title: Introduction to I/O Control Codes
author: windows-driver-content
description: Introduction to I/O Control Codes
MS-HAID:
- 'IRPs\_b179b00f-b7d2-4aee-ad19-490615f38d00.xml'
- 'kernel.introduction\_to\_i\_o\_control\_codes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8b9e09ef-56f9-42b9-9b65-04bc380f3a1e
keywords: ["I/O control codes WDK kernel , about I/O control codes", "control codes WDK IOCTLs , about I/O control codes", "IOCTLs WDK kernel , about I/O control codes", "private IOCTLs WDK kernel", "public IOCTLs WDK kernel", "IOCTLs WDK user-mode", "user-mode components WDK IOCTLs", "I/O control codes WDK user-mode", "control codes WDK user-mode"]
---

# Introduction to I/O Control Codes


## <a href="" id="ddk-introduction-to-i-o-control-codes-kg"></a>


I/O control codes (IOCTLs) are used for communication between user-mode applications and drivers, or for communication internally among drivers in a stack. I/O control codes are sent using IRPs.

User-mode applications send IOCTLs to drivers by calling [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), which is described in Microsoft Windows SDK documentation. Calls to **DeviceIoControl** cause the I/O manager to create an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request and send it to the topmost driver.

Additionally, upper-level drivers can send IOCTLs to lower-level drivers by creating and sending **IRP\_MJ\_DEVICE\_CONTROL** or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests. Drivers process these requests in [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) and [*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326) routines. (User-mode applications cannot send **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests.)

Some IOCTLs are "public" and some are "private". Public IOCTLs are typically system-defined and documented by Microsoft, in either the Windows Driver Kit (WDK) or the Windows SDK. They might be sent by means of a user-mode component's calls to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), or they might be sent from one kernel-mode driver to another, using **IRP\_MJ\_DEVICE\_CONTROL** or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. Examples of public IOCTLs include [SCSI Port I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565367) and [I8042prt Mouse Internal Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff539982).

Private IOCTLs, on the other hand, are meant to be used exclusively by a vendor's software components to communicate with each other. Private IOCTLs are typically defined in a vendor-supplied header file and are not publicly documented. Like public IOCTLs, they might be sent by means of a user-mode component's calls to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), or they might be sent from one kernel-mode driver to another, using **IRP\_MJ\_DEVICE\_CONTROL** or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests.

There is no difference between the coding of public and private IOCTLs. There are, however, differences in the internal codes that can be used in vendor-defined IOCTLs, compared with those that are used for system-defined IOCTLs. If the available public IOCTLs do not fit your needs, you can define new private IOCTLs that your software components can use to communicate with one another. For more information, see [Defining I/O Control Codes](defining-i-o-control-codes.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20I/O%20Control%20Codes%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


