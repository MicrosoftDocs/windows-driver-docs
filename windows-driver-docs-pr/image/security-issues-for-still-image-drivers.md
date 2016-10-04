---
title: Security Issues for Still Image Drivers
author: windows-driver-content
description: Security Issues for Still Image Drivers
MS-HAID:
- 'stillimg\_f5413645-1836-4e0c-a2e8-a053ca48e992.xml'
- 'image.security\_issues\_for\_still\_image\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ad795cf0-8bff-4b9b-ac43-94c74cc19d60
---

# Security Issues for Still Image Drivers


## <a href="" id="ddk-security-issues-for-still-image-drivers-si"></a>


It is important to remember that a user-mode minidriver can be called either from an application (through an image acquisition API), or from the still image event monitor (which is implemented as a Windows 2000 service). There are security implications associated with these multiple calling sources. For example, if a user-mode minidriver creates a mutex using the default security descriptor (by specifying a **NULL** security descriptor), one mutex cannot be shared between an instance of the minidriver called from the event monitor and one called from an image acquisition API.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Security%20Issues%20for%20Still%20Image%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


