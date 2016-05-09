---
title: Introduction to File System Filters
author: windows-driver-content
description: The file systems in Windows are implemented as file system drivers working above the storage system.
ms.assetid: 62DE75F7-0211-4173-AF45-84B2DDFDC95C
---

# Introduction to File System Filters


The file systems in Windows are implemented as file system drivers working above the storage system. Each of the file systems in Windows are designed to provide reliable data storage with varying features to meet the user’s requirements. A comparison of features for each of the standard file systems in Windows is shown in [File System Functionality Comparison](https://msdn.microsoft.com/library/windows/desktop/ee681827). New for Windows Server 2012 is ReFS. ReFS is a file system with scalable large volume support and the ability detect and correct data corruption on disk.

Creating a new file system driver in addition to those supplied in Windows is likely unnecessary. File Systems and File System Filter Drivers can provide any customized behavior required to modify the operation of existing file systems.

## <span id="File_System_Filter_Driver_Development"></span><span id="file_system_filter_driver_development"></span><span id="FILE_SYSTEM_FILTER_DRIVER_DEVELOPMENT"></span>File System Filter Driver Development


A file system filter driver intercepts requests targeted at a file system or another file system filter driver. By intercepting the request before it reaches its intended target, the filter driver can extend or replace functionality provided by the original target of the request. Examples of File Systems and File System Filter Drivers include anti-virus filters, backup agents, and encryption products.

File system filtering services are available through the [Filter Manager](filter-manager-and-minifilter-driver-architecture.md) in Windows. The Filter Manager provides a framework for developing File Systems and File System Filter Drivers without having to manage all the complexities of file I/O. The Filter Manager simplifies the development of third-party filter drivers and solves many of the problems with the existing legacy filter driver model, such as the ability to control load order through an assigned altitude. A filter driver developed to the Filter Manager model is called a minifilter. Every minifilter driver has an assigned altitude, which is a unique identifier that determines where the minifilter is loaded relative to other minifilters in the I/O stack. Altitudes are allocated and managed by Microsoft.

## <span id="File_System_Filter_Driver_Certification"></span><span id="file_system_filter_driver_certification"></span><span id="FILE_SYSTEM_FILTER_DRIVER_CERTIFICATION"></span>File System Filter Driver Certification


Certification information for File Systems and File System Filter Drivers is found in the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613). Tests for File Systems and File System Filter Drivers are found in the [Filter.Driver](http://msdn.microsoft.com/library/windows/hardware/jj124779) category of the HCK.

## <span id="File_System_Filter_Driver_Developer_Resources"></span><span id="file_system_filter_driver_developer_resources"></span><span id="FILE_SYSTEM_FILTER_DRIVER_DEVELOPER_RESOURCES"></span>File System Filter Driver Developer Resources


To request an altitude allocation from Microsoft, send an e-mail asking for an altitude assignment for your minifilter. Follow the instructions in [Minifilter Altitude Request](minifilter-altitude-request.md) to submit a request.

To obtain an ID for a filter driver that uses reparse points follow the steps in [Reparse Point Request](reparse-point-tag-request.md).

You can subscribe to the NTFSD newsgroup for details about developing file systems and filter drivers. The group is found at [NT File System Drivers Newsgroup](http://go.microsoft.com/fwlink/p/?LinkId=620898).

OSR's "Developing File Systems for Windows" seminar explores developing file systems and File Systems and File System Filter Drivers. See [Training for IFS Developers](http://go.microsoft.com/fwlink/p/?linkid=50692).

## <span id="IFS_Plugfest_28"></span><span id="ifs_plugfest_28"></span><span id="IFS_PLUGFEST_28"></span>**IFS Plugfest 28**


We are pleased to inform you that Installable File Systems (IFS) Plugfest 28 has been scheduled. Here are some preliminary event details:

### <span id="When"></span><span id="when"></span><span id="WHEN"></span>When

Monday, April 25<sup>th</sup> to Friday, April 29<sup>th</sup>, 2015.

The event begins at 9am and ends at 6pm each day, except for Friday, when it ends at 3pm.

### <span id="Where"></span><span id="where"></span><span id="WHERE"></span>Where

Building 37, rooms 1717-1727, Microsoft Campus, Redmond, Washington ([map](http://go.microsoft.com/fwlink/p/?LinkId=620764)).

### <span id="Audience"></span><span id="audience"></span><span id="AUDIENCE"></span>Audience

Independent Software Vendors (ISVs) and developers writing file system filter drivers and/or network filter drivers for Windows.

### <span id="Cost"></span><span id="cost"></span><span id="COST"></span>Cost

**Free** – There is no cost for this event. Attendees are responsible for their own travel and lodging.

### <span id="Goals"></span><span id="goals"></span><span id="GOALS"></span>Goals

-   Compatibility testing filters for Windows vNext with other file system filters and network filter drivers.
-   To ensure end users have a smooth upgrade to Windows vNext from Windows 7 or later.

### <span id="Benefits"></span><span id="benefits"></span><span id="BENEFITS"></span>Benefits

-   The opportunity to test products extensively for interoperability with other vendors' products and with Microsoft products. This is a great way to understand interoperability scenarios and flush out any interoperability-related bugs.
-   Talks and informative sessions by Microsoft product teams about topics that affect the filter driver community.

### <span id="Registration"></span><span id="registration"></span><span id="REGISTRATION"></span>Registration

To register, please fill in the [Registration Form](https://centerstage.research.microsoft.com/registration?rc=AIB5-BHWU-QOXC-ZK5S) before February 19th 2016. We will follow up through email to confirm your registration. Due to constraints in space and resources at this Plugfest, ISVs are required to limit their participation to a **maximum of two persons representing a product** to be tested for interoperability issues. There will be no exceptions to this rule, so please plan for the event accordingly. Please look for messages from <fsfcomm@microsoft.com> for registration confirmation.

Regards,

The Microsoft file systems team

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Introduction%20to%20File%20System%20Filters%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


