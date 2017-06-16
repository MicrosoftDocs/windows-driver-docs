---
title: WMI Registration Flags
author: windows-driver-content
description: WMI Registration Flags
ms.assetid: 001d4840-0ed4-464d-8379-7bbd0afce28c
keywords: ["dynamic instance names WDK WMI", "static instance names WDK WMI", "registration flags WDK WMI", "flags WDK WMI", "WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI", "registering blocks"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WMI Registration Flags


## <a href="" id="ddk-wmi-registration-flags-kg"></a>


A driver indicates whether a block uses static or dynamic instance names and specifies other characteristics of the block by setting flags in the [**WMIGUIDREGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff565811) or [**WMIREGGUID**](https://msdn.microsoft.com/library/windows/hardware/ff565827) structure that it passes to WMI to register the block.

A driver indicates that a block uses static instance names by setting one of the following flags:

-   WMIREG\_FLAG\_INSTANCE\_LIST indicates that the driver provides all instance names in a static list.

    A driver can set this flag only if it registers blocks by handling the [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) requests, not by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834). The driver writes the instance name strings at the byte offset indicated by **InstanceNameList** in the block's **WMIREGGUID** structure.

-   WMIREG\_FLAG\_INSTANCE\_BASENAME instructs WMI to generate static instance names from a driver-defined base name string.

    A driver that handles an **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** request writes the base name string at the offset indicated by **BaseNameOffset** in the block's **WMIREGGUID** structure.

    A driver that calls **WmiSystemControl** specifies the base name string in the *InstanceName* parameter of its [**DpWmiQueryReginfo**](https://msdn.microsoft.com/library/windows/hardware/ff544097) routine.

-   WMIREG\_FLAG\_INSTANCE\_PDO instructs WMI to generate static instance names from the device instance ID of the driver's PDO.

    A driver that handles an **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** request writes a pointer to the PDO at the **Pdo** member of the block's **WMIREGGUID** structure. If the request is **IRP\_MN\_REGINFO\_EX**, the driver must increase the reference count on each PDO passed by calling the [**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678) routine. (The system will dereference each PDO later.)

    A driver that calls **WmiSystemControl** writes a pointer to the PDO in the *Pdo* parameter of its [*DpWmiQueryReginfo*](https://msdn.microsoft.com/library/windows/hardware/ff544097) routine.

To indicate that a block uses dynamic instance names, the driver must not set any of the following flags: WMIREG\_FLAG\_INSTANCE\_LIST, WMIREG\_FLAG\_INSTANCE\_PDO, or WMIREG\_FLAG\_INSTANCE\_BASENAME.

A driver indicates that a data block is expensive to collect by setting WMIREG\_FLAG\_EXPENSIVE. This instructs WMI to send an [**IRP\_MN\_ENABLE\_COLLECTION**](https://msdn.microsoft.com/library/windows/hardware/ff550857) request the first time a WMI client opens the data block and an [**IRP\_MN\_DISABLE\_COLLECTION**](https://msdn.microsoft.com/library/windows/hardware/ff550848) request when the last WMI client closes the block. The driver need not collect data for such a block until it receives an **IRP\_MN\_ENABLE\_COLLECTION** request.

A driver indicates an event block by setting WMIREG\_FLAG\_EVENT\_ONLY\_GUID. This indicates that the block can be enabled or disabled as an event only, and cannot be queried or set.

A driver instructs WMI to remove a previously registered block by setting WMIREG\_FLAG\_REMOVE\_GUID. This flag is valid only in response to a request to update registration information ([**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) with WMIUPDATE). For more information, see [Updating WMI Registration Information](updating-wmi-registration-information.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Registration%20Flags%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


