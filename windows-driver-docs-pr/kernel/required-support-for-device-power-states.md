---
title: Required Support for Device Power States
description: Required Support for Device Power States
ms.assetid: f7218f2a-d4ad-4b9a-af90-057801e714a2
keywords: ["continuous power WDK kernel", "delays WDK power management", "device power states WDK kernel", "hardware WDK power management", "legacy power management WDK kernel", "class drivers WDK power management", "port drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Required Support for Device Power States





Consult the relevant Device Class Power Management Reference Specification to find out which device power states are defined for the class of device with which you are working with and what the operational requirements are for each state. These specifications are available at the [ACPI / Power Management](http://go.microsoft.com/fwlink/p/?linkid=57185) website.

Legacy devices and other devices for which no power management specification exists should follow the Default Device Class Power Management Specification. The default specification requires:

-   Support for the D0 and D3 states.

-   A driver that saves and restores or reinitializes device context when the device is powered on.

-   A driver that manages the device power policy.

Class and port drivers supplied with the system and by independent hardware vendors (IHVs) typically support power management. If you are writing a minidriver that links to such a driver, check the relevant class or port driver documentation in the Windows Driver Kit (WDK) to find out the extent of power management support required in the minidriver. The following general guidelines apply:

-   A network adapter driver must conform to the Network Driver Interface Specification 6.00 (NDIS 6.0) (Windows Vista) or to NDIS 5.0 (Windows Server 2003, Windows XP, and Windows 2000). In addition, the driver must conform to the power management requirements for the device setup class of the driver and the Windows version of the driver.

-   Streaming drivers use the power management interfaces in the streaming class driver to handle device power states D0 and D3. To handle device power states D1 and D2, these drivers must use the power management interfaces described in this section.

-   The SCSI port driver manages most of the PnP and power management requirements for the miniport. SCSI miniport drivers must support PnP and power management interfaces along with related routines such as [**HwScsiAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557274).

-   The video port driver manages most of the PnP and power management requirements for the miniport. Video miniport drivers must support miniport-specific routines, which are described elsewhere in the WDK.

 

 




