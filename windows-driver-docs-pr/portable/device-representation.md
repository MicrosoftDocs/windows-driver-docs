---
Description: Device Representation
title: Device Representation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Representation


Devices have two main behaviors that are addressed by the WPD architecture:

-   Accessing and storing content. For example, applications must be able to add music files to a portable music player.
-   Programming the device. This includes simple operations such as changing settings and preparing the device for data capture, or more complex operations such as uploading firmware. For example, a **Take Picture** command might be issued to a digital still camera.

In WPD, these behaviors are described by representing the device as a hierarchy of objects. The following picture shows a WPD object representation for a multifunction device, in this case, a mobile phone.

![wpd hierarchy](images/wpd_overview_figure3.png)

This hierarchy illustrates the following functionality and contents.

## <span id="Functionality"></span><span id="functionality"></span><span id="FUNCTIONALITY"></span>Functionality


-   Storage object. This device has data storage.
-   Contacts Service. This service is a functional object that can be used to synchronize and store contacts on the phone.
-   SMS Service. This service is a functional object that can be used to send, receive, and store SMS messages.

## <span id="Contents"></span><span id="contents"></span><span id="CONTENTS"></span>Contents


-   Media objects. This device stores images, music, and video files in folders on the Storage object. While the files shown above are stored under one folder, a device can subdivide content into folders organized by the type of media stored (such as an image folder, a music folder, or a video folder).
-   Contact objects. This device stores contact information (such as name, phone number, address, and so on) as children of the Contacts Service.
-   Message objects. This device stores SMS (Short Message Service) messages as children of the SMS Service.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 





