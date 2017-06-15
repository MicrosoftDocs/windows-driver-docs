---
title: Updating WMI Registration Information
author: windows-driver-content
description: Updating WMI Registration Information
MS-HAID:
- 'WMI\_03880ad4-5efe-48e5-ac0c-a47129c310c4.xml'
- 'kernel.updating\_wmi\_registration\_information'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d24688e5-bb50-4bce-a4d4-4a3bf886f86d
keywords: ["WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI", "registering blocks", "updating WMI registration information"]
---

# Updating WMI Registration Information


## <a href="" id="ddk-updating-wmi-registration-information-kg"></a>


After its initial registration with WMI, a driver changes its registration information by calling [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480) with one of the following actions:

-   WMIREG\_ACTION\_REREGISTER to replace all registration information previously supplied by the driver with new information.

    In response, WMI sends either an [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) request or an [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request to the driver, with **Parameters.WMI.DataPath** set to WMIREGISTER. (On Windows 98 and Windows 2000, the system sends the **IRP\_MN\_REGINFO** request. On Windows XP and later, the system sends the **IRP\_MN\_REGINFO\_EX** request.)

    The driver supplies WMI with new registration information for all blocks it supports, as described in [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md) and [Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks](handling-irp-mn-reginfo-and-irp-mn-reginfo-ex-to-register-blocks.md).

-   WMIREG\_ACTION\_UPDATE\_GUIDS to add or remove support for blocks or to change the static instance names of registered blocks.

    In response, WMI sends an [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request to the driver, with **Parameters.Wmi.DataPath** set to WMIUPDATE.

    The driver supplies WMI with an updated registration information in which:

    -   The driver sets WMIREG\_FLAG\_REMOVE\_GUID to remove support for that block.

    -   The driver clears WMIREG\_FLAG\_REMOVE\_GUID to add a new block or update an existing block.

    -   The driver sets or clears WMIREG\_FLAG\_INSTANCE\_*XXX* and supplies any necessary instance name information to change a block's static instance names or change it to use dynamic instance names.

-   WMIREG\_ACTION\_DEREGISTER to instruct WMI that the driver will no longer provide WMI information.

    WMI does not send an **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** request in response to this call, because it requires no further information from the driver. A driver typically deregisters its blocks in response to an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request. Note that the deregister call will block until all WMI IRPs to the device have been completed. If a driver queues WMI IRPs, it must cancel them before calling [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480) to deregister.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Updating%20WMI%20Registration%20Information%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


