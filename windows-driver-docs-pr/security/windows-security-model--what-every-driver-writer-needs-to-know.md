---
title: Windows security model what every driver writer needs to know
description: This article provides information about writing secure kernel-mode drivers for the Microsoft Windows family of operating systems.
ms.assetid: 10C6CFB8-91B3-4C94-8AAC-9D9A1CD71409
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows security model: what every driver writer needs to know


**Last updated:**

-   July 7, 2004

This article provides information about writing secure kernel-mode drivers for the Microsoft Windows family of operating systems. It describes how the Windows security model applies to drivers and explains what driver writers must do to ensure the security of their devices.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Windows security model](windows-security-model.md)</p></td>
<td align="left"><p>The Windows security model is based primarily on per-object rights, with a small number of system-wide privileges. Objects that can be secured include, —but are not limited to, —processes, threads, events and other synchronization objects, as well as files, directories, and devices.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Windows security model scenario: creating a file](windows-security-model-scenario--creating-a-file.md)</p></td>
<td align="left"><p>The system uses the security constructs described in the Windows security model whenever a process creates a handle to a file or object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Driver security responsibility (Windows security model)](driver-security-responsibility--windows-security-model-.md)</p></td>
<td align="left"><p>This article describes driver security responsibility in the Windows security model.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Call to action and resources (Windows security model)](call-to-action-and-resources--windows-security-model-.md)</p></td>
<td align="left"><p>This article contains call to action recommendations and resources for the Windows security model.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Introduction"></span><span id="introduction"></span><span id="INTRODUCTION"></span>Introduction


The Windows security model is based on securable objects. Each component of the operating system must ensure the security of the objects for which it is responsible. Drivers, therefore, must safeguard the security of their devices and device objects.

This section summarizes how the Windows security model applies to kernel-mode drivers and what drivers must do to ensure the security of their devices. For some types of devices, additional device-specific requirements apply. See the device-specific documentation in the [Windows Driver Kit (WDK)](http://msdn.microsoft.com/library/windows/hardware/gg487463) for details.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Windows%20security%20model:%20what%20every%20driver%20writer%20needs%20to%20know%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




