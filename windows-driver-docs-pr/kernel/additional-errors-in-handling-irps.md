---
title: Additional Errors in Handling IRPs
author: windows-driver-content
description: Additional Errors in Handling IRPs
MS-HAID:
- 'Other\_58022006-b18a-48cc-8548-3e6c7bfcbb83.xml'
- 'kernel.additional\_errors\_in\_handling\_irps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fb46e7a8-8181-46d3-a929-cec01fd71f20
keywords: ["reliability WDK kernel , double-completed IRPs", "double-completed IRPs WDK kernel", "lost IRPs WDK kernel", "reliability WDK kernel , lost IRPs", "converging public IOCTL and private IOCTL paths", "reliability WDK kernel , converge public and private IOCTL paths"]
---

# Additional Errors in Handling IRPs


## <a href="" id="ddk-additional-errors-in-handling-irps-kg"></a>


The following are additional errors that drivers sometimes make when handling IRPs.

### Lost or double-completed IRPs

These problems, along with missing calls to I/O manager routines such as [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358), often occur in error-handling paths. Quick reviews of driver paths can find such problems.

### Converging public IOCTL and private IOCTL paths

As a general rule, drivers should contain separate execution paths for public and private IOCTLs (or FSCTLs). A driver cannot determine whether an IOCTL or FSCTL request originates in kernel mode or user mode by looking at the control code. Consequently, handling both public and private codes in the same execution path (or performing minimal validation and then calling the same routines) can open a driver to security breaches. If a private IOCTL or FSCTL is privileged, then unprivileged users who know the control codes might be able to gain access to it. Therefore, if your driver supports private IOCTL or FSCTL requests, make sure it handles such requests separately from any public IOCTLs or FSCTLs it must also support.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Additional%20Errors%20in%20Handling%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


