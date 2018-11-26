---
title: Creating Push-Model Aware Applications
description: Creating Push-Model Aware Applications
ms.assetid: 0f554b2c-0217-4109-8ef6-99c5400dfed6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Push-Model Aware Applications





A push-model aware application is one that has registered itself with Microsoft STI so that it can be automatically activated when a still image device event has occurred. An application can be made push-model aware by either of the following two methods:

-   Calling [**IStillImage::RegisterLaunchApplication**](https://msdn.microsoft.com/library/windows/hardware/ff543798). The call can be made by the application or by its installation program.

-   Including an entry in the application's setup information (INF) file. The entry should be referenced by an [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) in the INF file. The syntax of the entry is illustrated in the following example:

    ```INF
    ; Register Application "Imaging" as a push-model aware application for use with the still image event monitor
    HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\StillImage\Registered Applications",Imaging,,"%25%\KodakImg.Exe /StiDevice:%%1 /StiEvent:%%2"
    ```

    Two INF file entries are required for devices that support push-model aware applications: **DeviceData** and **Events**. For more information, see [INF Files for Still Image Devices](inf-files-for-still-image-devices.md).

Either of these methods causes the application to be registered with the [Still Image Event Monitor](overview-of-sti-components.md#ddk-still-image-event-monitor-si).

If an application is registered as push-model aware, a user can assign [Still Image Device Events](still-image-device-events.md) to the application with the Scanners and Cameras Control Panel. Additionally, vendors can provide an initial assignment of device events to applications by including application names within a device driver's INF file. A user can change this initial assignment with the Scanners and Cameras Control Panel.

After device events have been assigned to an application, the event monitor will start the application when it detects an occurrence of an assigned device event.

When a push-model aware application is activated, it should call [**IStillImage::GetSTILaunchInformation**](https://msdn.microsoft.com/library/windows/hardware/ff543790) to determine the event and the device for which it was started. It can then call [**IStillImage::GetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff543782) to obtain more information about the device.

The application must handle the event, or it must create a user display explaining why it cannot handle the event. Presumably, the user will then use Control Panel to associate the device event with some other application.

Handling the event typically means reading in an image. To do this, the application typically calls an [Image Acquisition API](overview-of-sti-components.md#ddk-image-acquisition-api-si), such as TWAIN.

If an application has been started because an event occurred, but an image acquisition API has not opened the device in data mode (see [Transfer Modes](transfer-modes.md)), the event monitor will start another instance of the application if another event is detected. The application must be implemented so that it either allows multiple instances or (preferably) recognizes when it is not the first instance, sends a message to the first instance identifying the event, and exits.

 

 




