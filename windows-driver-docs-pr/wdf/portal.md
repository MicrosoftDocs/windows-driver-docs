---
title: Windows Driver Frameworks
description: Windows Driver Frameworks
ms.assetid: a3243ae3-1bc3-42d5-8975-b0588ae94dba
keywords: ["Kernel-Mode Driver Framework WDK", "KMDF WDK"]
---

# Windows Driver Frameworks


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>What is it</strong></p>
<p>Windows Driver Frameworks (WDF) is a set of libraries that you can use to develop device drivers that are interoperable with Windows. WDF is comprised of Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF).</p>
<p><strong>Where applicable</strong></p>
<p>A KMDF or UMDF driver is the software installed on the computer that communicates with the hardware to make the device function. If the device belongs to a device class supported by Microsoft, Windows loads one of the in-box class drivers for the device. Otherwise, a custom driver must be provided by the hardware manufacturer or a third party vendor. The user installs the driver for the device when the device is first detected by Windows. After successful installation, Windows loads the client driver every time the device is attached and unloads the driver when the device is detached from the host computer.</p>
<p>You can develop a custom driver for a hardware device by using WDF or the [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM). The topics in this section describe the callback functions that a driver needs to provide, and the device driver interfaces (DDIs) that the driver must call.</p>
<p><strong>Developer audience</strong></p>
<p>This section is intended for use by C/C++ programmers. Before you use this section, you should understand basic driver development. For more information, see [Getting Started with Windows Drivers](https://msdn.microsoft.com/library/windows/hardware/ff554690).</p>
<p><strong>Development requirements</strong></p>
<p>To write WDF drivers, you need the Windows Driver Kit (WDK), which is integrated with Microsoft Visual Studio Professional. The WDK contains resources that are required for driver development, such as headers, libraries, and tools. Optionally, you can download driver samples and debugging tools.</p>
<ul>
<li>How to Get [Visual Studio](https://go.microsoft.com/fwlink/p/?LinkId=533470) and the [WDK](https://go.microsoft.com/fwlink/p/?LinkId=733614)</li>
<li>[Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507 ) repository on GitHub</li>
<li>[Download and Install Debugging Tools for Windows](http://msdn.microsoft.com/library/windows/hardware/ff551063)</li>
</ul>
<p>To create a driver that uses KMDF or UMDF, you can use a template in Visual Studio. For step-by-step guidance, see [Writing your first driver](https://msdn.microsoft.com/library/windows/hardware/ff554811). You can use Visual Studio to build WDF drivers for Windows Vista and later. For general information about developing drivers in Visual Studio, see [Developing, Testing, and Deploying Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment).</p>
<p><strong>Related resources</strong></p>
<ul>
<li>[Developing Drivers with the Windows Driver Foundation: Reference Book](developing-drivers-with-wdf.md)</li>
<li>[WDF source code on GitHub](https://github.com/Microsoft/Windows-Driver-Frameworks)</li>
<li>[Windows driver samples on GitHub](https://github.com/Microsoft/Windows-Driver-Samples)</li>
</ul></td>
<td align="left"><p><strong>WDF Documentation Sections</strong></p>
<ul>
<li><p>[What's New for WDF Drivers](what-s-new-for-wdf-drivers.md)</p>
<p>Describes the new features for WDF in Windows 10.</p></li>
<li><p>[KMDF Version History](kmdf-version-history.md)</p></li>
<li><p>[UMDF Version History](umdf-version-history.md)</p>
<p>Summarizes which WDF versions ship with different versions of Windows, and lists new features and improvements in Windows 8.1.</p></li>
<li><p>[Building and Loading a WDF Driver](building-and-loading-a-kmdf-driver.md)</p>
<p>Get information about how to build a WDF driver using Visual Studio in Windows 8.1.</p></li>
<li><p>[Additional Topics for KMDF Drivers](kmdf-only-functionality.md)</p>
<p>Describes the WDF functionality that is available in KMDF, but not UMDF.</p></li>
<li><p>[WDF Reference](https://msdn.microsoft.com/library/windows/hardware/dn265590)</p>
<p>Gives specifications for callbacks, support routines, structures, and interfaces used by WDF drivers.</p></li>
<li><p>[Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591)</p>
<p>Lists all of the driver-supplied callbacks and system-supplied methods and their availability in KMDF and UMDF</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Windows%20Driver%20Frameworks%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




