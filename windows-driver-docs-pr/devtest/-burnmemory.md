---
title: /burnmemory
description: The /burnmemory parameter reduces the amount of memory available to Windows by the specified amount.
ms.assetid: ca2add1a-f7f2-4160-b12f-7e1ef5c00bfb
keywords: ["/burnmemory Driver Development Tools"]
topic_type:
- apiref
api_name:
- /burnmemory
api_type:
- NA
---

/burnmemory
===========

The **/burnmemory** parameter reduces the amount of memory available to Windows by the specified amount.

``` syntax
    /burnmemory=SizeInMB 

   
```

## Subparameters


<a href="" id="-------sizeinmb------"></a> *SizeInMB*   
Specifies an amount of memory (in megabytes). Enter a decimal integer. This value is subtracted from the amount of memory otherwise allocated to the system.

### Comments

The **/burnmemory** parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000. On Windows Vista and later versions of Windows, use the **removememory** option with BCDEdit.

This parameter is similar to the [**/maxmem**](-maxmem.md) parameter, which specifies the amount of memory available to Windows. However, because **/maxmem** actually sets an upper bound for memory addresses available to Windows, and because there might be gaps in the allocation of system memory, the **/burnmemory** parameter is more precise than the **/maxmem** parameter.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /burnmemory=256
```

### Bootcfg Command

```
bootcfg /raw "/burnmemory=256" /A /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/burnmemory%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




