---
title: Error Record Persistence
author: windows-driver-content
description: Error Record Persistence
ms.assetid: fe43f93a-59bd-4158-ad00-8fef595528cb
keywords:
- Windows Hardware Error Architecture WDK , error record persistence
- WHEA WDK , error record persistence
- errors WDK WHEA , error record persistence
- error record persistence WDK WHEA
- saving hardware error records WDK WHEA
- storing hardware error records WDK WHEA
- writing hardware error records WDK WHEA
- retrieving hardware error records WDK WHEA
- reading hardware error records WDK WHEA
- hardware errors WDK WHEA , error record persistence
- platform-specific hardware error driver plug-ins WDK WHEA , error record persistence
- PSHED plug-ins WDK WHEA , error record persistence
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Error Record Persistence


The PSHED exposes an interface to the operating system that allows the Windows kernel to save and retrieve error records to or from the system's persistent data storage. Error source control operations include the following:

-   Write an error record to the persistent data storage

-   Read an error record from the persistent data storage

-   Clear an error record from the persistent data storage

If a hardware platform does not implement hardware or firmware that is compatible with the error record persistence mechanisms that are supported by the PSHED, the platform vendor must implement a PSHED plug-in that participates in error record persistence. This PSHED plug-in interfaces with the error record persistence mechanism that is implemented by the hardware platform.

For more information about how to implement a PSHED plug-in that participates in error record persistence, see [Participating in Error Record Persistence](participating-in-error-record-persistence.md).

For more information about error record persistence, see [Error Record Persistence Mechanism](error-record-persistence-mechanism.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Error%20Record%20Persistence%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


