---
title: Handling Enumeration Requests
description: Handling Enumeration Requests
ms.assetid: 3719ffa7-2daf-4716-a183-531837be99aa
keywords: ["enumeration WDK KMDF", "PnP WDK KMDF , bus enumeration", "Plug and Play WDK KMDF , bus enumeration", "bus enumeration WDK KMDF", "listing child devices WDK KMDF", "child devices WDK KMDF", "dynamic enumeration WDK KMDF", "static enumeration WDK KMDF"]
---

# Handling Enumeration Requests


The PnP manager can request a bus driver to enumerate its children at any time. (If you are familiar with WDM interfaces, enumeration requests are [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) requests with a relation type of **BusRelations**.) Framework-based drivers do not see these requests. Instead, the framework handles the requests by using the information that is stored in a device's child list. The driver is responsible for keeping the child list up-to-date so that the framework can provide correct information when the PnP manager requests an enumeration.

Framework-based bus drivers that support dynamic enumeration can receive a request to reenumerate a particular child device. Such a request might be sent by the child device's function driver after the driver detects a device failure. (The framework supports this type of request by implementing the [**REENUMERATE\_SELF\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff560839) interface, which is a standard [driver-defined interface](using-driver-defined-interfaces.md) that is defined in *wdm.h*.)

Framework-based bus drivers that support dynamic enumeration can provide an [*EvtChildListDeviceReenumerated*](https://msdn.microsoft.com/library/windows/hardware/ff540830) callback function, which the framework calls when it receives a reenumeration request from a child device's driver. If this callback function returns **TRUE** or does not exist, the framework marks the child device as no longer being present and informs the PnP manager that the bus driver's child list has changed. As a result, the PnP manager requests a reenumeration and the framework calls the driver's [*EvtChildListCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540828) callback function, which creates a new PDO for the child device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20Enumeration%20Requests%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




