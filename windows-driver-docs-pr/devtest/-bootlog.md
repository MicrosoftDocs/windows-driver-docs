---
title: /bootlog
description: The /bootlog parameter records the names of drivers as they load during the boot process and saves the ordered list in the SystemRoot \\ntbtlog.txt file.
ms.assetid: 33a233f1-aabd-4429-9379-151eb6c4cf43
keywords: ["/bootlog Driver Development Tools"]
topic_type:
- apiref
api_name:
- /bootlog
api_type:
- NA
---

/bootlog
========

The **/bootlog** parameter records the names of drivers as they load during the boot process and saves the ordered list in the %SystemRoot%\\ntbtlog.txt file.

``` syntax
    /bootlog 

   
```

### Comments

The **/bootlog** parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000. On Windows Vista and later versions of Windows, use the **LogInitialization** element in BCDEdit.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /bootlog
```

### Bootcfg Command

```
bootcfg /raw "/bootlog" /A /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/bootlog%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




