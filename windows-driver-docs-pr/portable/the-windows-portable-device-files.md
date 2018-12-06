---
Description: The Windows Portable Devices Files
title: The Windows Portable Devices Files
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 




