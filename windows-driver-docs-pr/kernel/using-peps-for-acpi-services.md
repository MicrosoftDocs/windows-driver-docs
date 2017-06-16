---
title: Using PEPs for ACPI services
author: windows-driver-content
description: This topic provides information about using platform extension plug-ins (PEPs) for ACPI services.
ms.assetid: 80ED3B80-A1FF-4A41-BA88-EC1C832C4639
---

# Using PEPs for ACPI services


This topic provides information about using platform extension plug-ins (PEPs) for ACPI services.

PEPs provide dynamic, runtime ACPI methods. The static tables (FADT, MADT, DBG2, etc.) must be implemented in the ACPI firmware, as well as the DSDT/SSDT device hierarchy.

PEPs are intended to be used for off-SoC power management methods. Since they are installable binaries, they can be updated on-the-fly as opposed to ACPI firmware which requires a firmware flash. This means you could improve your power management code on platforms that you’ve already shipped by posting an updated driver on Windows Update. Power management was the original intent for PEPs, but they can be used to provide or override any arbitrary ACPI runtime method.

PEPs play no role in the construction of the ACPI namespace hierarchy because the namespace hierarchy must be provided in the firmware DSDT. When the ACPI driver evaluates a method at runtime, it will check against the PEP’s implemented methods for the device in question, and, if present, it will execute the PEP and ignore the firmware’s version. However, the device itself must be defined in the firmware.

Providing power management using PEPs can be much easier to debug than code written for the ACPI firmware because of the tools available. Tools for debugging ACPI firmware are unfamiliar to most and tool options are limited. In contrast, PEPs are developed as Windows drivers so developers can use whatever development and debugging tools they are most comfortable with.

When using a PEP in place of an ACPI service, no special action or operation is needed in order to claim the role of the service. When a method is implemented in the PEP, Windows will use it automatically. If a firmware version of the same method on the same device is provided, it will be ignored.

PEPs are loaded very early so that their services are available for the device driver. Additionally, the abstraction layer through Windows is designed to be transparent to device drivers. The driver should expect to be able to interact with its ACPI methods as if a PEP weren't in use.

When using PEP for both device power management (DPM) and ACPI services, it's advisable to use separate PEP handles, but this is only a matter of preference. When sharing the handle DPM and ACPI state can be tracked easily for a device because the handle is the same. However, handle lifetime management is a little more complicated. The PEP will need to provide reference counting for the handle to make sure it is only deleted after both DPM and ACPI services have been torn down for that handle (i.e., both [**PEP\_DPM\_UNREGISTER\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt186742) and [**PEP\_NOTIFY\_ACPI\_UNREGISTER\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt186758) have been received on that handle). When different handles are used, DPM and ACPI state will be tracked separately, but handle lifetime management is simpler. In this case, the handle can be destroyed when the corresponding unregister notification is sent.

To simplify the process of working with ACPI resources, the power management framework (PoFx) provides the PEP\_REQUEST\_COMMON\_ACPI\_CONVERT\_TO\_BIOS\_RESOURCES helper routine to convert ACPI resources to BIOS resources.

PEPs are responsible for scheduling work that cannot be performed synchronously in response to an ACPI notification from PoFx but the method used is determined by the PEP developer. Typically, the PEP will queue the work on some internal queue and then start a worker thread if needed. It is also possible that the work needs to wait for some external event (e.g. device interrupt) and will be processed in the context of that event. Once the work is done, a PEP can request PoFx to query for work by invoking [**PEP\_KERNEL\_INFORMATION\_STRUCT\_V3**](https://msdn.microsoft.com/library/windows/hardware/mt186747)-&gt;[*RequestWorker*](https://msdn.microsoft.com/library/windows/hardware/mt186884)(). In response, PoFx will send a [**PEP\_DPM\_WORK notification**](https://msdn.microsoft.com/library/windows/hardware/mt186743) for PEPs that implement the DPM notification handler ([*AcceptDeviceNotification*](https://msdn.microsoft.com/library/windows/hardware/mt186626)) or a [**PEP\_NOTIFY\_ACPI\_WORK notification**](https://msdn.microsoft.com/library/windows/hardware/mt188089) for PEPs that implement the ACPI-only notification handler ([*AcceptAcpiNotification*](https://msdn.microsoft.com/library/windows/hardware/mt186625)).

## Related topics
[ACPI system description tables](https://msdn.microsoft.com/library/Dn495660.aspx)  
[**PEP\_DPM\_UNREGISTER\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt186742)  
[**PEP\_NOTIFY\_ACPI\_UNREGISTER\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt186758)  
[**PEP\_KERNEL\_INFORMATION\_STRUCT\_V3**](https://msdn.microsoft.com/library/windows/hardware/mt186747)  
[**PEP\_DPM\_WORK**](https://msdn.microsoft.com/library/windows/hardware/mt186743)  
[**PEP\_NOTIFY\_ACPI\_WORK**](https://msdn.microsoft.com/library/windows/hardware/mt188089)  
[*RequestWorker*](https://msdn.microsoft.com/library/windows/hardware/mt186884)  
[*AcceptDeviceNotification*](https://msdn.microsoft.com/library/windows/hardware/mt186626)  
[ACPI notifications](https://msdn.microsoft.com/library/windows/hardware/mt186628)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20PEPs%20for%20ACPI%20services%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


