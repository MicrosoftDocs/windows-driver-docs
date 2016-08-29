---
title: Viewing Hidden Devices
description: Viewing Hidden Devices
ms.assetid: 5dd02478-9937-4364-bd33-b64ac89c32eb
keywords: ["nonpresent devices WDK", "Device Manager WDK , hidden devices", "hidden devices WDK", "DN_NO_SHOW_IN_DM", "showing hidden devices", "viewing hidden devices", "viewing nonpresent devices", "showing nonpresent devices", "displaying nonpresent devices"]
---

# Viewing Hidden Devices


## <a href="" id="ddk-viewing-hidden-devices-dg"></a>


Device Manager lists the devices that are installed in the computer. By default, certain devices are not shown in the list. These *hidden devices* include devices that have the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) status bit DN\_NO\_SHOW\_IN\_DM set and devices that are part of a setup class that is marked as a **NoDisplayClass** in the registry (for example, printers and non-PnP drivers).

**Note**  Starting with Windows 8 and Windows Server 2012, the Plug-and-Play Manager no longer creates device representations for non-PnP (legacy) devices. Thus there are no such devices to view in the Device Manager.

 

To include hidden devices in Device Manager display, click **View** and select **Show Hidden Devices**.

Another category of hidden devices, not shown in Device Manager by default, includes devices that were physically removed from the computer but whose registry entries were not deleted. These devices are considered [*nonpresent devices*](https://msdn.microsoft.com/library/windows/hardware/ff556313#wdkgloss-nonpresent-device). Users should never have to view such devices because a nonpresent device should not have their attention and should not cause any problems. If a user has to view your device when it is not present, there is likely a problem with your driver design.

However, during testing, a developer might have to view such devices. To view nonpresent devices, you must set the environment variable DEVMGR\_SHOW\_NONPRESENT\_DEVICES to **1** before you open Device Manager, then open Device Manager and select **Show Hidden Devices**.

To permanently set the user environment variable DEVMGR\_SHOW\_NONPRESENT\_DEVICES to **1**, use the **Advanced** tab of the system property sheet. After you set this environment variable, run Device Manager and select **Show Hidden Devices**.

For information about how to set user environment variables, see "Setting environment variables" in the Help and Support Center.

For more information about hidden devices, see [Hiding Devices from Device Manager](https://msdn.microsoft.com/library/windows/hardware/ff547032).

 

 





