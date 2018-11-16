---
title: The radio-manager file list
description: The following table describes the files that are found in the radio manager DLL.
ms.assetid: 70A8B11F-89FF-49E3-933E-2BB66D5E1BF6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The radio-manager file list

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The following table describes the files that are found in the radio manager DLL.

|                              |                                                                                                                                                                                                                                             |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File name                    | Contents                                                                                                                                                                                                                                    |
| SampleRM.sln                 | The Visual Studio 2010 solution file for building the Sample Radio Manager dll                                                                                                                                                              |
| sampleRM.idl                 | The interface definition for the Sample Radio Manager                                                                                                                                                                                       |
| RadioMgr.idl                 | The interface definition for a Windows Radio Manager                                                                                                                                                                                        |
| SampleRadioManager.h         | Header file for the functions required for a Radio Manager                                                                                                                                                                                  |
| SampleRadioInstance.h        | Header file for the functions required for a Radio Instance                                                                                                                                                                                 |
| SampleInstanceCollection.h   | Header file for the functions required for a Collection of Radio Instances                                                                                                                                                                  |
| precomp.h                    | Common header file                                                                                                                                                                                                                          |
| dllmain.cpp                  | Standard dllmain                                                                                                                                                                                                                            |
| InternalInterfaces.h         | Header file for internal interface used for this sample                                                                                                                                                                                     |
| SampleRadioManager.cpp       | Implementation details for the Sample Radio Manager. Important concepts include: - Utilizing IMediaRadioManagerNotifySink for radio instance events - Adding/Removing radio instances - Queuing and deploying worker jobs for system events |
| SampleRadioInstance.cpp      | Implementation details for the Sample Radio Instance. Important concepts include: - Accessors & Modifiers for radio information - Instance change functions                                                                                 |
| SampleInstanceCollection.cpp | Implementation details for the Sample Instance Collection. Important concepts include: - Radio Instance discovery and retrieval                                                                                                             |
| RadioMgr\_interface.cpp      | Helper source file to include the MIDL-generated files.                                                                                                                                                                                     |

 

 

 




