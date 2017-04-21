---
title: Using Device Manager
description: Using Device Manager
ms.assetid: 3c229347-b36f-43e7-9e9c-3ba6ec1e6108
keywords:
- Device Manager WDK
- Device Manager WDK , about Device Manager
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Device Manager


## <a href="" id="ddk-using-device-manager-dg"></a>


To start Device Manager, right-click the My Computer icon, select **Manage** from the menu, and select **Device Manager** from the System Tools that are listed in the resulting display.

Device Manager displays information about each device. This includes the device type, device status, manufacturer, device-specific properties, and information about the driver for the device. See the Help in Device Manager for more information.

If your device is required to start the computer, a problem with your device installation can prevent the computer from starting. In these cases, you have to use the kernel debugger to troubleshoot your device installation. For more information, see the online documentation supplied with the Microsoft debuggers.

If your device is not required to start the computer, you will typically notice a problem with your device installation because your device is not working correctly and Device Manager marks your device with a yellow exclamation point. Device Manager also provides an error message. For more information, see [Device Manager Error Messages](device-manager-error-messages.md).

When you are testing the installation of a new PnP device, it can be useful to have Device Manager list hidden devices. For more information, see [Viewing Hidden Devices](viewing-hidden-devices.md).

For Windows XP and later versions of Windows, Device Manager provides a **Details** tab that contains information that can be useful when you debug drivers. For more information, see [Device Manager Details Tab](device-manager-details-tab.md).

 

 





