---
title: INF SharedDriver Entry
author: windows-driver-content
description: INF SharedDriver Entry
ms.assetid: 36d094b4-481d-41bb-b034-345b0743456e
keywords: ["INF files WDK non-HID keyboard/mouse", "SharedDriver entry WDK non-HID keyboard/mouse"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20INF%20SharedDriver%20Entry%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


