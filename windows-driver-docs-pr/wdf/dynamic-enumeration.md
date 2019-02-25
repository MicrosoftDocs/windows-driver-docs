---
title: Dynamic Enumeration
description: Dynamic Enumeration
ms.assetid: 6e46b456-7d2d-4c6e-8692-7f310366387d
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

Each time a driver creates a framework device object that represents an FDO for a device, the framework creates an empty, default child list for the device. Your driver can obtain a handle to a device's default child list by calling [**WdfFdoGetDefaultChildList**](https://msdn.microsoft.com/library/windows/hardware/ff547235). Typically, if you are writing a bus driver that enumerates a device's children, your driver can add children to the default child list. If you need to create additional child lists, your driver can call [**WdfChildListCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545615).

Before a driver can use a child list, it must configure the child-list object by initializing a [**WDF\_CHILD\_LIST\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551227) structure and passing the structure to either [**WdfFdoInitSetDefaultChildListConfig**](https://msdn.microsoft.com/library/windows/hardware/ff547258), for the default child list, or to [**WdfChildListCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545615), for additional child lists.

### Dynamic Child Descriptions

Each time a bus driver identifies a child device, it must add the child device's description to a child list. A *child description* consists of a required *identification description* and an optional *address description*.

<a href="" id="identification-description"></a>*Identification Description*  
An identification description is a structure that contains information that uniquely identifies each device that the driver enumerates. The driver defines this structure, but its first member must be a [**WDF\_CHILD\_IDENTIFICATION\_DESCRIPTION\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff551223) structure.

Typically, an identification description contains a device's [device identification strings](https://msdn.microsoft.com/library/windows/hardware/ff541224), possibly a serial number, and information about the device's location on the bus, such as a slot number.

The driver can provide the following set of callback functions, which allow the framework to manipulate the information in an identification description:

-   [*EvtChildListIdentificationDescriptionCompare*](https://msdn.microsoft.com/library/windows/hardware/ff540833), which compares the contents of two identification description structures.

-   [*EvtChildListIdentificationDescriptionCopy*](https://msdn.microsoft.com/library/windows/hardware/ff540834), which copies the contents of one identification description structure to another.

-   [*EvtChildListIdentificationDescriptionDuplicate*](https://msdn.microsoft.com/library/windows/hardware/ff540836), which creates a new identification description by duplicating an existing identification description structure and, if necessary, allocating additional buffers.

-   [*EvtChildListIdentificationDescriptionCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540832), which deallocates buffers that were allocated by the [*EvtChildListIdentificationDescriptionDuplicate*](https://msdn.microsoft.com/library/windows/hardware/ff540836) callback function.

Typically, you will need to provide these callback functions if your driver's identification description structures contain pointers to dynamically allocated buffers. For more information about the purpose of these callback functions, see their reference pages.

<a href="" id="address-description"></a>*Address Description*  
An address description is a structure that contains information that the driver requires so that it can access the device on its bus, if the information can change while the device is plugged in. The driver defines this structure, but its first member must be a [**WDF\_CHILD\_ADDRESS\_DESCRIPTION\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff551219) structure.

Address descriptions are optional. If a device's address information cannot change between the time the device is plugged in and the time it is unplugged, all of the device's address information can be stored in an identification description. For example, USB controllers assign addresses to devices when the devices are plugged in, and these addresses do not change.

On the other hand, some buses use addressing information that can change. For example, the IEEE 1394 bus uses a "generation count," which is the number of bus resets that have occurred. Each asynchronous I/O request to an IEEE 1394 device must include the generation count. Because this address information can change, your driver must store it in an address description.

The driver can provide the following set of callback functions to manipulate the information in an address description:

-   [*EvtChildListAddressDescriptionCopy*](https://msdn.microsoft.com/library/windows/hardware/ff540824), which copies the contents of one address description structure to another.

-   [*EvtChildListAddressDescriptionDuplicate*](https://msdn.microsoft.com/library/windows/hardware/ff540826), which creates a new address description by duplicating an existing address description structure and, if necessary, allocating additional buffers.

-   [*EvtChildListAddressDescriptionCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540823), which deallocates buffers that were allocated by the [*EvtChildListAddressDescriptionDuplicate*](https://msdn.microsoft.com/library/windows/hardware/ff540826) callback function.

Typically, you will need to provide these callback functions if your driver's address description structures contain pointers to dynamically allocated buffers. For more information about the purpose of these callback functions, see their reference pages.

### Adding Devices to a Dynamic Child List

When the framework calls a bus driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, the callback function must call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create an FDO for the parent device, which is typically a bus adapter. For more information about creating an FDO, see [Creating Device Objects in a Function Driver](creating-device-objects-in-a-function-driver.md). The driver must then enumerate the parent device's children and add the children to a child list.

Optionally, the driver can call [**WdfDeviceSetBusInformationForChildren**](https://msdn.microsoft.com/library/windows/hardware/ff546868) to provide the framework with information about the bus. Doing so is recommended because it makes it easier for child devices and apps to identify the bus.

To add children to a child list, the driver must call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591) for each child device that it finds. This call informs the framework that a driver has discovered a child device that is connected to a parent device. When your driver calls **WdfChildListAddOrUpdateChildDescriptionAsPresent**, it supplies an identification description and, optionally, an address description.

After the driver calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591) to report a new device, the framework informs the PnP manager that the new device exists. The PnP manager then builds a device stack and driver stack for the new device. As part of this process, the framework calls the bus driver's [*EvtChildListCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540828) callback function. This callback function must call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a PDO for the new device.

Typically, several child devices are connected to a parent, so the bus driver will need to call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591) several times. The most efficient way to do this is the following:

1.  Call [**WdfChildListBeginScan**](https://msdn.microsoft.com/library/windows/hardware/ff545608).

2.  Call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591) for each child device.

3.  Call [**WdfChildListEndScan**](https://msdn.microsoft.com/library/windows/hardware/ff545626).

If you surround your driver's dynamic enumeration with calls to [**WdfChildListBeginScan**](https://msdn.microsoft.com/library/windows/hardware/ff545608) and [**WdfChildListEndScan**](https://msdn.microsoft.com/library/windows/hardware/ff545626), the framework stores all of the changes to the child list, and notifies the PnP manager of the changes when the driver calls **WdfChildListEndScan**. At some later time, the framework calls the bus driver's [*EvtChildListCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540828) callback function for each device in the child list. This callback function calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a PDO for each new device.

When your driver calls [**WdfChildListBeginScan**](https://msdn.microsoft.com/library/windows/hardware/ff545608), the framework marks all previously reported devices as no longer being present. Therefore, the driver must call [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591) for all children that the driver can detect, not just newly discovered children. To add a single child to a child list, the driver can make a single call to [**WdfChildListUpdateAllChildDescriptionsAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545667) without first calling **WdfChildListBeginScan**.

### Updating a Dynamic Child List

There are two common ways to update the information in a dynamic child list:

1.  When a parent device receives an interrupt that indicates the arrival or removal of a child, the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591) if a device has been plugged in or [**WdfChildListUpdateChildDescriptionAsMissing**](https://msdn.microsoft.com/library/windows/hardware/ff545674) if a device has been unplugged.

2.  The driver can provide an [*EvtChildListScanForChildren*](https://msdn.microsoft.com/library/windows/hardware/ff540838) callback function, which the framework calls each time the parent device enters its working (D0) state. This callback function should enumerate all child devices by calling [**WdfChildListBeginScan**](https://msdn.microsoft.com/library/windows/hardware/ff545608), [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591) (or [**WdfChildListUpdateAllChildDescriptionsAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545667)), and [**WdfChildListEndScan**](https://msdn.microsoft.com/library/windows/hardware/ff545626).

You can use one or both of these techniques in your driver.

### Traversing a Dynamic Child List

If you want your driver to examine the contents of a child list, it can traverse the list by using one of the following techniques:

-   To obtain the contents of each child device description, one at a time, the driver can:

    1.  Call [**WdfChildListBeginIteration**](https://msdn.microsoft.com/library/windows/hardware/ff545601).
    2.  Call [**WdfChildListRetrieveNextDevice**](https://msdn.microsoft.com/library/windows/hardware/ff545655), as many times as necessary.
    3.  Call [**WdfChildListEndIteration**](https://msdn.microsoft.com/library/windows/hardware/ff545618).

    When calling [**WdfChildListBeginIteration**](https://msdn.microsoft.com/library/windows/hardware/ff545601), the driver specifies a [**WDF\_RETRIEVE\_CHILD\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff552507)-typed flag that indicates whether the framework should retrieve all device descriptions or only a subset. When [**WdfChildListRetrieveNextDevice**](https://msdn.microsoft.com/library/windows/hardware/ff545655) finds a match, it retrieves the child device's identification and address descriptions, plus a handle to its device object.

-   If you need to obtain the address description that is currently contained in a child device description, your driver can call [**WdfChildListRetrieveAddressDescription**](https://msdn.microsoft.com/library/windows/hardware/ff545648), specifying an identification description. The framework traverses the child list until it finds a child device with a matching identification description, and then it retrieves the address description.

-   If you need to obtain a handle to the framework device object that is associated with a particular child device, your driver can call [**WdfChildListRetrievePdo**](https://msdn.microsoft.com/library/windows/hardware/ff545663). The framework traverses the child list until it finds a child device with a matching identification description, and then it returns a device object handle.

### Accessing a PDO's Identification and Address Descriptions

Your driver can call the following methods to access a PDO's identification description or address description:

-   [**WdfPdoRetrieveIdentificationDescription**](https://msdn.microsoft.com/library/windows/hardware/ff548824), which retrieves the identification description that is associated with a PDO.

-   [**WdfPdoRetrieveAddressDescription**](https://msdn.microsoft.com/library/windows/hardware/ff548820), which retrieves the address description that is associated with a PDO.

-   [**WdfPdoUpdateAddressDescription**](https://msdn.microsoft.com/library/windows/hardware/ff548826), which updates the address description that is associated with a PDO.

 

 





