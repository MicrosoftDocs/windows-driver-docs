---
title: Windows Kernel-Mode WMI Library
author: windows-driver-content
description: Windows Kernel-Mode WMI Library
MS-HAID:
- 'wmilib\_f500781e-2b62-4e45-b113-26bb1787a51b.xml'
- 'kernel.windows\_kernel\_mode\_wmi\_library'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ca981f38-8f3b-48cc-969f-ce53b85bba20
---

# Windows Kernel-Mode WMI Library


Windows provides a general mechanism for managing components. This system is called Windows Management Instrumentation (WMI). To satisify Windows Driver Model (WDM) requirements, you should implement WMI for your driver so that your driver can be managed by the system.

For more information on WMI, see [Windows Management Instrumentation](implementing-wmi.md).

Routines that provide a direct interface to the WMI library are prefixed with the letters "**Wmi**"; for a list of WMI routines, see [Windows Management Instrumentation (WMI) Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff566359).

For a list of WMI callbacks, see [WMI Library Callback Routines](https://msdn.microsoft.com/library/windows/hardware/ff566357).

Communication with WMI is done with IRPs. For a list of routines that your driver can use to receive IRPs, see [WMI IRP Processing Routines](https://msdn.microsoft.com/library/windows/hardware/ff566353). For a list of routines that your driver can use to send WMI IRPs, see [WMI IRP Sending Routines](https://msdn.microsoft.com/library/windows/hardware/ff566355). For a list of IRPs that are used with WMI, see [WMI Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff566361).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20WMI%20Library%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


