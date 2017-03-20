---
Description: The Windows Portable Devices Files
MS-HAID: 'wpddk.the\_windows\_portable\_device\_files'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The Windows Portable Devices Files
---

# The Windows Portable Devices Files


The WpdHelloWorldDriver project contains the following Windows Portable Devices files.

| Filename                | Description                                                                                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WpdBaseDriver.cpp       | Contains an implementation of the WpdBaseDriver member functions.                                                                                                                  |
| WpdBaseDriver.h         | Contains the definition of the WpdBaseDriver class. This class contains the member functions which dispatch messages, initialize the driver object, and so on.                     |
| WpdCapabilities.cpp     | Contains an implementation of the WpdCapabilities member functions.                                                                                                                |
| WpdCapabilities.h       | Contains the definition for the WpdCapabilities class. This class contains the event handlers for retrieving: supported commands, command options, function categories, and so on. |
| WpdObjectEnum.cpp       | Contains an implementation of the WpdObjectEnumerator class.                                                                                                                       |
| WpdObjectEnum.h         | Contains the definition for the WpdObjectEnumerator class. This class contains the member functions that enumerate objects supported by the device.                                |
| WpdObjectProperties.cpp | Contains an implementation of the WpdObjectProperties class.                                                                                                                       |
| WpdObjectProperties.h   | Contains the definition for the WpdObjectProperties class. This class contains the member functions that set and retrieve properties supported by the device.                      |
| WpdObjectResources.cpp  | Contains an implementation of the WpdObjectResources member functions.                                                                                                             |
| WpdObjectResources.h    | Contains the definition for the WpdObjectResources class. This class contains a member function that retrieves the resources supported by the driver.                              |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20Windows%20Portable%20Devices%20Files%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



