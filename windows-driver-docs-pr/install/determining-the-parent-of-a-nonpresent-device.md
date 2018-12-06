---
title: Determining the Parent of a Nonpresent Device
description: Determining the Parent of a Nonpresent Device
ms.assetid: 2d5948db-5844-4f78-b3a6-2f9f88ee1b24
keywords:
- SetupAPI functions WDK , determining parents
- nonpresent devices WDK
- parent device determining WDK SetupAPI
- device parents WDK
- parent-child relationships WDK
- saving parent-child relationships
- retrieving parent-child relationships
- connected sequence of ancestors WDK
- ancestors WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining the Parent of a Nonpresent Device





You can use the approach described in this section to determine the parent of a [*nonpresent device*](https://msdn.microsoft.com/library/windows/hardware/ff556313#wdkgloss-nonpresent-device) only if the relationship between the nonpresent device and its parent is fixed. (If the relationship between a nonpresent device and its parent is not fixed, you cannot use this method because the nonpresent device does not have a specific parent).

For example, this method applies to a USB composite device, such as a multifunction printer, that has one or more interfaces, each of which is represented as a child device. Because all the child interface devices depend on the presence of a specific composite device as their parent, the relationship between the device and its parent is fixed.

The following topics describe this method:

[Saving the Parent/Child Relationship](#saving-the-parent-child-relationship)

[Retrieving the Parent/Child Relationship](#retrieving-the-parent-child-relationship)

[Handling a Chain of Ancestors for a Nonpresent Device](#handling-a-chain-of-ancestors-for-a-nonpresent-device)

### <a href="" id="saving-the-parent-child-relationship"></a> Saving the Parent/Child Relationship

To save the parent/child relationship of a device, supply a [*device co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-co-installer) that saves the device instance ID of the device's parent in a user-created entry value under the hardware registry key of the device. You should use a device instance ID because it remains constant across system restarts and between system processes, whereas a device instance handle does not. When you process a [**DIF_INSTALLDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543692) request in the co-installer, follow these steps to save the device instance ID.

***<em>To save the device instance ID of the immediate parent in the registry</em>***

1.  Call [**CM_Get_Parent**](https://msdn.microsoft.com/library/windows/hardware/ff538610) to obtain a device instance handle for the parent of the device.

2.  Using the device instance handle for the parent device, call [**CM_Get_Device_ID**](https://msdn.microsoft.com/library/windows/hardware/ff538405) to obtain the device instance ID for the parent device.

3.  Call [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) by using the DIREG_DEV flag to obtain a handle to the hardware registry key of the device.

4.  Call **RegSetValueEx** to save the device instance ID of the parent device in a user-created entry value under the hardware registry key of the device.

### <a href="" id="retrieving-the-parent-child-relationship"></a> Retrieving the Parent/Child Relationship

After a device co-installer has saved the device instance ID of the parent device in an entry value under a device's hardware registry key, you can retrieve the device instance ID.

***<em>To retrieve the device instance ID of the parent from the registry</em>***

1.  Call **SetupDiOpenDevRegKey** using the DIREG_DEV flag to obtain a handle to the hardware registry key for the device.

2.  Call **RegQueryValueEx** to retrieve the device instance ID of the parent device that you saved in the entry value that you set in your device co-installer.

After you retrieve the device instance ID of the parent device, call [**SetupDiOpenDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552071) to obtain an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the parent device.

### <a href="" id="handling-a-chain-of-ancestors-for-a-nonpresent-device"></a> Handling a Chain of Ancestors for a Nonpresent Device

If you require the device instance IDs of a connected sequence of ancestors for a given device, you should save the device instance ID for each ancestor in the registry in a way that you can retrieve them. Be aware that this is valid only if the relationship between the device and all the ancestors is fixed.

One way to do this is for your device co-installer to use **CM_Get_Parent** to obtain all the device instance IDs for all the ancestors and save each instance ID in a different entry value under the hardware registry key of the device. You can use the method described in [Saving the Parent/Child Relationship](#saving-the-parent-child-relationship) to save the device instance ID of each ancestor. You can then retrieve each device instance ID in the same way as is described in [Retrieving the Parent/Child Relationship](#retrieving-the-parent-child-relationship).

 

 





