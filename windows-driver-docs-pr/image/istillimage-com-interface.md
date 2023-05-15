---
title: IStillImage COM interface
description: IStillImage COM interface
ms.date: 05/03/2023
---

# IStillImage COM interface

The **IStillImage** COM interface provides access to the [Still image event monitor](overview-of-sti-components.md#ddk-still-image-event-monitor-si) so applications can register themselves as "push-model aware". Applications can use this interface to obtain information about the system's still image devices.

The interface provides some application management functions, such as enabling event notification and starting an application, for use by customized application control software.

Additionally, the **IStillImage** interface provides access to the [IStiDevice COM interface](istidevice-com-interface.md), which allows applications to perform I/O operations on still image devices.

The following table lists and describes all of the **IStillImage** interface's methods. The table indicates the types of clients that typically must call each method.

| Method | Description | Typical callers |
|--|--|--|
| [**IStillImage::CreateDevice**](/previous-versions/windows/hardware/drivers/ff543778(v=vs.85)) | Creates an instance of the COM object that defines the **IStiDevice** interface, and returns a pointer to the interface. | Image Acquisition APIs |
| [**IStillImage::EnableHwNotifications**](/previous-versions/windows/hardware/drivers/ff543780(v=vs.85)) | Enables or disables the notification of applications when [Still Image Device Events](still-image-device-events.md) occur for a specified device. | Still image event monitor |
| [**IStillImage::GetDeviceInfo**](/previous-versions/windows/hardware/drivers/ff543782(v=vs.85)) | Returns hardware characteristics for a specified still image device. | Image Acquisition APIs |
| [**IStillImage::GetDeviceList**](/previous-versions/windows/hardware/drivers/ff543784(v=vs.85)) | Returns hardware characteristics for all installed still image devices. | Scanners and Cameras Control Panel, Image Acquisition APIs |
| [**IStillImage::GetDeviceValue**](/previous-versions/windows/hardware/drivers/ff543786(v=vs.85)) | Returns registry information associated with a specified still image device. | Image Acquisition APIs, Scanners and Cameras Control Panel |
| [**IStillImage::GetHwNotificationState**](/previous-versions/windows/hardware/drivers/ff543788(v=vs.85)) | Indicates whether applications will be notified when still image device events occur on a specified device. | Still image event monitor |
| [**IStillImage::GetSTILaunchInformation**](/previous-versions/windows/hardware/drivers/ff543790(v=vs.85)) | Returns the reason the calling still image application was started, if the still image event monitor started it. | Push-model aware applications |
| [**IStillImage::Initialize**](/previous-versions/windows/hardware/drivers/ff543793(v=vs.85)) | Initializes the object instance. | Not called directly |
| [**IStillImage::LaunchApplicationForDevice**](/previous-versions/windows/hardware/drivers/ff543796(v=vs.85)) | Starts a specified application for a specified still image device. | Still image event monitor |
| [**IStillImage::RegisterLaunchApplication**](/previous-versions/windows/hardware/drivers/ff543798(v=vs.85)) | Adds an application to the still image event monitor's list of push-model aware applications. | Push-model aware applications or their installers |
| [**IStillImage::Release**](/previous-versions/windows/hardware/drivers/ff543799(v=vs.85)) | Closes the object instance and removes access to the **IStillImage** interface. | All **IStillImage** interface clients |
| [**IStillImage::SetDeviceValue**](/previous-versions/windows/hardware/drivers/ff543801(v=vs.85)) | Sets registry information for a specified still image device. | Scanners and Cameras Control Panel |
| [**IStillImage::SetupDeviceParameters**](/previous-versions/windows/hardware/drivers/ff543803(v=vs.85)) | Allows clients of the **IStillImage** interface to modify a still image device's stored characteristics. | Scanners and Cameras Control Panel |
| [**IStillImage::StiCreateInstance**](/previous-versions/windows/hardware/drivers/ff543804(v=vs.85)) | Creates an instance of the COM object that defines the **IStillImage** interface, and returns a pointer to the interface. | All **IStillImage** interface clients |
| [**IStillImage::UnregisterLaunchApplication**](/previous-versions/windows/hardware/drivers/ff543806(v=vs.85)) | Removes an application from the still image event monitor's list of push-model aware applications. | Push-model aware applications or their installers |
| [**IStillImage::WriteToErrorLog**](/previous-versions/windows/hardware/drivers/ff543807(v=vs.85)) | Writes a message to the still image error log. | All **IStillImage** interface clients |
