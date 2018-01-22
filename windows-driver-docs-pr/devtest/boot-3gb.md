---
title: /3GB
description: On 32-bit versions of Windows, the /3GB parameter enables 4 GT RAM Tuning, a feature that enlarges the user-mode virtual address space to 3 GB and restricts the kernel-mode components to the remaining 1 GB.
ms.assetid: ebb5ab9f-9761-489f-9c69-e72d92252832
keywords: ["/3GB", "/3GB Driver Development Tools"]
topic_type:
- apiref
api_name:
- /3GB
api_type:
- NA
---

/3GB
====

On 32-bit versions of Windows, the **/3GB** parameter enables *4 GT RAM Tuning*, a feature that enlarges the user-mode virtual address space to 3 GB and restricts the kernel-mode components to the remaining 1 GB.

``` syntax
    /3GB [ /userva=SizeInMB ] 

   
```

## Subparameters


<a href="" id="--------userva------"></a> **/userva**   
Specifies an alternate amount of user-mode virtual address space for operating systems booted with the **/3GB** parameter.

<a href="" id="-------sizeinmb------"></a> *SizeInMB*   
Specifies the amount of memory, in megabytes, for user-mode virtual address space. This variable can have any value between 2048 (2 GB) and 3072 (3 GB) megabytes in decimal notation. Windows uses the remaining address space (4 GB minus the specified amount) as its kernel-mode address space.

### Comments

The **/3GB** parameter is supported on Windows Server 2003, Windows XP, and Windows 2000. On Windows Vista and later versions of Windows, use the **IncreaseUserVA** element in BCDEdit.

On Windows, by default, the lower 2 GB are reserved for user-mode programs and the upper 2 GB are reserved for kernel-mode programs. You can use this parameter to test the performance of your driver when it is running in a 1 GB kernel.

The *4 GT RAM Tuning* feature is fully functional on Microsoft Windows 2000 Advanced Server, Microsoft Windows 2000 Datacenter Server, and all editions of Windows XP, Windows Server 2003, Windows Vista, and later versions of Windows. See [4-Gigabyte Tuning (Windows)](https://msdn.microsoft.com/library/windows/desktop/bb613473) for additional information about this feature.

On other versions of Windows 2000, this feature restricts the kernel to addresses above the 3 GB boundary. However, user-mode applications cannot access more than 2 GB of address space.

The **/userva** subparameter is designed for computers that need more than 2 GB but less than 3 GB of user-mode address space, particularly those that are running memory-intensive user-mode programs. When used without the /**3GB** parameter, **/userva** is ignored.

The **/3GB** and **/userva** parameters are valid only on boot entries for 32-bit versions of Windows on computers with x86 or x64-based processors.

To take advantage of the 3 GB available to user-mode programs, the program must be linked with the **/LARGEADDRESSAWARE** option.

On 64-bit versions of Windows Server 2003, the system automatically expands the virtual address space available to 32-bit user-mode programs linked with the **/LARGEADDRESSAWARE** option as needed without the **/3GB** boot parameter. On Windows Server 2003 RTM (without Service Pack 1), these 32-bit programs can access up to 3 GB of virtual address space. On Windows Server 2003 with Service Pack 1, they can access up to 4 GB of virtual address space. Native 64-bit user-mode programs can access up to 8 TB of virtual address space.

Booting with the **/3GB** parameter decreases the amount of kernel virtual address space on the system. In order to fit all of the kernel resources within the remaining 1 GB of virtual memory, NT-based Windows operating systems prior to Windows Vista restrict physical memory to frames below the 16 GB physical boundary. Windows Vista and later versions of Windows restrict physical memory to frames below the 64 GB boundary. Because allocation of memory resources in Windows Vista and later is dynamic and, therefore, more adaptable and efficient, the system can devote more memory space to addressing, thereby accommodating more physical memory.

The following table lists the physical memory limits of 32-bit Windows operating systems that support the use of more than 4 GB of physical memory with and without the **/3GB** boot parameter.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operating system</th>
<th align="left">Physical memory limit without /3GB</th>
<th align="left">Physical memory limit with /3GB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows Vista</p></td>
<td align="left"><p>4 GB</p></td>
<td align="left"><p>4 GB (no effect)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Server 2008 Enterprise</p></td>
<td align="left"><p>64 GB</p></td>
<td align="left"><p>64 GB</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2008 Datacenter Edition</p></td>
<td align="left"><p>64 GB</p></td>
<td align="left"><p>64 GB</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Server 2003, Enterprise Edition</p></td>
<td align="left"><p>64 GB</p></td>
<td align="left"><p>16 GB</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2003, Datacenter Edition</p></td>
<td align="left"><p>64 GB</p></td>
<td align="left"><p>16 GB</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP (all editions)</p></td>
<td align="left"><p>4 GB</p></td>
<td align="left"><p>4 GB (no effect)</p></td>
</tr>
</tbody>
</table>

 

On Windows XP, some drivers, especially video adapter drivers with onboard RAM, cannot run with the **/3GB** parameter because they require more address space than the 1 GB kernel address space permits.

### Examples

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Windows Server 2003, Enterprise" /fastdetect /3GB

multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Windows Server 2003, Enterprise" /fastdetect /3GB /userva=3030
```

### Bootcfg Commands

```
bootcfg /raw "/3GB" /A /ID 1
bootcfg /raw "/3GB /userva=3030" /A /ID 2
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/3GB%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




