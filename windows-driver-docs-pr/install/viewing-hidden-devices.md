---
title: Viewing Hidden Devices
description: Viewing Hidden Devices
ms.assetid: 5dd02478-9937-4364-bd33-b64ac89c32eb
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Viewing Hidden Devices


## <a href="" id="ddk-viewing-hidden-devices-dg"></a>


Device Manager lists the devices that are installed in the computer. By default, certain devices are not shown in the list. These *hidden devices* include:

* Devices that have the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) status bit DN_NO_SHOW_IN_DM set
* Devices that are part of a setup class that is marked as a **NoDisplayClass** in the registry (for example, printers and non-PnP drivers)
* Devices that were physically removed from the computer but whose registry entries were not deleted (also known as [*nonpresent devices*](https://msdn.microsoft.com/library/windows/hardware/ff556313#wdkgloss-nonpresent-device)).

**Note**  Starting with Windows 8 and Windows Server 2012, the Plug-and-Play Manager no longer creates device representations for non-PnP (legacy) devices. Thus there are no such devices to view in the Device Manager.

**Note**  Users should never have to view nonpresent devices because a nonpresent device should not have their attention and should not cause any problems. If a user has to view your device when it is not present, there is likely a problem with your driver design. However, during testing, a developer might have to view such devices. 

To include hidden devices in Device Manager display, click **View** and select **Show Hidden Devices**.

Prior to Windows 8, to view nonpresent devices, you must set the environment variable DEVMGR_SHOW_NONPRESENT_DEVICES to **1** before you open Device Manager, then open Device Manager and select **Show Hidden Devices**.

To permanently set the user environment variable DEVMGR_SHOW_NONPRESENT_DEVICES to **1**, use the **Advanced** tab of the system property sheet. After you set this environment variable, run Device Manager and select **Show Hidden Devices**.

For information about how to set user environment variables, see "Setting environment variables" in the Help and Support Center.

For more information about hidden devices, see [Hiding Devices from Device Manager](https://msdn.microsoft.com/library/windows/hardware/ff547032).

 

 





