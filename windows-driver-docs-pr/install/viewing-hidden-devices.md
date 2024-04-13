---
title: Viewing Hidden Devices
description: Viewing hidden devices
keywords:
- non-present devices WDK
- Device Manager WDK, hidden devices
- hidden devices WDK
- DN_NO_SHOW_IN_DM
- showing hidden devices
- viewing hidden devices
- viewing non-present devices
- showing non-present devices
- displaying non-present devices
ms.date: 12/05/2022
---

# Viewing Hidden Devices

Device Manager lists the devices that are installed in the computer. By default, certain devices aren't shown in the list. These *hidden devices* include:

- Devices that have the [device node (devnode) status](devpkey-device-devnodestatus.md) bit DN_NO_SHOW_IN_DM set.

- Devices that are part of a [device setup class](overview-of-device-setup-classes.md) that is marked as a **NoDisplayClass** (for example, printers and non-PnP drivers)

- Devices that were physically removed from the computer but whose registry entries weren't deleted (also known as non-present devices or phantom devices).

> [!NOTE]
> Starting with Windows 8 and Windows Server 2012, the Plug-and-Play Manager no longer creates device representations for non-PnP (legacy) devices. Thus there are no such devices to view in the Device Manager.

> [!NOTE]
> Users should never have to view non-present devices because a non-present device should not have their attention and should not cause any problems. If a user has to view your device when it is not present, there is likely a problem with your driver design. However, during testing, a developer might have to view such devices.

To include hidden devices in Device Manager display, select **View** and select **Show hidden devices**.

Prior to Windows 8, to view non-present devices, you must set the environment variable DEVMGR_SHOW_NONPRESENT_DEVICES to **1** before you open Device Manager, then open Device Manager, and on the View menu, select **Show hidden devices**.

To permanently set the user environment variable DEVMGR_SHOW_NONPRESENT_DEVICES to **1**, use the **Advanced** tab of the system property sheet. After you set this environment variable, run Device Manager and select **Show hidden devices**.
