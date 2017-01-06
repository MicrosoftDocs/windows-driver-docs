---
Description: Representing Functionality
MS-HAID: 'wpddk.representing\_functionality'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Representing Functionality
---

# Representing Functionality


The purpose of functional objects is to identify or to group feature capabilities of a device logically. For example, an application can see that a device supports Short Message Service (SMS) by looking for the SMS functional object. Or, the application can see that a device has camera capabilities by looking for the Still Image Capture functional object.

This flexible object representation enables support for devices with multifunction capabilities. Drivers can expose whatever functional objects represent their device, which is more granular than using traditional device classes. It is also useful to isolate functional pieces that overlap. For example, some cell phones might have two cameras, four storage devices, and so on.

In Windows 7, service objects extend functional objects by providing rich capabilities queries and an abstract grouping of content. Applications can use service objects to discover device capabilities and to interact with content more efficiently. For example, an application can see that a device supports the Windows 7 contacts synchronization capabilities by looking for a service object that implements the Microsoft Full Enumeration Sync Contacts Service. Now, the application can locate all contacts on the device without searching the storage hierarchy.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Representing%20Functionality%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




