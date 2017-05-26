---
title: What Is Device Stage
author: windows-driver-content
description: What Is Device Stage
ms.assetid: 57b402c5-31ad-4096-be70-a1dbbee86b83
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20What%20Is%20Device%20Stage?%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


