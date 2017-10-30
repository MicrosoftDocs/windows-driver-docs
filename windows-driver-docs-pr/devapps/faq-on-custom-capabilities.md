---
title: FAQ on Custom Capabilities
author: windows-driver-content
description: Describes Custom Capabilities for Hardware Support Apps (HSA) and how they differ from other capabilities.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FAQ on Custom Capabilities

## How are Custom Capabilities different from other capabilities?

1)  3rd party Microsoft partners can define new capabilities.

2)  They don't have to be built-in to Windows at compile time.

3)  App authorization to use the capability verifies during the app
    installation instead of when uploaded to the store.

## What is the best way to install a UWP app with Custom Capabilities?
The suggested method to install a UWP app with Custom Capabilities is to pre-install the app using DISM (Deployment Image Servicing and Management). For more information on DISM's see [DISM - Deployment Image Servicing and Management](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management-technical-reference-for-windows).
## What’s the difference between UWP apps with Custom Capabilities and DCA’s (Device Companion Apps)?

|                           | **DCA**                                                  | **UWP app with Custom Capabilities**|
|---------------------------|----------------------------------------------------------|-------------------------------------|
|Communication|Device Scenario APIS (image capture, scanning, etc.)<br>Device protocol APIs (USB, HID, etc.)<br>Customer driver access|                                                                              
|Trust Model|Defined at a “container” level<br>The system's OEM must submit apps for internal components|Defined at a system level<br>The system's OEM must submit apps for internal components|
|Automatic App Acquisition  |Available for peripherals                                  |Available for all hardware          |
|Deployment Dependencies    |WU: Driver package<br>Store: App|WU: Driver package<br>Store: App                  |
                                                                                                                                                    
                                                                                                            
                                                                                                                                                    
                                                  

For more information on DCA’s, see [Getting started with Microsoft Store device apps](https://msdn.microsoft.com/windows/hardware/drivers/devapps/getting-started).

