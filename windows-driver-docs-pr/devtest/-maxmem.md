---
title: /maxmem
description: The /maxmem parameter limits the physical memory available to Windows.
ms.assetid: 7c405a33-f5aa-4c61-bce7-8885554ec0c2
keywords: ["/maxmem Driver Development Tools"]
topic_type:
- apiref
api_name:
- /maxmem
api_type:
- NA
---

/maxmem
=======

The **/maxmem** parameter limits the physical memory available to Windows.

``` syntax
    /maxmem=SizeInMB 

   
```

## Subparameters


<a href="" id="-------sizeinmb------"></a> *SizeInMB*   
Specifies the maximum amount of physical memory available to Windows. Enter a decimal number that represents the amount of memory in megabytes.

### Comments

This parameter actually limits Windows to memory addresses less than or equal to the specified value. Because some memory within the remaining address space might be reserved for nonsystem use, the actual memory available to Windows might be less than the amount that you specify.

The **/maxmem** parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000. On Windows Server 2003 and Windows XP, use [**/burnmemory**](-burnmemory.md) to limit system memory more precisely. On Windows Vista and later versions of Windows, use the **removememory** or **truncatememory** parameters with the [**BCDEdit /set**](bcdedit--set.md) command

You can use this parameter to test a driver in low memory conditions. For example, you can use this parameter to limit a computer with 1 GB of memory to 256 MB of memory.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /maxmem=256
```

### Bootcfg Command

```
bootcfg /addsw /MM 256 /ID 1 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/maxmem%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




