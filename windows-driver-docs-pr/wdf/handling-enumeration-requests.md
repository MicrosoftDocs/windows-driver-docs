---
title: Handling Enumeration Requests
description: Handling Enumeration Requests
keywords:
- enumeration WDK KMDF
- PnP WDK KMDF , bus enumeration
- Plug and Play WDK KMDF , bus enumeration
- bus enumeration WDK KMDF
- listing child devices WDK KMDF
- child devices WDK KMDF
- dynamic enumeration WDK KMDF
- static enumeration WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Enumeration Requests


The PnP manager can request a bus driver to enumerate its children at any time. (If you are familiar with WDM interfaces, enumeration requests are [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](../kernel/irp-mn-query-device-relations.md) requests with a relation type of **BusRelations**.) Framework-based drivers do not see these requests. Instead, the framework handles the requests by using the information that is stored in a device's child list. The driver is responsible for keeping the child list up-to-date so that the framework can provide correct information when the PnP manager requests an enumeration.

Framework-based bus drivers that support dynamic enumeration can receive a request to reenumerate a particular child device. Such a request might be sent by the child device's function driver after the driver detects a device failure. (The framework supports this type of request by implementing the [**REENUMERATE\_SELF\_INTERFACE\_STANDARD**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reenumerate_self_interface_standard) interface, which is a standard [driver-defined interface](using-driver-defined-interfaces.md) that is defined in *wdm.h*.)

Framework-based bus drivers that support dynamic enumeration can provide an [*EvtChildListDeviceReenumerated*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_device_reenumerated) callback function, which the framework calls when it receives a reenumeration request from a child device's driver. If this callback function returns **TRUE** or does not exist, the framework marks the child device as no longer being present and informs the PnP manager that the bus driver's child list has changed. As a result, the PnP manager requests a reenumeration and the framework calls the driver's [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function, which creates a new PDO for the child device.

 

