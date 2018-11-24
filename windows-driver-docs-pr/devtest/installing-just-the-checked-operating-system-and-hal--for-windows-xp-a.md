---
title: Install Checked Operating System and HAL (Windows XP and Windows Server 2003)
description: Installing Just the Checked Operating System and HAL (For Windows XP and Windows Server 2003)
ms.assetid: 51175951-9267-4d92-8b47-4dd2155f4e56
keywords:
- checked builds WDK , installing
- free builds WDK
- retail builds WDK
- HAL WDK
- partial checked builds WDK
- names WDK checked builds
- copying checked files
- Boot.ini files WDK , checked builds
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Just the Checked Operating System and HAL (For Windows XP and Windows Server 2003)


## <span id="ddk_installing_just_the_checked_operating_system_and_hal_tools"></span><span id="DDK_INSTALLING_JUST_THE_CHECKED_OPERATING_SYSTEM_AND_HAL_TOOLS"></span>


Instead of installing the complete checked build on your computer, you can install the free build of the system, and then install the checked versions of the operating system image and HAL. If you use this procedure, you can configure the boot loader to provide you with two boot options. The first boot option is for the free build. The second boot option starts the system using the checked operating system image and HAL, but uses free versions of all other system components.

This approach, compared to installing the complete checked build, provides the following advantages:

-   Drivers get the benefit of the operating-system and HAL debug checks. At the same time, because free versions of system components other than the operating system and HAL are being used, the performance impact on the entire system is minimized.

-   A single installation (and thus one system directory, one set of executable components, and one set of registry parameters) can use either the checked or the free version of the operating system image and HAL, as determined at boot time.

To install the checked versions of the operating system image and HAL, you must copy the appropriate files from the checked distribution medium to the %SystemRoot%\\system32 directory using new, unique file names. Then you must instruct the system to offer an option that uses these files during system startup. You should keep in mind the following important guidelines when you install checked operating system and HAL images on an otherwise free installation:

-   The operating system image and HAL must be kept in sync at all times. Therefore, if you use a checked version of the operating system image, you must also use the checked version of the HAL (and vice versa). Failure to keep a system's operating system image and HAL coordinated can make the system unbootable.

-   Do not overwrite the free versions of the operating system image and the HAL that are installed during the installation of the free build. Overwriting the free versions of the operating system image and HAL can make the system unbootable, and can make it difficult to recover from errors. Therefore, always be careful to use new, unique file names when you copy the checked versions of the operating system and HAL to the %SystemRoot%\\system32 directory.

-   Ensure that the checked distribution you use is the same Service Pack number as that of the free system. For example, if you are installing the checked operating system image and HAL on a system for which Service Pack 2 of a free build system is installed, make certain that the checked distribution you use is also Service Pack 2.

The steps to install a partial checked build are as follows:

### <span id="step_1__identifying_the_files_to_install"></span><span id="STEP_1__IDENTIFYING_THE_FILES_TO_INSTALL"></span>Step 1: Identifying the Files To Install

Your first step in installing a partial checked build is to determine the version of the operating system image and HAL files that were used to install the free build on your system.

Several different versions of the operating system and HAL images are supplied on the NT-based operating system distribution medium. These different versions exist to support different combinations of processors and other system hardware. When the operating system software is installed, the installation procedure automatically identifies which operating system image and HAL image to use, and copies the appropriate files from the distribution medium to the system's %SystemRoot%\\system32 directory.

The operating system image file that is installed depends on whether one or multiple processors are to be supported, and on whether Physical Address Extension (PAE) is supported (PAE is active on systems with more than 4 GB of physical memory). The file names on the distribution medium are as follows:

<span id="NTOSKRNL.EXE"></span>ntoskrnl.exe  
Uniprocessor x86 architecture systems with 4 GB of physical memory or less.

<span id="NTKRNLPA.EXE"></span>ntkrnlpa.exe  
Uniprocessor x86 architecture systems with PAE support.

<span id="NTKRNLMP.EXE"></span>ntkrnlmp.exe  
Multiprocessor x86 architecture systems with 4 GB of physical memory or less.

<span id="NTKRPAMP.EXE"></span>ntkrpamp.exe  
Multiprocessor x86 architecture systems with PAE support.

Likewise, there are several different names for the HAL.

During system installation, the installation procedure determines the appropriate operating system image and HAL to install on your system. The selected files are copied to the %SystemRoot%\\system32 directory during installation, using fixed, well-known, names. The use of these fixed names makes it easy for the loader to locate these files at boot time. The fixed names for these files are:

<span id="NTOSKRNL.EXE"></span>ntoskrnl.exe  
Operating system image for x86 systems with 4 GB of physical memory or less.

<span id="NTKRNLPA.EXE"></span>ntkrnlpa.exe  
Operating system image for x86 systems with more than 4 GB of physical memory.

<span id="HAL.DLL"></span>hal.dll  
Loadable HAL image.

Note that in some cases, depending on the system's hardware configuration, one or more of the files may be renamed to the appropriate fixed name. In other cases, the file name on the distribution medium is the same as the required fixed file name.

To install the checked operating system image and HAL, you must first determine the original names of the images that were copied to your system during system installation. To perform this, examine the file %SystemRoot%\\repair\\setup.log. This is a hidden file, so you need to change its attributes before you can view it using the **dir** command.

The setup.log file lists the files that were copied from the distribution medium to the %SystemRoot%\\system32 directory during the system installation process.

An example of a setup.log file is as follows:

```
[Paths]
TargetDirectory = "\WINNT"
TargetDevice = "\Device\Harddisk0\Partition1"
SystemPartitionDirectory = "\"
SystemPartition = "\Device\Harddisk0\Partition1"
[Signature]
Version = "WinNt5.1"
[Files.SystemPartition]
NTDETECT.COM = "NTDETECT.COM","f41f"
ntldr = "ntldr","3e8b5"
arcsetup.exe = "arcsetup.exe","379db"
arcldr.exe = "arcldr.exe","2eca9"
[Files.WinNt]
\WINNT\system32\drivers\kbdclass.sys = "kbdclass.sys","e259"
\WINNT\system32\drivers\mouclass.sys = "mouclass.sys","7e78"
\WINNT\system32\drivers\uhcd.sys = "uhcd.sys","10217"
\WINNT\system32\drivers\usbd.sys = "usbd.sys","5465"
(...several similar lines omitted...)
\WINNT\system32\framebuf.dll = "framebuf.dll","10c84"
\WINNT\system32\hal.dll = "halmacpi.dll","2bedf"
\WINNT\system32\ntkrnlpa.exe = "ntkrpamp.exe","1d66a6"
\WINNT\system32\ntoskrnl.exe = "ntkrnlmp.exe","1ce5c5"
\WINNT\inf\mdmrpci.inf = "mdmrpci.inf","96a3"
```

In the sample setup.log file, you can see that two operating system image files were copied to the \\winnt\\system32 directory (which is %SystemRoot%\\system32) during installation. The file ntkrpamp.exe is copied from the distribution medium to ntkrnlpa.exe and the file ntkrnlmp.exe is copied from the distribution medium to ntoskrnl.exe. From this sample, you can also see that the HAL file (with the fixed name hal.dll in the %SystemRoot%\\system32 directory) was originally named halmacpi.dll.

**Warning**   Some HAL files have deceptively similar names. For example, halacpi.dll and halapic.dll are two commonly used HALs. Be careful to use the correct version of the HAL for your system. Selecting the wrong HAL will result in a system that is not bootable.

 

### <span id="step_2__copying_the_checked_files"></span><span id="STEP_2__COPYING_THE_CHECKED_FILES"></span>Step 2: Copying the Checked Files

Now that you know the names of the files that were used during your system installation, you can copy the checked versions of these files to your system. Find the files you have identified in the checked distribution kit. Then copy these files to the %SystemRoot%\\system32 directory of your system, giving them new, unique, file names. The copies of these files must follow the 8.3 naming convention. One way to ensure unique, 8.3-compliant file names is to rename the file types from their original file types (.dll or .exe) to .chk when they are copied. Thus, using the example in Step 1, you would copy files from the checked distribution kit as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">If the original file name in the checked distribution is:</th>
<th align="left">Copy it to the following file name in %SystemRoot%\system32:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ntkrnlmp.exe</p></td>
<td align="left"><p>ntkrnlmp.chk</p></td>
</tr>
<tr class="even">
<td align="left"><p>ntkrpamp.exe</p></td>
<td align="left"><p>ntkrpamp.chk</p></td>
</tr>
<tr class="odd">
<td align="left"><p>halmapic.dll</p></td>
<td align="left"><p>halmapic.chk</p></td>
</tr>
</tbody>
</table>

 

Some files in the checked distribution are provided in compressed form. These files are indicated with an underscore character as the last character in their file type. For example, if you look for the file halapic.dll in the checked build distribution kit, you will find the file halapic.dl\_, which is the correct file, but in compressed form.

To decompress compressed files from the checked distribution, use the Expand utility (%SystemRoot%\\system32\\expand.exe). For example, to expand halapic.dl\_ and name the expanded file as halapic.chk, you can use the following command from a command prompt window:

```
> expand halapic.dl_ halapic.chk
```

### <span id="step_3__editing_boot_ini"></span><span id="STEP_3__EDITING_BOOT_INI"></span>Step 3: Editing boot.ini

After you have copied the checked files to the %SystemRoot%\\system32 directory, you must create a boot-time option that allows the system to start using these checked files. To perform this, edit the boot.ini file.

For general instructions, see [Editing the boot.ini File](editing-the-boot-ini-file.md).

In this specific case, you need to create a new boot-time option that allows you to start the system with the checked version of the operating system image and HAL that you have installed.

Locate the line in the **\[operating systems\]** section of boot.ini that refers to your Windows installation. Make a second copy of it, and add the following parameters to the end of the copied line:

```
/kernel=KernelFile /hal=HalFile 
```

where *KernelFile* is the name of the checked version of the operating system image file that you previously copied from the checked distribution kit, and *HalFile* is the name of the checked version of the HAL that you previously copied from the checked distribution kit.

If the line that describes your operating system contains the **/PAE** parameter, make sure that you use the checked version of the operating system image with PAE support. If the line that describes your operating system does not have the **/PAE** parameter, use the checked version of the operating system image without PAE support.

You should also change the quoted text on the new line, so that you can identify which line is the free build and which line is the partial checked build.

An example of such a boot.ini file is as follows:

```
[boot loader]
timeout=30
default=multi(0)disk(0)rdisk(0)partition(1)\WINNT
[operating systems]
multi(0)disk(0)rdisk(0)partition(1)\WINNT="Microsoft Windows 2000 Professional" /fastdetect
multi(0)disk(0)rdisk(0)partition(1)\WINNT="Windows 2000 Checked" /fastdetect /kernel=ntoskrnl.chk /hal=halacpi.chk
```

If you use the checked build with a kernel debugger, you should also add the proper debugging-related parameters. (The **/kernel** and **/hal** parameters do not enable debugging automatically.) For details, see [Editing the boot.ini File](editing-the-boot-ini-file.md).

After you have made the changes, save the changes and exit from the editor. The next time you boot this system, a new operating system boot option will be displayed that allows you to select your checked operating system image and HAL.

### <span id="installing_additional_checked_files"></span><span id="INSTALLING_ADDITIONAL_CHECKED_FILES"></span>Installing Additional Checked Files

After you have the checked operating system and HAL installed, you have the option to install additional checked components. You can replace the installed, free versions of a few key components with their checked counterparts from the checked distribution medium. This can be helpful, for example, when you are writing a driver that exists within a stack of other devices. By replacing the free versions of the drivers that are above and below your driver in the stack, you will enable additional error checking in these components. This could help you identify problems in your driver more quickly and easily.

When replacing free drivers with their checked counterparts, there is no way to easily provide alternate images for system-supplied driver components. Thus, when you replace free drivers with checked drivers on your system, the checked drivers will be used when either the free or checked version of the operating system image and HAL is started. Therefore, you might want to rename (or copy) the original free versions of any drivers that you replace with their checked counterparts, so that you can restore the free drivers later.

Finally, note that any time you change one of the standard files that exist in one of the system directories (such as %SystemRoot%\\system32) Windows File Protection (WFP) will restore that file to its original state unless WFP is first disabled. If a debugger is attached to your system, you can temporarily disable WFP by changing the following registry value:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
SFCDisable:REG_DWORD:2
```

Setting **SFCDisable** to a value of 2 disables WFP for the next boot (only). A value of 0 (the default) enables WFP. For a description of the features of WFP, see the Microsoft Windows SDK. For more information about the WFP registry settings, see [Microsoft Knowledge Base Article Q222473](http://go.microsoft.com/fwlink/p/?linkid=38360).

 

 





