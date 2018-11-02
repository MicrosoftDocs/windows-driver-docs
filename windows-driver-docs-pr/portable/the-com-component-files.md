---
Description: The COM Component Files
title: The COM Component Files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The COM Component Files


The WpdHelloWorldDriver project contains the following COM component files.

| Filename                | Description                                                                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| resource.h              | Contains a single definition for the driver's identifier.                                                                                                 |
| stdafx.h                | Includes standard system files.                                                                                                                           |
| WpdHelloWorldDriver.cpp | Contains the basic COM methods that handle server registration, returning a class factory, and the DLL entry point.                                       |
| WpdHelloWorldDriver.def | Declares the module parameters.                                                                                                                           |
| WpdHelloWorldDriver.idl | Contains the necessary definitions for the driver's COM component.                                                                                        |
| WpdHelloWorldDriver.rc  | Contains definitions for resources required by the driver. These resources include the file type, the file description string, and the original filename. |
| WpdHelloWorldDriver.rgs | Contains the registration script for the driver's COM component.                                                                                          |

 

 

 




