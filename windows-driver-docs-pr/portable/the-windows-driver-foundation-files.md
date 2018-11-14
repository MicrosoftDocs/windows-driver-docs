---
Description: The Windows Driver Frameworks Files
title: The Windows Driver Frameworks Files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The Windows Driver Frameworks Files


The WpdHelloWorldDriver project contains the following Windows user-mode driver framework (UMDF) files.

| Filename   | Description                                                                                                                                                                   |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device.cpp | Contains an implementation of the CDevice member functions. These functions handle Plug and Play and Power-Management events.                                                 |
| Device.h   | Contains a definition for the CDevice class.                                                                                                                                  |
| Driver.cpp | Contains an implementation of the CDriver member functions. These functions handle device initialization and cleanup.                                                         |
| Driver.h   | Contains a definition for the CDriver class.                                                                                                                                  |
| Queue.cpp  | Contains an implementation of the CQueue member functions.                                                                                                                    |
| Queue.h    | Contains a definition for the CQueue class as well as definitions for the Windows Driver Foundation (WDF) callbacks. These functions handle device control and file creation. |

 

 

 




