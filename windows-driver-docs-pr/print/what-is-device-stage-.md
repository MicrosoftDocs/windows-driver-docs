---
title: What Is Device Stage
description: What Is Device Stage
ms.assetid: 57b402c5-31ad-4096-be70-a1dbbee86b83
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What Is Device Stage?


Device Stage is a new Windows platform that enables device manufacturers to deliver rich user experiences that match the specific branding, features, and content of their devices. With Device Stage, users can simply connect their device to a Windows 7 PC, and the manufacturer-supplied experience will be automatically installed and presented to the user, ensuring a seamless experience between the device and PC.

Device Stage is closely linked to the other prominent Windows Device Experience end-user feature, the Devices and Printers folder. A Device Stage experience contains all the elements necessary to work with both the Device Stage platform and the Devices and Printers folder. Users navigate to Device Stage by first navigating from the Windows Start menu to the Devices and Printers folder, where they will find the photo-realistic icon that represents their physical device. Double-clicking on the icon opens Device Stage. For nomad devices, Device Stage shows the device directly on the Windows taskbar when the device is currently connected.

A Device Stage experience is made up of XML and graphics files. These files define the functionality and branding to be used by the Device Stage platform when rendering the experience. These files also contain device-specific information, including identifying information about the devices for which the Device Stage experience should be presented. The files are assembled together into a device metadata package for easy distribution. A validation system run by Microsoft digitally signs the package and its components after determining that the associated devices meet certain quality requirements, such as those set by the Windows Hardware Certification Kit (HCK). The Device Stage experience must also be well-formed and meet the requirements for the device class. Microsoft hosts a Web service for global distribution of device metadata packages to Windows PCs. Device metadata packages are automatically retrieved and processed by Windows when a device is connected to the Windows PC.

Device Stage provides several advantages to device makers:

-   **Increased customer connection**

    Device Stage provides a highly customizable user interface that places your device in the center of the Windows experience. Custom logos, rich graphics, and device images reflect your unique product and corporate branding on the desktop.

-   **Richer desktop experiences**

    Windows 7 provides a rich set of device functionality such as setting print preferences, scan a document, view contents of storage, and many more. With Device Stage you can include key device functionality in your device experience without having to develop, download, and install additional software.

-   **Deploy and update device experiences anytime**

    Windows 7 Device Stage automatically retrieves the latest device experience metadata for the device from WMIS service. You can update the data on the service at anytime, ensuring that you retain complete control over the experience and that users are given the most current applications, services, and content for their device.

 

 




