---
title: FAQ on Custom Capabilities
description: Describes Custom Capabilities for Hardware Support Apps (HSA) and how they differ from other capabilities.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# FAQ on Custom Capabilities

## How are custom capabilities different from other capabilities?

1. Microsoft partners can define custom capabilities.
2. Custom capabilities do not have to be built in to Windows at compile time.
3. Windows verifies that an app is authorized to use a custom capability when the app installs.  For other capabilities, this verification happens when the Windows Store receives the app submission.

## What's the difference between UWP apps with custom capabilities and Device Companion Apps (DCAs)?

|                           | **DCA**                                                  | **UWP app with custom capabilities**|
|---------------------------|----------------------------------------------------------|-------------------------------------|
|Communication|Device Scenario APIS (image capture, scanning, etc.)<br>Device protocol APIs (USB, HID, etc.)<br>Customer driver access|                                                                              
|Trust Model|Defined at a "container" level<br>The system's OEM must submit apps for internal components|Defined at a system level<br>The system's OEM must submit apps for internal components|
|Automatic App Acquisition  |Available for peripherals                                  |Available for all hardware          |
|Deployment Dependencies    |WU: Driver package<br>Store: App|WU: Driver package<br>Store: App                  |
                                                                                                                                                                                                    
For more information on DCAs, see [Getting started with Microsoft Store device apps](https://msdn.microsoft.com/windows/hardware/drivers/devapps/getting-started).

