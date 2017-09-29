---
title: Driver Security Guidance
description: This section contains information on enhancing driver security.
ms.assetid: 50D09948-8CE2-446F-A208-35F7B3795A6B
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver Security Guidance


This section contains information on enhancing driver security.

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
<tr class="even">
<td align="left"><p>[Driver security checklist](driver-security-checklist.md)</p></td>
<td align="left"><p>This topic provides a driver security checklist for driver developers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Threat modeling for drivers](threat-modeling-for-drivers.md)</p></td>
<td align="left"><p>Driver writers and architects should make threat modeling an integral part of the design process for any driver. This article provides guidelines for creating threat models for drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Windows security model for driver developers](windows-security-model.md)</p></td>
<td align="left"><p>This topic provides information about writing secure kernel-mode drivers for Windows. It describes how the Windows security model applies to drivers and explains what driver writers must do to improve the security of their devices.</p></td>
</tr>
</tbody>
</table>

## <span id="Kernel-mode_drivers"></span><span id="kernel-mode_drivers"></span><span id="KERNEL-MODE_DRIVERS"></span>Kernel-mode drivers


Kernel-mode drivers run in the trusted system address space and are, in effect, extensions of the operating system. Kernel-mode drivers must validate all data and addresses that originate with user-mode processes.

Numerous security and reliability issues apply to kernel-mode drivers. The following are a few examples of the areas in which kernel-mode drivers can be vulnerable to security threats:

-   Handling unexpected IOCTLs
-   Validating buffer lengths
-   Handling IOCTLs that permit FILE\_ANY\_ACCESS
-   Securing device objects
-   Securing Registry keys
-   Handling user-mode buffers
-   Using handles that are passed from user mode to kernel mode

For information about specific points at which kernel-mode drivers might be vulnerable, see the resources listed at the end of this topic and the white paper titled *Kernel-Mode Drivers: Fixing Common Driver Reliability Issues* available for download at <http://www.microsoft.com/whdc/driver/security/drvqa.mspx>. All writers of kernel-mode drivers should become familiar with this material.
 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Driver%20Security%20Guidance%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




