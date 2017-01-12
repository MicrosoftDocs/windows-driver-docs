---
title: Privacy and Security in the Sensor and Location Platform
description: Privacy and Security in the Sensor and Location Platform
MS-HAID:
- 'Sensor\_DG\_PrivacySecurity\_db032110-f125-4d57-9ec7-d0a67c471db7.xml'
- 'sensors.privacy\_and\_security\_in\_the\_sensor\_and\_location\_platform'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9defb163-4de6-46cc-b817-d3e6291137be
---

# Privacy and Security in the Sensor and Location Platform


Location data can violate a user's privacy, especially if the information identifies a specific person. A street address, or the latitude and longitude coordinates that determine it, are considered personally identifiable information. Users expect computer software to keep this kind of information secure. The challenge for software developers is to find ways to give users the features they want and need, without violating their privacy.

### Privacy and Security Controls

The sensor and location platform in Windows provides the following features to help ensure that location data remains private:

-   In Windows 8, there are three types of settings for enabling location. There is a setting for administrators that can disable location for all users, a per-user setting to enable or disable location, and for Windows Store apps, users can apply per-app location settings. By default, per-user location settings are turned off until the user provides explicit consent to access the data through Control Panel.

    For more information on location settings in Windows 8, see [Location awareness](https://msdn.microsoft.com/library/windows/apps/br225603).

-   Windows provides disclosure messages to the user. These messages help users understand how using location data can result in the disclosure of personally identifiable information.

-   Desktop apps that use the Location API can call the [**RequestPermissions**](https://msdn.microsoft.com/library/windows/desktop/dd317635) method to open a system dialog box that prompts users to enable location.

-   Location drivers use the sensor class extension. The class extension processes all I/O requests and makes sure that only programs that have user permission can access location data.

### Keeping User Data Private

When you write a sensor driver, you must consider user privacy. You must make sure not to bypass the privacy controls that are enforced by the sensor class extension. Because certain properties can be retrieved before the user has granted permission, you must make sure that your driver does not reveal personally identifiable information through these properties. For a list of properties that are available before the user has granted permission, see [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610).

### Additional Resources

Review the following resources to help you develop software that protects user privacy.

-   [Privacy Guidelines for Developing Software Products and Services](http://go.microsoft.com/fwlink/p/?linkid=237149)

-   [MSDN Security Developer Center](http://go.microsoft.com/fwlink/p/?linkid=237150)

## Related topics


[Architecture Overview](https://msdn.microsoft.com/library/windows/hardware/ff545400)

[About the Sensor Class Extension](https://msdn.microsoft.com/library/windows/hardware/ff545398)

[Location awareness](https://msdn.microsoft.com/library/windows/apps/br225603)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Privacy%20and%20Security%20in%20the%20Sensor%20and%20Location%20Platform%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





