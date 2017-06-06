---
title: FAQ on custom capabilities
author: windows-driver-content
description: Describes custom capabilities for Hardware Support Apps (HSA) and how they differ from other capabilities.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FAQ on custom capabilities

## How are custom capabilities different from other capabilities?

1)  3rd party Microsoft partners can define new capabilities.

2)  They don't have to be built-in to Windows at compile time.

3)  App authorization to use the capability verifies during the app
    installation instead of when uploaded to the store.

## What’s the difference between UWP’s with Custom Capabilities and DCA’s (Device Companion Apps)?

|                           | **DCA**                                                  | **UWP App with Custom Capabilities**|
|---------------------------|----------------------------------------------------------|-------------------------------------|
|Communication|Device Scenario APIS (image capture, scanning, etc.)<br>Device protocol APIs (USB, HID, etc.)<br>Customer driver access|                                                                              
|Trust Model|Defined at a “container” level<br>The system's OEM must submit apps for internal components|Defined at a system level<br>The system's OEM must submit apps for internal components|
|Automatic App Acquisition  |Available for peripherals                                  |Available for all hardware          |
|Deployment Dependencies    |WU: Driver package<br>Store: App|WU: Driver package<br>Store: App                  |
                                                                                                                                                    
                                                                                                            
                                                                                                                                                    
                                                  

For more information on DCA’s, see [Getting started with Windows Store
device
apps](https://msdn.microsoft.com/windows/hardware/drivers/devapps/getting-started).

