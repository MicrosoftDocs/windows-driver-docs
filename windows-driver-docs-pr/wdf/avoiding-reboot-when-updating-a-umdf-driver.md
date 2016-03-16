---
title: Avoiding Reboot when Updating a UMDF Driver
description: Avoiding Reboot when Updating a UMDF Driver
ms.assetid: B5321732-50FD-4719-BBD0-F0A3BE1EE532
---

# Avoiding Reboot when Updating a UMDF Driver


To avoid a required reboot when you update a UMDF driver, specify the **COPYFLG\_IN\_USE\_RENAME** flag in the [**CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) in your driver's INF file, as shown in this example:

```
[VirtualSerial_Install.NT]
CopyFiles=UMDriverCopy
 
[UMDriverCopy]
Virtualserial.dll,,,0x00004000  ; COPYFLG_IN_USE_RENAME
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Avoiding%20Reboot%20when%20Updating%20a%20UMDF%20Driver%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




