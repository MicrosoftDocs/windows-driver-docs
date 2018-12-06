---
Description: Representing Functionality
title: Representing Functionality
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Representing Functionality


The purpose of functional objects is to identify or to group feature capabilities of a device logically. For example, an application can see that a device supports Short Message Service (SMS) by looking for the SMS functional object. Or, the application can see that a device has camera capabilities by looking for the Still Image Capture functional object.

This flexible object representation enables support for devices with multifunction capabilities. Drivers can expose whatever functional objects represent their device, which is more granular than using traditional device classes. It is also useful to isolate functional pieces that overlap. For example, some cell phones might have two cameras, four storage devices, and so on.

In Windows 7 and onwards, service objects extend functional objects by providing rich capabilities queries and an abstract grouping of content. Applications can use service objects to discover device capabilities and to interact with content more efficiently. For example, an application can see that a device supports contact synchronization by looking for a service object that implements the Microsoft Full Enumeration Sync Contacts Service. Now, the application can locate all contacts on the device without searching the storage hierarchy.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 





