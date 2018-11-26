---
title: History of Storport
description: History of Storport
ms.assetid: 1ddf45e1-06bb-42c6-9409-0f54143bb350
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# History of Storport


Microsoft Windows Server 2003 and later versions provide Storport (*Storport.sys*), a storage port driver that is especially suitable for use with high-performance buses, such as fibre channel buses, and RAID adapters.

To extend the usefulness of the Storport interface, for Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, Microsoft has defined the Virtual Miniport (VMiniport) driver interface. This interface is designed for miniport drivers that currently have no strict association with the physical hardware.

In versions of Storport prior to Windows 7, Storport's system event log interface gave miniport drivers access to a small fraction of the capabilities of the kernel's system event log facility, which severely impacts the usefulness of miniport event log entries. For Windows 7, the new Storport event log interface gives miniport drivers full access to the capabilities of the Windows kernel event facility. This access enables miniport drivers to create event log entries that are truly useful in troubleshooting storage issues.

Storport offers a higher performance architecture and better fibre channel compatibility in Windows systems.

 

 




