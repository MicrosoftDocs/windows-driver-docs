---
title: Device Experience in Devices and Printers
description: Device Experience in Devices and Printers
ms.assetid: 95c5ce1d-8a38-4d88-bea2-e6728f83f010
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Experience in Devices and Printers


In Windows Vista, users open the Printers folder to view the available printers. They open the Control Panel Scanners and Cameras application to view the available scanners and cameras. In Windows 7, the Printers folder is removed and all printers and scanners appear in the Devices and Printers view.

If a manufacturer does not supply a custom Device Stage metadata package for a printer, scanner, or MFP device, the devices will still appear in the Devices and Printers view. Devices and Printers user interface provides a default device experience for the device. The default device experience does not include a Device Stage page for the device.

As shown in Figure 3, the device icon and the context menu that appears when the user right-clicks a device in the Devices and Printers view is different for devices that have customized device experiences and those devices that have default device experiences. In this example, the device is a locally connected MFP. For the default experience, shown on the left side of Figure 3, the device is represented by a generic printer icon. For the customized experience, shown on the right side of Figure 3, the device is represented by a custom icon that the manufacturer supplies. For the customized experience, the default action in the context menu is **Open**. Clicking **Open** opens the Device Stage page. **Open in new window** opens the Device Stage in a new window. For the default experience, the device has no associated Device Stage page and the context menu does not contain an **Open** option. Clicking the **See what's printing** option opens the print queue.

![figures comparing the menus for the default device experience and the custom device experience](images/devicestage004.png)

 

 




