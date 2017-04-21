---
Description: Group Policy Changes
title: Group Policy Changes
author: windows-driver-content
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Group Policy Changes


To control device redirection at a granular level, RPM exposes two new software device redirection policies (group policies). These policies can be configured by an IT administrator depending on the needs of the organization.

One policy prevents the alternate driver from being loaded, while the second policy allows some alternate drivers to be loaded.

HID and hub devices can never be redirected and hence remain excluded by default.

The following two new policies are listed under Computer Configuration -&gt; Administrative Templates -&gt; System -&gt; Device Redirection -&gt; Device Redirection Restrictions:

<a href="" id="group-policy-setting--prevent-redirection-of-usb-devices"></a>**Group Policy setting: Prevent redirection of USB devices**  
This policy setting prevents an alternate driver for a USB device from being loaded. When enabled, the alternate driver cannot be loaded. When disabled or not configured, the alternate driver for the USB device can be loaded.

<a href="" id="group-policy-setting--prevent-redirection-of-usb-devices-that-match-any-of-these-device-ids"></a>**Group Policy setting: Prevent redirection of USB devices that match any of these device IDs**  
This policy setting lets the IT Administrator specify a list of USB devices that cannot be redirected. When enabled, an alternate driver will not be loaded if the device ID matches an ID in the list. When disabled or not configured, an alternate driver can be loaded.

To create a list of devices which need to be excluded from redirection, specify a USB device hardware ID, then click OK.

For example, to prevent redirection of a device whose Vendor ID is 058F, Product ID is 6387, and Revision is 0142, type the value in the following format: "VID\_058F&PID\_6387&REV\_0142". The device manager can be used to determine the VID, PID, and revision of a USB device. The IDs of all USB devices connected to the computer are listed under the details tab (hardware IDs).

As an alternative, administrators can use class and protocol information to block USB devices. To specify a device that has a value of Class 08, SubClass 06, and Prot 50, type the value in the following format: "Class\_08&SubClass\_06&Prot\_50". This information is also available in the device manager. The class and protocol values of all USB devices connected to the computer are listed under details tab (compatible IDs).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Group%20Policy%20Changes%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


