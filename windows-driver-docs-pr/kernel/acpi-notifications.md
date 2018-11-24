---
title: ACPI notifications
description: Each ACPI notification that the PEP's AcceptAcpiNotification callback routine receives is accompanied by a Notification parameter that indicates the type of notification, and a Data parameter.
ms.assetid: E4DD4386-8008-463B-B048-DE8E559A7456
keywords: [AcceptAcpiNotification]
ms.date: 01/17/2018
ms.localizationpriority: medium
---

# ACPI notifications

Each ACPI notification that the PEP's AcceptAcpiNotification callback routine receives is accompanied by a Notification parameter that indicates the type of notification, and a Data parameter that points to a data structure that contains the information for the specified notification type.

In this call, the Notification parameter is set to a PEP_NOTIFY_ACPI_XXX constant value that indicates the notification type. The Data parameter points to a PEP_ACPI_XXX structure type that is associated with this notification type.

The following ACPI notification IDs are used by the AcceptAcpiNotification callback routine.

|Notification ID |Value |Associated structure|
|---|---|---| 
|PEP_NOTIFY_ACPI_PREPARE_DEVICE| 0x01 |PEP_ACPI_PREPARE_DEVICE| 
|PEP_NOTIFY_ACPI_ABANDON_DEVICE |0x02 |PEP_ACPI_ABANDON_DEVICE |
|PEP_NOTIFY_ACPI_REGISTER_DEVICE |0x03 |PEP_ACPI_REGISTER_DEVICE |
|PEP_NOTIFY_ACPI_UNREGISTER_DEVICE |0x04 |PEP_ACPI_UNREGISTER_DEVICE |
|PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE |0x05 |PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE |
|PEP_NOTIFY_ACPI_QUERY_OBJECT_INFORMATION |0x06 |PEP_ACPI_QUERY_OBJECT_INFORMATION |
|PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD |0x07 |PEP_ACPI_EVALUATE_CONTROL_METHOD |
|PEP_NOTIFY_ACPI_QUERY_DEVICE_CONTROL_RESOURCES |0x08 |PEP_ACPI_QUERY_DEVICE_CONTROL_RESOURCES |
|PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES |0x09 |PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES |


## PEP_NOTIFY_ACPI_PREPARE_DEVICE 

Notification: The value PEP_NOTIFY_ACPI_PREPARE_DEVICE.
Data: A pointer to a PEP_ACPI_PREPARE_DEVICE structure that identifies the device by name.
 
Allows the PEP to choose whether to provide ACPI services for a device.

The Windows power management framework (PoFx) sends this notification when the Windows ACPI driver discovers a new device in the ACPI namespace during device enumeration. This notification is sent to PEPs that implement AcceptAcpiNotification callback routines.

To send a PEP_NOTIFY_ACPI_PREPARE_DEVICE notification, PoFx calls the PEP's AcceptAcpiNotification routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_PREPARE_DEVICE, and the Data parameter points to a PEP_ACPI_PREPARE_DEVICE structure that contains the name of the device. If the PEP is prepared to provide ACPI services for this device, the PEP sets the DeviceAccepted member of this structure to TRUE. To decline to provide such services, the PEP sets this member to FALSE.

If the PEP indicates (by setting DeviceAccepted = TRUE) that it is prepared to provide ACPI services for the device, PoFx will respond by sending the PEP a PEP_NOTIFY_ACPI_REGISTER_DEVICE notification to register the PEP to be the sole provider of ACPI services for the device. PoFx expects only one PEP to claim the role of ACPI services provider for a device.

As a best practice, do not perform any device initialization in response to the PEP_NOTIFY_ACPI_PREPARE_DEVICE notification. Instead, defer this initialization until either the PEP_NOTIFY_ACPI_REGISTER_DEVICE notification for the device is received, or an ACPI control method (for example, _INI) is invoked for the device.

For a PEP_NOTIFY_ACPI_PREPARE_DEVICE notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_ABANDON_DEVICE 

Notification: The value PEP_NOTIFY_ACPI_ABANDON_DEVICE.

Data: A pointer to a PEP_ACPI_ABANDON_DEVICE structure that identifies the abandoned device.
 
Informs the PEP that the specified device has been abandoned and no longer requires ACPI services from the PEP.

The Windows power management framework (PoFx) sends this notification to inform the PEP that the device is no longer in use by the operating system. The PEP can use this notification to clean up any internal storage that it has allocated to track the state of the device.

To send a PEP_NOTIFY_ACPI_ABANDON_DEVICE notification, PoFx calls the PEP's AcceptAcpiNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_ABANDON_DEVICE, and the Data parameter points to a PEP_ACPI_ABANDON_DEVICE structure.

PoFx sends this notification only to a PEP that has opted to provide ACPI services for the device in a previous PEP_NOTIFY_ACPI_PREPARE_DEVICE notification. If the PEP has registered to provide these services in a previous PEP_NOTIFY_ACPI_REGISTER_DEVICE notification, PoFx will send a PEP_NOTIFY_ACPI_UNREGISTER_DEVICE notification for the device before sending the PEP_NOTIFY_ACPI_ABANDON_DEVICE notification.

For a PEP_NOTIFY_ACPI_ABANDON_DEVICE notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_REGISTER_DEVICE
Notification: The value PEP_NOTIFY_ACPI_REGISTER_DEVICE.

Data: A pointer to a PEP_ACPI_REGISTER_DEVICE structure that identifies the device. In response to this notification, the PEP is expected to create a valid PEPHANDLE value to identify the device and to write this handle value to the structure.
 
Registers the PEP to be the sole provider of ACPI services for the specified device.

The Windows power management framework (PoFx) sends this notification to a PEP that has indicated—in a previous PEP_NOTIFY_ACPI_PREPARE_DEVICE notification—that it is prepared to provide ACPI services for the specified device.

To send a PEP_NOTIFY_ACPI_REGISTER_DEVICE notification, PoFx calls the PEP's AcceptAcpiNotification routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_REGISTER_DEVICE, and the Data parameter points to a PEP_ACPI_REGISTER_DEVICE structure that identifies the device for which the PEP is to provide ACPI services.

For a PEP_NOTIFY_ACPI_REGISTER_DEVICE notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_UNREGISTER_DEVICE 

Notification: The value PEP_NOTIFY_ACPI_UNREGISTER_DEVICE.

Data: A pointer to a PEP_ACPI_UNREGISTER_DEVICE structure that contains the PEPHANDLE for the device.
 
Cancels the registration of the specified device for ACPI services from the PEP.

In response to this notification, the PEP can destroy the PEPHANDLE that the PEP created for this device in a previous PEP_NOTIFY_ACPI_REGISTER_DEVICE notification.

To send a PEP_NOTIFY_ACPI_UNREGISTER_DEVICE notification, PoFx calls the PEP's AcceptAcpiNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_UNREGISTER_DEVICE, and the Data parameter points to a PEP_ACPI_UNREGISTER_DEVICE structure.

For a PEP_NOTIFY_ACPI_UNREGISTER_DEVICE notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE 

Notification: The value PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE.

Data: A pointer to a PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure that contains an enumeration of the objects in the ACPI namespace of the device.
 
Queries the PEP for the list of ACPI objects (native methods) supported by the PEP under the specified device in the ACPI namespace.

The Windows ACPI driver uses the objects enumerated by this notification to build the namespace for the specified device. Thereafter, when referring to this device, the ACPI driver will query the PEP only for these objects.

The Windows power management framework (PoFx) sends the PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE notification shortly after a device is discovered and the PEP registers to provide ACPI services for the device. For more information about this registration, see PEP_NOTIFY_ACPI_REGISTER_DEVICE.

To send a PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE notification, PoFx calls the PEP's AcceptAcpiNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE, and the Data parameter points to a PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure.

The AcceptAcpiNotification routine is expected to handle a PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE notification and to return TRUE. Failure to do so causes a bug check.

For a PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_QUERY_OBJECT_INFORMATION 

Notification: The value PEP_NOTIFY_ACPI_QUERY_OBJECT_INFORMATION.

Data: A pointer to a PEP_ACPI_QUERY_OBJECT_INFORMATION structure that specifies the attributes of the ACPI object.

Queries the PEP for information about a previously enumerated ACPI object.

The Windows power management framework (PoFx) sends this notification to query the PEP for the attributes of an object that was enumerated during the handling of a previous PEP_NOTIFY_ACPI_ENUMERATE_DEVICE_NAMESPACE notification. Currently, the only objects that are enumerated are control methods.

To send a PEP_NOTIFY_ACPI_QUERY_OBJECT_INFORMATION notification, PoFx calls the PEP's AcceptAcpiNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_QUERY_OBJECT_INFORMATION, and the Data parameter points to a PEP_ACPI_QUERY_OBJECT_INFORMATION structure.

For a PEP_NOTIFY_ACPI_QUERY_OBJECT_INFORMATION notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD 

Notification: The value PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD.

Data: A pointer to a PEP_ACPI_EVALUATE_CONTROL_METHOD structure that specifies an ACPI control method to evaluate, an input argument to supply to this method, and an output buffer for the result.

Is used to evaluate an ACPI control method for which the PEP is the registered handler.

The Windows power management framework (PoFx) sends this notification to the PEP when the Windows ACPI driver needs to evaluate an ACPI control method that is implemented by the PEP.

To send a PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD notification, PoFx calls the PEP's AcceptAcpiNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD, and the Data parameter points to a PEP_ACPI_EVALUATE_CONTROL_METHOD structure.

The platform designer can choose whether to have the PEP or the ACPI firmware handle a particular ACPI control method. If the PEP is the registered handler for an ACPI control method, PoFx responds to a request from the Windows ACPI driver to evaluate this method by sending a PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD notification to the PEP.

The following is a list of examples of ACPI control methods that the PEP can handle for a device:

Device identification and configuration: _HID, _CID, _UID, _ADR, _CLS, _SUB, _CRS, _PRS, and so on. 
Device power management and wake: _PS0 through _PS3, _PR0 through _PR3, _DSW, and so on. 
Device-specific methods: _DSM and any device-stack-specific control methods. 
For a special device, such as an ACPI Time and Alarm device, this notification is used to evaluate time and alarm methods (_GCP, _GRT, _SRT, and so on). 

For a PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_QUERY_DEVICE_CONTROL_RESOURCES 

Notification: The value PEP_NOTIFY_ACPI_QUERY_DEVICE_CONTROL_RESOURCES.

Data: A pointer to a PEP_ACPI_QUERY_DEVICE_CONTROL_RESOURCES structure that contains the list of power resources.
 
Queries the PEP for the list of raw resources needed to control power to the device.

In response to this notification, the PEP provides the list of raw resources that are needed to control power to the device. The Windows ACPI driver requires this list so that it can reserve the power resources required by the device, and provide the corresponding list of translated resources to the PEP (by sending a PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES notification). For more information, see Raw and Translated Resources.

To send a PEP_NOTIFY_ACPI_QUERY_DEVICE_CONTROL_RESOURCES notification, The Windows power management framework (PoFx) calls the PEP's AcceptAcpiNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_QUERY_DEVICE_CONTROL_RESOURCES, and the Data parameter points to a PEP_ACPI_QUERY_DEVICE_CONTROL_RESOURCES structure.

For a PEP_NOTIFY_ACPI_QUERY_DEVICE_CONTROL_RESOURCES notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES 

Notification: The value PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES.

Data: A pointer to a PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure that contains the list of translated resources.
 
Provides the PEP with a list of translated resources for any power control resources needed for the device.

The Windows power management framework (PoFx) sends this notification if the PEP listed any raw resources in response to the previous PEP_NOTIFY_ACPI_QUERY_DEVICE_CONTROL_RESOURCES notification. The PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES notification provides the PEP with the corresponding list of translated resources. For more information, see Raw and Translated Resources.

To send a PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES notification, PoFx calls the PEP's AcceptAcpiNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES, and the Data parameter points to a PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure.

For a PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 
## PEP_NOTIFY_ACPI_WORK 

Notification: The value PEP_NOTIFY_ACPI_WORK.

Data: A pointer to a PEP_WORK structure.
 
Sent to the PEP once each time the PEP calls the RequestWorker routine to request an item of work from the Windows power management framework (PoFx). This notification is used for ACPI-only work.

After the PEP calls the RequestWorker routine to request a work item, PoFx responds by sending the PEP a PEP_NOTIFY_ACPI_WORK notification. However, this notification is not sent until the resources (that is, the worker thread) necessary to process the work item are available. In this way, PoFx guarantees that the work request that the PEP passes to PoFx during the notification can never fail due to lack of resources.

On entry, the PEP should assume that the PEP_WORK structure is uninitialized. To handle this notification, the PEP should set the WorkInformation member to point to a PEP-allocated PEP_WORK_INFORMATION structure that describes the work that is being requested. In addition, the PEP should set the NeedWork member of the PEP_WORK structure to TRUE to confirm that the PEP has handled the PEP_NOTIFY_ACPI_WORK notification and that the WorkInformation member points to a valid PEP_WORK_INFORMATION structure. If the PEP fails to handle the notification or is unable to allocate the PEP_WORK_INFORMATION structure, the PEP should set the WorkInformation member to NULL and set the NeedWork member to FALSE.

For a PEP_NOTIFY_ACPI_WORK notification, the AcceptAcpiNotification routine is always called at IRQL = PASSIVE_LEVEL.
 


