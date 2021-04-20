---
title: Dynamic Enumeration
description: Dynamic Enumeration
keywords:
- dynamic enumeration WDK KMDF
- child descriptions WDK KMDF
- address descriptions WDK KMDF
- identification descriptions WDK KMDF
- dynamic child lists WDK KMDF
- traversing dynamic child lists WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamic Enumeration


*Dynamic enumeration* is a driver's ability to detect and report changes to the number and type of devices that are connected to the system while the system is running.

Bus drivers must use dynamic enumeration if the number or types of devices that are connected to the parent device depend on a system's configuration. Some of these devices might be always connected to the system, and some might be plugged in and unplugged while the system is running.

For example, the number and type of devices that are plugged into a system's PCI bus are system-dependent, but they are permanent unless a user turns off power, opens the case, and adds or removes a device by using a screwdriver. On the other hand, a user can add or remove USB devices by plugging in or unplugging a cable while the system is running.

### Dynamic Child Lists

The framework enables drivers to support dynamic enumeration by providing framework child-list objects. Each child-list object represents a list of child devices that are connected to a parent device. The bus driver for the parent device must identify the parent's child devices, add them to the parent device's child list, and create a physical device object (PDO) for each child.

Each time a driver creates a framework device object that represents an FDO for a device, the framework creates an empty, default child list for the device. Your driver can obtain a handle to a device's default child list by calling [**WdfFdoGetDefaultChildList**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdogetdefaultchildlist). Typically, if you are writing a bus driver that enumerates a device's children, your driver can add children to the default child list. If you need to create additional child lists, your driver can call [**WdfChildListCreate**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistcreate).

Before a driver can use a child list, it must configure the child-list object by initializing a [**WDF\_CHILD\_LIST\_CONFIG**](/windows-hardware/drivers/ddi/wdfchildlist/ns-wdfchildlist-_wdf_child_list_config) structure and passing the structure to either [**WdfFdoInitSetDefaultChildListConfig**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitsetdefaultchildlistconfig), for the default child list, or to [**WdfChildListCreate**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistcreate), for additional child lists.

### Dynamic Child Descriptions

Each time a bus driver identifies a child device, it must add the child device's description to a child list. A *child description* consists of a required *identification description* and an optional *address description*.

<a href="" id="identification-description"></a>*Identification Description*
An identification description is a structure that contains information that uniquely identifies each device that the driver enumerates. The driver defines this structure, but its first member must be a [**WDF\_CHILD\_IDENTIFICATION\_DESCRIPTION\_HEADER**](/windows-hardware/drivers/ddi/wdfchildlist/ns-wdfchildlist-_wdf_child_identification_description_header) structure.

Typically, an identification description contains a device's [device identification strings](../install/device-identification-strings.md), possibly a serial number, and information about the device's location on the bus, such as a slot number.

The driver can provide the following set of callback functions, which allow the framework to manipulate the information in an identification description:

-   [*EvtChildListIdentificationDescriptionCompare*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_identification_description_compare), which compares the contents of two identification description structures.

-   [*EvtChildListIdentificationDescriptionCopy*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_identification_description_copy), which copies the contents of one identification description structure to another.

-   [*EvtChildListIdentificationDescriptionDuplicate*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_identification_description_duplicate), which creates a new identification description by duplicating an existing identification description structure and, if necessary, allocating additional buffers.

-   [*EvtChildListIdentificationDescriptionCleanup*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_identification_description_cleanup), which deallocates buffers that were allocated by the [*EvtChildListIdentificationDescriptionDuplicate*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_identification_description_duplicate) callback function.

Typically, you will need to provide these callback functions if your driver's identification description structures contain pointers to dynamically allocated buffers. For more information about the purpose of these callback functions, see their reference pages.

<a href="" id="address-description"></a>*Address Description*
An address description is a structure that contains information that the driver requires so that it can access the device on its bus, if the information can change while the device is plugged in. The driver defines this structure, but its first member must be a [**WDF\_CHILD\_ADDRESS\_DESCRIPTION\_HEADER**](/windows-hardware/drivers/ddi/wdfchildlist/ns-wdfchildlist-_wdf_child_address_description_header) structure.

Address descriptions are optional. If a device's address information cannot change between the time the device is plugged in and the time it is unplugged, all of the device's address information can be stored in an identification description. For example, USB controllers assign addresses to devices when the devices are plugged in, and these addresses do not change.

On the other hand, some buses use addressing information that can change. For example, the IEEE 1394 bus uses a "generation count," which is the number of bus resets that have occurred. Each asynchronous I/O request to an IEEE 1394 device must include the generation count. Because this address information can change, your driver must store it in an address description.

The driver can provide the following set of callback functions to manipulate the information in an address description:

-   [*EvtChildListAddressDescriptionCopy*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_address_description_copy), which copies the contents of one address description structure to another.

-   [*EvtChildListAddressDescriptionDuplicate*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_address_description_duplicate), which creates a new address description by duplicating an existing address description structure and, if necessary, allocating additional buffers.

-   [*EvtChildListAddressDescriptionCleanup*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_address_description_cleanup), which deallocates buffers that were allocated by the [*EvtChildListAddressDescriptionDuplicate*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_address_description_duplicate) callback function.

Typically, you will need to provide these callback functions if your driver's address description structures contain pointers to dynamically allocated buffers. For more information about the purpose of these callback functions, see their reference pages.

### Adding Devices to a Dynamic Child List

When the framework calls a bus driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function, the callback function must call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create an FDO for the parent device, which is typically a bus adapter. For more information about creating an FDO, see [Creating Device Objects in a Function Driver](creating-device-objects-in-a-function-driver.md). The driver must then enumerate the parent device's children and add the children to a child list.

Optionally, the driver can call [**WdfDeviceSetBusInformationForChildren**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetbusinformationforchildren) to provide the framework with information about the bus. Doing so is recommended because it makes it easier for child devices and apps to identify the bus.

To add children to a child list, the driver must call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) for each child device that it finds. This call informs the framework that a driver has discovered a child device that is connected to a parent device. When your driver calls **WdfChildListAddOrUpdateChildDescriptionAsPresent**, it supplies an identification description and, optionally, an address description.

After the driver calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) to report a new device, the framework informs the PnP manager that the new device exists. The PnP manager then builds a device stack and driver stack for the new device. As part of this process, the framework calls the bus driver's [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function. This callback function must call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a PDO for the new device.

Typically, several child devices are connected to a parent, so the bus driver will need to call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) several times. The most efficient way to do this is the following:

1.  Call [**WdfChildListBeginScan**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistbeginscan).

2.  Call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) for each child device.

3.  Call [**WdfChildListEndScan**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistendscan).

If you surround your driver's dynamic enumeration with calls to [**WdfChildListBeginScan**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistbeginscan) and [**WdfChildListEndScan**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistendscan), the framework stores all of the changes to the child list, and notifies the PnP manager of the changes when the driver calls **WdfChildListEndScan**. At some later time, the framework calls the bus driver's [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function for each device in the child list. This callback function calls [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a PDO for each new device.

When your driver calls [**WdfChildListBeginScan**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistbeginscan), the framework marks all previously reported devices as no longer being present. Therefore, the driver must call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) for all children that the driver can detect, not just newly discovered children. To add a single child to a child list, the driver can make a single call to [**WdfChildListUpdateAllChildDescriptionsAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistupdateallchilddescriptionsaspresent) without first calling **WdfChildListBeginScan**.

### Updating a Dynamic Child List

There are two common ways to update the information in a dynamic child list:

1.  When a parent device receives an interrupt that indicates the arrival or removal of a child, the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) if a device has been plugged in or [**WdfChildListUpdateChildDescriptionAsMissing**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistupdatechilddescriptionasmissing) if a device has been unplugged.

2.  The driver can provide an [*EvtChildListScanForChildren*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_scan_for_children) callback function, which the framework calls each time the parent device enters its working (D0) state. This callback function should enumerate all child devices by calling [**WdfChildListBeginScan**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistbeginscan), [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) (or [**WdfChildListUpdateAllChildDescriptionsAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistupdateallchilddescriptionsaspresent)), and [**WdfChildListEndScan**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistendscan).

You can use one or both of these techniques in your driver.

### Traversing a Dynamic Child List

If you want your driver to examine the contents of a child list, it can traverse the list by using one of the following techniques:

-   To obtain the contents of each child device description, one at a time, the driver can:

    1.  Call [**WdfChildListBeginIteration**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistbeginiteration).
    2.  Call [**WdfChildListRetrieveNextDevice**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistretrievenextdevice), as many times as necessary.
    3.  Call [**WdfChildListEndIteration**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistenditeration).

    When calling [**WdfChildListBeginIteration**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistbeginiteration), the driver specifies a [**WDF\_RETRIEVE\_CHILD\_FLAGS**](/windows-hardware/drivers/ddi/wdfchildlist/ne-wdfchildlist-_wdf_retrieve_child_flags)-typed flag that indicates whether the framework should retrieve all device descriptions or only a subset. When [**WdfChildListRetrieveNextDevice**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistretrievenextdevice) finds a match, it retrieves the child device's identification and address descriptions, plus a handle to its device object.

-   If you need to obtain the address description that is currently contained in a child device description, your driver can call [**WdfChildListRetrieveAddressDescription**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistretrieveaddressdescription), specifying an identification description. The framework traverses the child list until it finds a child device with a matching identification description, and then it retrieves the address description.

-   If you need to obtain a handle to the framework device object that is associated with a particular child device, your driver can call [**WdfChildListRetrievePdo**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistretrievepdo). The framework traverses the child list until it finds a child device with a matching identification description, and then it returns a device object handle. Be sure to wrap the call with [**WdfChildListBeginIteration**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistbeginiteration) and [**WdfChildListEndIteration**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistenditeration) to protect the caller from sudden PnP removal of the PDO on another thread.

### Accessing a PDO's Identification and Address Descriptions

Your driver can call the following methods to access a PDO's identification description or address description:

-   [**WdfPdoRetrieveIdentificationDescription**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoretrieveidentificationdescription), which retrieves the identification description that is associated with a PDO.

-   [**WdfPdoRetrieveAddressDescription**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoretrieveaddressdescription), which retrieves the address description that is associated with a PDO.

-   [**WdfPdoUpdateAddressDescription**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoupdateaddressdescription), which updates the address description that is associated with a PDO.

### Handling re-enumeration requests

Framework-based bus drivers that support dynamic enumeration can receive a request to reenumerate a particular child device through the [**REENUMERATE_SELF_INTERFACE_STANDARD**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reenumerate_self_interface_standard) interface. For more info, see [Handling Enumeration Requests](./handling-enumeration-requests.md)
