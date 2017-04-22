---
title: Security Issues for WIA Drivers
author: windows-driver-content
description: Security Issues for WIA Drivers
ms.assetid: 5d8fc015-cbf5-43a3-8f65-3ebb17754417
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security Issues for WIA Drivers


## <a href="" id="ddk-security-issues-for-wia-drivers-si"></a>


Running services under a **LocalSystem** account can be dangerous, because **LocalSystem** is essentially Administrator and, therefore, has access to virtually any resource on the machine. Design flaws or buggy code in a service running under **LocalSystem** might result in an escalation of privilege for a destructive user. Windows XP introduced two new built-in service accounts, **LocalService** and **NetworkService**, specifically designed to mitigate the consequences of a service compromise. These two new accounts are restricted user accounts without any special privileges, except "Login as service".

In keeping with this security initiative, the WIA service runs under the **LocalService** account in Microsoft Windows Server 2003 and later operating system versions.

Prior to Windows Server 2003, the WIA service and WIA drivers were developed on the assumption that they would run under **LocalSystem**. This changed with Windows Server 2003 and has several ramifications that driver developers need to be aware of. This section contains a list of common problems that a WIA driver developer might experience, including possible ways to resolve them.

Following the practices outlined in this document ensures that the WIA drivers developed will function correctly whether running on Windows XP, Windows Server 2003, or later operating system versions.

[Common WIA Security Problems](common-wia-security-problems.md)

[WIA Security Best Practices](wia-security-best-practices.md)

For additional information about device driver security, see the [Securing Device Objects](https://msdn.microsoft.com/library/windows/hardware/ff563688) and [Creating Secure Device Installations](https://msdn.microsoft.com/library/windows/hardware/ff540212) sections.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Security%20Issues%20for%20WIA%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


