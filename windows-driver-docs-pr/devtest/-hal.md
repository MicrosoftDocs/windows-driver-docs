---
title: /hal
description: The /hal parameter directs the boot loader to load an alternate hardware abstraction layer (HAL) file for the operating system. The default HAL file is hal.dll.
ms.assetid: 95657043-c9c7-4855-a038-f0ec5928762b
keywords: ["/hal Driver Development Tools"]
topic_type:
- apiref
api_name:
- /hal
api_type:
- NA
---

/hal
====

The **/hal** parameter directs the boot loader to load an alternate hardware abstraction layer (HAL) file for the operating system. The default HAL file is hal.dll.

``` syntax
    /hal=HALFile 

   
```

## Subparameters


<a href="" id="-------halfile------"></a> *HALFile*   
Specifies a HAL file. The specified file must be located in the %SystemRoot%\\system32 directory, and its file name must conform to 8.3−character format.

### Comments

The **/hal** option is supported only on Windows Server 2003 with SP1 and Windows XP with SP2. On Windows Vista and later versions of Windows, use the **HAL** element in BCDEdit.

You can use this parameter to test a HAL update or use it with the [**/kernel**](-kernel.md) parameter to load a [partial checked build](https://msdn.microsoft.com/library/windows/hardware/ff547196) installation.

Do not use this parameter unless you have deliberately installed a different HAL.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /hal=HALtest.dll
```

### Bootcfg Command

```
bootcfg /raw "/hal=HALtest.dll" /A /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/hal%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




