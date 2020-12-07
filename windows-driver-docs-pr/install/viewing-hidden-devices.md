---
title: Viewing hidden devices
description: Viewing hidden devices
keywords:
- nonpresent devices WDK
- Device Manager WDK , hidden devices
- hidden devices WDK
- DN_NO_SHOW_IN_DM
- showing hidden devices
- viewing hidden devices
- viewing nonpresent devices
- showing nonpresent devices
- displaying nonpresent devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Viewing Hidden Devices

Device Manager lists the devices that are installed in the computer. By default, certain devices are not shown in the list. These *hidden devices* include:

* Devices that have the device node (devnode) status bit DN_NO_SHOW_IN_DM set.

    There is a devnode for each device on a machine and the devnodes are organized into a hierarchical Device Tree. The PnP manager creates a devnode for a device when the device is configured.

    A devnode contains the device stack (the device objects for the device's drivers) and information about the device such as whether the device has been started and which drivers have registered for notification on the device.

* Devices that are part of a setup class that is marked as a **NoDisplayClass** in the registry (for example, printers and non-PnP drivers)

* Devices that were physically removed from the computer but whose registry entries were not deleted (also known as nonpresent devices).

> [!NOTE]
> Starting with Windows 8 and Windows Server 2012, the Plug-and-Play Manager no longer creates device representations for non-PnP (legacy) devices. Thus there are no such devices to view in the Device Manager.

> [!NOTE]
> Users should never have to view nonpresent devices because a nonpresent device should not have their attention and should not cause any problems. If a user has to view your device when it is not present, there is likely a problem with your driver design. However, during testing, a developer might have to view such devices.

To include hidden devices in Device Manager display, select **View** and select **Show hidden devices**.

Prior to Windows 8, to view nonpresent devices, you must set the environment variable DEVMGR_SHOW_NONPRESENT_DEVICES to **1** before you open Device Manager, then open Device Manager, and on the View menu, select **Show hidden devices**.

To permanently set the user environment variable DEVMGR_SHOW_NONPRESENT_DEVICES to **1**, use the **Advanced** tab of the system property sheet. After you set this environment variable, run Device Manager and select **Show hidden devices**.
