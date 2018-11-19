---
title: INF SharedDriver Entry
description: INF SharedDriver Entry
ms.assetid: 36d094b4-481d-41bb-b034-345b0743456e
keywords:
- INF files WDK non-HID keyboard/mouse
- SharedDriver entry WDK non-HID keyboard/mouse
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF SharedDriver Entry





**\[ControlFlags\]**

<em>SharedDriver</em>**=**<em>install-section-name</em>***,***<em>warning-text-string</em>
Before the keyboard or mouse class installer installs a PS/2 device, it checks for a *SharedDriver* entry in the [INF **ControlFlags** section](https://msdn.microsoft.com/library/windows/hardware/ff546342) for the device. If such an entry value exists, the class installer notifies the user by displaying the warning text string, and provides the user the option to cancel changing the PS/2 port driver.

### Entries and Values

<a href="" id="shareddriver"></a>*SharedDriver*  
Specifies that the device driver is shared by both a PS/2 keyboard and mouse device.

<a href="" id="install-section-name"></a>*install-section-name*  
Specifies a device's *DDInstall* section.

<a href="" id="warning-text-string"></a>*warning-text-string*  
Specifies a string the class installer uses to warn a user before changing the PS/2 port driver.

 

 




