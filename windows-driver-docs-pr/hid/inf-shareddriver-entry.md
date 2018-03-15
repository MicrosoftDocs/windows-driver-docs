---
title: INF SharedDriver Entry
author: windows-driver-content
description: INF SharedDriver Entry
ms.assetid: 36d094b4-481d-41bb-b034-345b0743456e
keywords:
- INF files WDK non-HID keyboard/mouse
- SharedDriver entry WDK non-HID keyboard/mouse
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF SharedDriver Entry


## <a href="" id="ddk-inf-shareddriver-entry-kg"></a>


**\[ControlFlags\]**

*SharedDriver***=***install-section-name****,****warning-text-string*
Before the keyboard or mouse class installer installs a PS/2 device, it checks for a *SharedDriver* entry in the [INF **ControlFlags** section](https://msdn.microsoft.com/library/windows/hardware/ff546342) for the device. If such an entry value exists, the class installer notifies the user by displaying the warning text string, and provides the user the option to cancel changing the PS/2 port driver.

### Entries and Values

<a href="" id="shareddriver"></a>*SharedDriver*  
Specifies that the device driver is shared by both a PS/2 keyboard and mouse device.

<a href="" id="install-section-name"></a>*install-section-name*  
Specifies a device's *DDInstall* section.

<a href="" id="warning-text-string"></a>*warning-text-string*  
Specifies a string the class installer uses to warn a user before changing the PS/2 port driver.

 

 




