---
title: The radio-manager file list
author: windows-driver-content
description: The following table describes the files that are found in the radio manager DLL.
ms.assetid: 70A8B11F-89FF-49E3-933E-2BB66D5E1BF6
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# The radio-manager file list


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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20The%20radio-manager%20file%20list%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


