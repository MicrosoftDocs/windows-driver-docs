---
title: Windows Driver Model (WDM)
author: windows-driver-content
description: This section describes the Windows Driver Model (WDM), and discusses types of WDM drivers, device configuration, driver layering, and WDM versioning.
MS-HAID:
- 'WDMIntro\_ef015643-817a-486f-8416-1c805c680c6a.xml'
- 'kernel.windows\_driver\_model'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9e76c5a8-a19a-44cf-867a-b2246ea8eaf1
keywords: ["kernel-mode drivers WDK , WDM drivers"]
---

# Windows Driver Model (WDM)


This section describes the *Windows Driver Model* (WDM), and discusses types of WDM drivers, device configuration, driver layering, and WDM versioning. WDM simplifies the design of kernel-mode drivers that are written to run on multiple versions of the Windows operating system.

## <a href="" id="ddk-windows-driver-model-kg"></a>


## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Introduction to WDM](introduction-to-wdm.md)</p></td>
<td><p>To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the <em>Windows Driver Model</em> (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called <em>WDM drivers</em>.</p></td>
</tr>
<tr class="even">
<td><p>[Types of WDM Drivers](types-of-wdm-drivers.md)</p></td>
<td><p>There are three kinds of WDM drivers: bus drivers, function drivers, and filter drivers.</p></td>
</tr>
<tr class="odd">
<td><p>[Device Configurations and Layered Drivers](device-configurations-and-layered-drivers.md)</p></td>
<td><p>For the most common kinds of devices, the Windows Driver Kit (WDK) supplies a sample set of fully functional system drivers. Individual sample drivers can be used as models when developing new drivers for similar kinds of devices. However, the system's drivers had an additional design requirement: to make it easy to develop new device drivers. Consequently, many of the system's drivers have a layered architecture so that certain drivers can be reused to support new drivers for similar devices.</p></td>
</tr>
<tr class="even">
<td><p>[WDM Versions](wdm-versions.md)</p></td>
<td><p>Later versions of WDM generally support all the features available in earlier versions of WDM; that is, each new version of WDM is a superset of the previous WDM version. When possible, a cross-system driver should conform to the lowest WDM version on any operating system.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Driver%20Model%20%28WDM%29%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


