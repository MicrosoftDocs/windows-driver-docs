---
title: IPM Configuration and Usage
author: windows-driver-content
description: IPM Configuration and Usage
ms.assetid: 95057785-e5b5-40ae-86e4-50bbf0014cef
---

# IPM Configuration and Usage


Storport Idle Power Management (IPM) is not enabled by default. It can be enabled in the registry by setting the "EnableIdlePowerManagement" value in the "StorPort" subkey of the device's hardware key to any nonzero value. This can be done by using the device INF file or manually by using the registry editor.

The following sample text shows what you need to add to your device's INF file to enable the Storport Idle Power Management feature.

```
          [DDInstall.HW]
          ; Enables Storport IPM for this adapter
          HKR, "StorPort", "EnableIdlePowerManagement", 0x00010001, 0x01
```

This can be done only from within the INF file's DDInstall.HW section where HKR points to the hardware key and not the service key. For more information about how to change an INF file, see [Introduction to Registry Keys for Drivers](http://go.microsoft.com/fwlink/p/?linkid=144533) on MSDN.

The Power Options control panel applet shown in the following screen shot is used to configure the system power policy and disk idle timeout value. It is accessible from **Start** &gt; **Control Panel** &gt; **Power Options**.

![screen shot illustrating ipm power options](images/ipm-power-options.png)

A command line tool (*Powercfg.exe*) can also be used. Type **powercfg /?** for usage information at the command prompt.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20IPM%20Configuration%20and%20Usage%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


