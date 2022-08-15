---
title: Privacy and Security in the Sensor and Location Platform
description: The sensor and location platform in Windows provides features to help ensure that location data remains private.
ms.date: 08/25/2021
---

# Privacy and Security in the Sensor and Location Platform

Location data can violate a user's privacy, especially if the information identifies a specific person. A street address, or the latitude and longitude coordinates that determine it, are considered personally identifiable information. Users expect computer software to keep this kind of information secure. The challenge for software developers is to find ways to give users the features they want and need, without violating their privacy.

## Privacy and Security Controls

The sensor and location platform in Windows provides the following features to help ensure that location data remains private:

- In Windows 8, there are three types of settings for enabling location. There is a setting for administrators that can disable location for all users, a per-user setting to enable or disable location, and for UWP apps, users can apply per-app location settings. By default, per-user location settings are turned off until the user provides explicit consent to access the data through Control Panel. For more information on location settings in Windows 8, see [Location awareness](/uwp/api/Windows.Devices.Geolocation).

- Windows provides disclosure messages to the user. These messages help users understand how using location data can result in the disclosure of personally identifiable information.

- Desktop apps that use the Location API can call the [**RequestPermissions**](/windows/win32/api/locationapi/nf-locationapi-ilocation-requestpermissions) method to open a system dialog box that prompts users to enable location.

- Location drivers use the sensor class extension. The class extension processes all I/O requests and makes sure that only programs that have user permission can access location data.

## Keeping User Data Private

When you write a sensor driver, you must consider user privacy. You must make sure not to bypass the privacy controls that are enforced by the sensor class extension. Because certain properties can be retrieved before the user has granted permission, you must make sure that your driver does not reveal personally identifiable information through these properties. For a list of properties that are available before the user has granted permission, see [**ISensorDriver::OnGetProperties**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetproperties).

## Related topics

[Architecture Overview](../sensors/architecture-overview-for-sensor-drivers.md)  

[About the Sensor Class Extension](../sensors/about-the-sensor-class-extension.md)  

[Location awareness](/uwp/api/Windows.Devices.Geolocation)
