---
title: History of Storport
author: windows-driver-content
description: History of Storport
ms.assetid: 1ddf45e1-06bb-42c6-9409-0f54143bb350
---

# History of Storport


Microsoft Windows Server 2003 and later versions provide Storport (*Storport.sys*), a storage port driver that is especially suitable for use with high-performance buses, such as fibre channel buses, and RAID adapters.

To extend the usefulness of the Storport interface, for Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, Microsoft has defined the Virtual Miniport (VMiniport) driver interface. This interface is designed for miniport drivers that currently have no strict association with the physical hardware.

In versions of Storport prior to Windows 7, Storport's system event log interface gave miniport drivers access to a small fraction of the capabilities of the kernel's system event log facility, which severely impacts the usefulness of miniport event log entries. For Windows 7, the new Storport event log interface gives miniport drivers full access to the capabilities of the Windows kernel event facility. This access enables miniport drivers to create event log entries that are truly useful in troubleshooting storage issues.

Storport offers a higher performance architecture and better fibre channel compatibility in Windows systems.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20History%20of%20Storport%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


