---
title: Storport Idle Power Management
author: windows-driver-content
description: Storport Idle Power Management
ms.assetid: 1ad47775-4d7a-47c4-83eb-774e58c863d3
---

# Storport Idle Power Management


Storport Idle Power Management (IPM) allows the classpnp and disk class drivers to send the SCSI Stop Unit command to the disk device when it has been idle for some period of time. The idle period is configurable by the system administrator. The Storport miniport driver is responsible for how the command is used by the Storport miniport driver to conserve power. The following sections describe IPM in more detail.

[IPM Scope](ipm-scope.md)

[IPM Assumptions](ipm-assumptions.md)

[IPM Configuration and Usage](ipm-configuration-and-usage.md)

[IPM Hard Disk Drive Idle Timeout](ipm-hard-disk-drive-idle-timeout.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storport%20Idle%20Power%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


