---
title: Changing the Boot Menu Time-out
description: Changing the Boot Menu Time-out
ms.assetid: 447fe656-4bb5-454e-bc89-bab58c8ffaea
keywords: ["Boot.ini files WDK , menu time-outs", "boot options WDK , menu time-outs", "menu time-outs WDK boot options", "time-outs WDK boot options", "boot menu time-outs WDK"]
---

# Changing the Boot Menu Time-out


## <span id="ddk_changing_the_boot_menu_time_out_tools"></span><span id="DDK_CHANGING_THE_BOOT_MENU_TIME_OUT_TOOLS"></span>


The boot menu time-out determines how long the boot menu is displayed before the default boot entry is loaded. It is calibrated in seconds.

If you want extra time to choose the operating system that loads on your computer, you can extend the time-out value. Or, you can shorten the time-out value so that the default operating system starts faster.

For Windows, you can use BCDEdit to change the default boot menu time-out value.

### <span id="using_bcdedit"></span><span id="USING_BCDEDIT"></span>Using BCDEdit

To specify the boot menu time-out value, use the **/timeout** option:

```
bcdedit /timeout <timeout>
```

Use the **/timeout** option and specify the timeout value in seconds. For example, to specify a 15-second timeout value:

```
bcdedit /timeout 15
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Changing%20the%20Boot%20Menu%20Time-out%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




