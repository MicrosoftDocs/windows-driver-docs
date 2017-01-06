---
Description: Device Representation
MS-HAID: 'wpddk.device\_representation'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Device Representation
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Device%20Representation%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




