---
title: Privacy and Security in the Sensor and Location Platform
description: Privacy and Security in the Sensor and Location Platform
ms.assetid: 9defb163-4de6-46cc-b817-d3e6291137be
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Privacy and Security in the Sensor and Location Platform


Location data can violate a user's privacy, especially if the information identifies a specific person. A street address, or the latitude and longitude coordinates that determine it, are considered personally identifiable information. Users expect computer software to keep this kind of information secure. The challenge for software developers is to find ways to give users the features they want and need, without violating their privacy.

### Privacy and Security Controls

The sensor and location platform in Windows provides the following features to help ensure that location data remains private:

-   In Windows 8, there are three types of settings for enabling location. There is a setting for administrators that can disable location for all users, a per-user setting to enable or disable location, and for UWP apps, users can apply per-app location settings. By default, per-user location settings are turned off until the user provides explicit consent to access the data through Control Panel.

    For more information on location settings in Windows 8, see [Location awareness](https://msdn.microsoft.com/library/windows/apps/br225603).

-   Windows provides disclosure messages to the user. These messages help users understand how using location data can result in the disclosure of personally identifiable information.

-   Desktop apps that use the Location API can call the [**RequestPermissions**](https://msdn.microsoft.com/library/windows/desktop/dd317635) method to open a system dialog box that prompts users to enable location.

-   Location drivers use the sensor class extension. The class extension processes all I/O requests and makes sure that only programs that have user permission can access location data.

### Keeping User Data Private

When you write a sensor driver, you must consider user privacy. You must make sure not to bypass the privacy controls that are enforced by the sensor class extension. Because certain properties can be retrieved before the user has granted permission, you must make sure that your driver does not reveal personally identifiable information through these properties. For a list of properties that are available before the user has granted permission, see [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610).

### Additional Resources

Review the following resources to help you develop software that protects user privacy.

-   [Privacy Guidelines for Developing Software Products and Services](http://go.microsoft.com/fwlink/p/?linkid=237149)

-   [TechNet Security Developer Center](http://go.microsoft.com/fwlink/p/?linkid=237150)

## Related topics
[Architecture Overview](https://msdn.microsoft.com/library/windows/hardware/ff545400)  
[About the Sensor Class Extension](https://msdn.microsoft.com/library/windows/hardware/ff545398)  
[Location awareness](https://msdn.microsoft.com/library/windows/apps/br225603)  



