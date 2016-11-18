---
title: Overview of Boot Options in EFI
description: Overview of Boot Options in EFI
ms.assetid: 2237d321-75e6-4723-9f08-484bd9097360
keywords: ["NVRAM boot options WDK , about EFI NVRAM boot options", "EFI NVRAM boot options WDK , about EFI NVRAM boot options", "globally-defined variables WDK boot options", "boot options WDK , variables", "boot entry IDs WDK", "EFI boot entry IDs WDK", "identifiers WDK boot options", "boot entries WDK", "Bootcfg tool"]
---

# Overview of Boot Options in EFI


## <span id="ddk_overview_of_boot_options_in_efi_tools"></span><span id="DDK_OVERVIEW_OF_BOOT_OPTIONS_IN_EFI_TOOLS"></span>


Like the boot options on a system with BIOS firmware, there are two types of boot options in EFI NVRAM:

-   *Globally-defined variables* that apply to all bootable devices and bootable programs on the computer.

-   *Boot option variables* that apply only to a particular load configuration of a bootable device or program, such as an operating system. The system-specific variables comprise a boot entry for each configuration of a bootable device or bootable program on the computer.

The Bootcfg tool (discussed in [Editing Boot Options in EFI](editing-boot-options-in-efi.md) and documented in Windows Help and Support) allows you to view and edit the boot options in EFI NVRAM.

The following sample shows a Bootcfg display of a computer with an Itanium processor.

```
Boot Options
------------
Timeout:             30
Default:             \Device\HarddiskVolume3\WINDOWS
CurrentBootEntryID:  1

Boot Entries
------------

Boot entry ID:    1
OS Friendly Name: Windows Server 2003, Enterprise
OsLoadOptions: /debug /debugport=COM1 /baudrate=57600
BootFilePath:     \Device\HarddiskVolume1\EFI\Microsoft\WINNT50\ia64ldr.efi
OsFilePath:       \Device\HarddiskVolume3\WINDOWS

Boot entry ID:    2
OS Friendly Name: EFI Shell [Built-in]
```

The following table describes the elements of the Bootcfg display of boot data in EFI NVRAM.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Description</th>
<th align="left">Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Boot Options</strong></p></td>
<td align="left"><p>Contains options that apply to all boot entries.</p></td>
<td align="left"><p>(Section heading)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Timeout</strong></p></td>
<td align="left"><p>Determines how long the boot menu is displayed. When this value expires, the boot loader loads the default operating system.</p></td>
<td align="left"><pre space="preserve"><code>Timeout:   30</code></pre></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Default</strong></p></td>
<td align="left"><p>Specifies the location of the default operating system.</p></td>
<td align="left"><pre space="preserve"><code>\Device\HarddiskVolume3\WINDOWS</code></pre></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CurrentBootEntryID</strong></p></td>
<td align="left"><p>Identifies the boot entry that was used to start the current session of the operating system.</p></td>
<td align="left"><pre space="preserve"><code>CurrentBootEntryID:  1</code></pre></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Boot Entries</strong></p></td>
<td align="left"><p>Contains system-specific data. It is comprised of one or more <em>boot entries</em> for each operating system or bootable program installed on the computer.</p>
<p>A <em>boot entry</em> is a set of options that defines a load configuration for an operating system or bootable program.</p></td>
<td align="left"><p>(Section heading)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Boot entry ID</strong></p></td>
<td align="left"><p>Identifies the boot entry to Bootcfg. This value changes when you reorder the boot entries.</p>
<p>This is not the <em>EFI boot entry ID</em>, which is a persistent identifier for the EFI components.</p></td>
<td align="left"><pre space="preserve"><code>Boot entry ID:    1</code></pre></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>OS Friendly Name</strong></p></td>
<td align="left"><p>Represents the boot entry in the boot menu.</p></td>
<td align="left"><pre space="preserve"><code>Windows Server 2003,
Enterprise</code></pre></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OsLoadOptions</strong></p></td>
<td align="left"><p>Specifies the <em>boot parameters</em> for the entry. <em>Boot parameters</em> are commands to enable, disable, and configure features of the operating system. The EFI Boot Manager passes these parameters to the bootable device or system to be interpreted and implemented.</p>
<p>For a list of the boot parameters that are related to driver debugging and testing, see [Boot.ini Boot Parameter Reference](https://msdn.microsoft.com/library/windows/hardware/ff542248).</p></td>
<td align="left"><pre space="preserve"><code>OsLoadOptions: /debug
/debugport=COM1 /baudrate=57600</code></pre></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>BootFilePath</strong></p></td>
<td align="left"><p>Specifies the location of the EFI boot loader for the operating system. On EFI-based systems, each operating system or bootable device has its own copy of the boot loader on the EFI partition.</p>
<p>In EFI NVRAM, the boot loader file path is stored as a binary EFI device path that uses a globally unique identifier (GUID) to identify the EFI partition .</p>
<p>Bootcfg uses the NT device name of the partition in its path display.</p></td>
<td align="left"><pre space="preserve"><code>BootFilePath: \Device\HarddiskVolume1
\EFI\Microsoft\WINNT50\ia64ldr.efi</code></pre></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OsFilePath</strong></p></td>
<td align="left"><p>Specifies the location of the operating system.</p>
<p>In NVRAM, this value is stored as an EFI device path that uses the GUID of the boot disk partition and the path to the directory that contains the operating system.</p>
<p>Bootcfg uses the NT device name of the partition in its path display.</p></td>
<td align="left"><pre space="preserve"><code>OsFilePath: \Device\HarddiskVolume3
\WINDOWS</code></pre></td>
</tr>
</tbody>
</table>

 

In addition, there is an important element of an EFI boot entry that Bootcfg does not display, the *EFI boot entry ID*. The EFI boot entry is a unique identifier for an EFI boot entry. This identifier is assigned when the boot entry is created, and it does not change. It represents the boot entry in several lists, including the *BootOrder* array, and it is the name of the directory on disk in which the system stores data related to the boot entry, including backup copies of the boot entry. An EFI boot entry ID has the format, Boot*xxxx*, where *xxxx* is a hexadecimal number that reflects the order in which the boot entries are created.

**Note**   The **Boot entry ID** field in Bootcfg and the boot entry number in Nvrboot do not display the EFI boot entry ID. The Bootcfg and Nvrboot IDs are line numbers that represent the order of the boot entry in the **Boot Entries** section and change when the entries are reordered.

 

For a detailed description of boot options on Itanium-based systems, see the Extensible Firmware Interface Specification. You can download a copy of the specification from the [Intel Extensible Firmware Interface](http://go.microsoft.com/fwlink/p/?linkid=10596) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Overview%20of%20Boot%20Options%20in%20EFI%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




