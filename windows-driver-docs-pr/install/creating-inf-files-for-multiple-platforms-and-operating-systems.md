---
title: Creating INF Files for Multiple Platforms and Operating Systems
description: Creating INF Files for Multiple Platforms and Operating Systems
ms.assetid: 61996c72-c5a7-4ff0-aeb3-6e77b77542c8
keywords: ["INF files WDK device installations , multiple platforms and operating systems", "multiple operating systems WDK , INF files", "cross-platform INF files WDK", "operating systems WDK , cross-operating system INF files"]
---

# Creating INF Files for Multiple Platforms and Operating Systems


## <a href="" id="ddk-creating-inf-files-for-multiple-platforms-and-operating-systems-dg"></a>


By using system-defined platform extensions to [INF file sections and directives](inf-file-sections-and-directives.md), you can create a single INF file for cross-platform installations. The extensions enable you to create *decorated* section names, which specify which sections and directives are relevant to each target platform and operating system. For example, you can create an INF file that installs a device only on x64-based systems, only on Itanium-based systems, only on x86-based systems, or on all systems that are supported by Windows 2000 and later versions of Windows.

The following table summarizes the system-supported platform extensions that can be added to the names of sections that support extensions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Platform extension</th>
<th align="left">Use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>.ntamd64</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on x64-based systems that are supported by Windows XP and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.ntia64</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on Itanium-based systems that are supported by Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>.ntx86</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on x86-based systems that are supported by Windows XP and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.nt</strong></p></td>
<td align="left"><p>In versions of Windows earlier than Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on all systems that are supported by the operating system.</p>
<p>Starting with Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on x86-based systems that are supported by the operating system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>(no platform extension)</p></td>
<td align="left"><p>In versions of Windows earlier than Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on all systems that are supported by the operating system.</p>
<p>Starting with Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on x86-based systems that are supported by the operating system.</p></td>
</tr>
</tbody>
</table>

 

**Important**  Starting with Windows Server 2003 SP1, INF files must decorate entries in the [**INF Models section**](inf-models-section.md) with .**ntia64** or .**ntamd64** platform extensions to specify non-x86 target operating system versions. These platform extensions are not required in INF files for x86-based target operating system versions or non-PnP driver INF files (such as file system driver INF files for x64-based architectures).

 

**Tip**   We highly recommend that you always decorate entries in the [**INF Models section**](inf-models-section.md) with platform extensions for target operating systems of Windows XP and later versions of Windows. For x86-based hardware platforms, you should avoid the use of the **.nt** platform extension and use **.ntx86** instead.

 

## In this section


-   [INF File Platform Extensions and x64-Based Systems](inf-file-platform-extensions-and-x64-based-systems.md)
-   [INF File Platform Extensions and x86-Based Systems](inf-file-platform-extensions-and-x86-based-systems.md)
-   [Cross-Platform INF Files](cross-platform-inf-files.md)
-   [Combining Platform Extensions with Other Section Name Extensions](combining-platform-extensions-with-other-section-name-extensions.md)

For an example of how to use INF file platform extensions to support cross-platform installations, see [Cross-Platform INF Files](cross-platform-inf-files.md).

For information about how to use platform extensions in combination with section name extensions, see [Combining Platform Extensions With Other Section Name Extensions](combining-platform-extensions-with-other-section-name-extensions.md).

For information about how to specify target operating systems through platform extensions, see [Combining Platform Extensions with Operating System Versions](combining-platform-extensions-with-operating-system-versions.md).

For information about a sample INF file that can be used to install drivers in multiple operating system versions, see [Sample INF File for Device Installation on Multiple Versions of Windows](sample-inf-file-for-device-installation-on-multiple-versions-of-windows.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Creating%20INF%20Files%20for%20Multiple%20Platforms%20and%20Operating%20Systems%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




