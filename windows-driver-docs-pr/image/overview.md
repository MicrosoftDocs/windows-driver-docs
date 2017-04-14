---
title: Overview
author: windows-driver-content
description: Overview
ms.assetid: e9a45ae0-0ec8-4d6c-8486-ae88bdaa1f8c
---

# Overview


Distributed Scan Management (DSM) enables IT administrators to manage scanning services for organizations with many users. DSM is implemented in Windows Server 2008 R2 and uses Web Services on Devices (WSD) technologies to integrate scanning devices into the system.

For a list of helpful DSM terms and definitions, see [DSM Terminology](dsm-terminology.md).

A device that supports DSM can be a network-connected image scanner, or it can be a scanner function in a network-connected copier or multifunction printer. A DSM scan device works in conjunction with a DSM scan server. DSM Scan Server is a feature in Windows Server 2008 R2 and the user can select the Print and Document Services Role to enable this feature. During a scanning job, the scan device acquires images from the documents that it scans and sends the images to the scan server. The scan server processes and stores the images.

A user initiates a scanning job from the user interface of a DSM device instead of from the user interface of an application running on a desktop computer. To configure the device for the scanning job, the user selects a scan process--a set of instructions for acquiring and processing images--that was previously created by an administrator. The scan process contains the following information:

-   A scan ticket that contains the image-acquisition settings for the DSM device.

-   A DSM scan server to send the acquired images.

-   A set of scan processing instructions to specify how the images acquired by the device are to be processed and stored by the DSM scan server.

    **Note**   In other contexts, the term *process* can have other meanings. For example, *process* might refer to a program instance that is scheduled and executed by an operating system. To avoid confusion with this usage, this section always uses the term *scan process* in full and never abbreviates it as *process*.

     

The communication protocols defined for Distributed Scan Management operate in conjunction with the Web Services on Devices for scanners (WS-Scan) protocol, which was introduced in Windows Vista. The WS-Scan protocol is based on the [Devices Profile for Web Services](http://go.microsoft.com/fwlink/p/?linkid=59069) (DPWS) specification. WS-Scan has these features:

-   Easy discovery of network-connected DSM devices.

-   An eventing model to inform the user of changes in the scanner hardware status and image-processing activity.

-   A seamless administrative experience for managing scanning operations.

In Windows Server 2008 R2, to complement WS-Scan, Distributed Scan Management provides the following features to meet the needs of organizations with many users:

-   A new user interface, the Windows Scan-Management Console (SMC), to enable IT administrators to manage scanning activities across an organization. Administrators use the SMC to define scan processes for various groups of users. The SMC is part of the Microsoft Management Console (MMC) Windows Server technology.

-   A DSM scan server, to process and store images acquired by a DSM device.

-   The SMC and the Distributed Scan Server are integrated with Active Directory, which stores scan processes and determines which scan processes are available to a user.

-   Full support for push-scan operations. In fact, Distributed Scan Management supports only push-scan operations. A scanning operation with Distributed Scan Management can be initiated only by a user who interacts directly with the DSM device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Overview%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


