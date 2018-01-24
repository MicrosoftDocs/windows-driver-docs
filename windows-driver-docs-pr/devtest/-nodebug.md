---
title: /nodebug
description: The /nodebug parameter disables kernel debugging.
ms.assetid: 23e94fc4-1ae3-4a55-9c10-5af14c9acafd
keywords: ["/nodebug Driver Development Tools"]
topic_type:
- apiref
api_name:
- /nodebug
api_type:
- NA
---

/nodebug
========

The **/nodebug** parameter disables kernel debugging.

``` syntax
    /nodebug 

   
```

### Comments

The **/nodebug** option is supported only on Windows Server 2003 with SP1 and Windows XP with SP2. On Windows Vista and later versions of Windows, in BCDEdit, use the **/debug** command with a value of **OFF** (**bcdedit /debug** \[*ID*\] **OFF**).

If you include the **/nodebug** parameter, then the [**/debug**](-debug.md) parameter and its **/debugport**, **/baudrate**, and **/targetname** subparameters are ignored. If you include the [**/crashdebug**](-crashdebug.md) parameter, then the **/nodebug** parameter is ignored.

You can use this parameter to disable a debugging configuration without deleting it from the boot options on your computer.

### Examples

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /nodebug

multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /debug /debugport=1394 /channel=52 /nodebug
```

### Bootcfg Command

```
bootcfg /raw "/nodebug" /A /ID 1n
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/nodebug%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




