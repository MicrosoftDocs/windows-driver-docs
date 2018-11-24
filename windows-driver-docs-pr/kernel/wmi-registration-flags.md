---
title: WMI Registration Flags
description: WMI Registration Flags
ms.assetid: 001d4840-0ed4-464d-8379-7bbd0afce28c
keywords: ["dynamic instance names WDK WMI", "static instance names WDK WMI", "registration flags WDK WMI", "flags WDK WMI", "WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI", "registering blocks"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI Registration Flags





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

 

 




