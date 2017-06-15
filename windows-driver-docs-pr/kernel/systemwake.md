---
title: SystemWake
author: windows-driver-content
description: SystemWake
MS-HAID:
- 'PwrMgmt\_ffb2cc5a-3e30-4355-a2a1-a531525edcc5.xml'
- 'kernel.systemwake'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 77390637-bb92-4634-a407-9a409a8a8acd
keywords: ["SystemWake"]
---

# SystemWake


## <a href="" id="ddk-systemwake-kg"></a>


The **SystemWake** member of [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) contains the lowest (least-powered) system power state from which the device can wake the system, or **PowerSystemUnspecified** if the device cannot wake the system.

The bus driver sets this value at when it enumerates the device. A higher-level driver can change the value to a higher-powered state but cannot change it to a lower-powered state. For example, if the bus driver sets **SystemWake** to S3 but a driver further up the device stack supports wake-up only from S2, the higher-level driver can change the value to S2. If a driver changes **SystemWake**, it might also have to change [**DeviceWake**](devicewake.md), as explained in the next section.

Drivers rarely need to propagate changed values back down the device stack. Because changes make the device capabilities more restrictive, lower drivers do not see requests that they cannot handle. In the previous example, a higher-level driver fails any request to wake the system from a lower-powered state than S2, so lower drivers never see such a request. However, if a lower driver must be aware of any changes, it can send a PnP [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) to its own device stack during its processing of an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749).

If both the **SystemWake** and **DeviceWake** members are nonzero (that is, not **PowerSystemUnspecified**), then the device and its drivers support wake-up on this system.

On non-ACPI hardware, this member always contains zero (**PowerSystemUnspecified**).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20SystemWake%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


