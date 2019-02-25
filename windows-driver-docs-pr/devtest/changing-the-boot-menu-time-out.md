---
title: Changing the Boot Menu Time-out
description: Changing the Boot Menu Time-out
ms.assetid: 447fe656-4bb5-454e-bc89-bab58c8ffaea
keywords:
- Boot.ini files WDK , menu time-outs
- boot options WDK , menu time-outs
- menu time-outs WDK boot options
- time-outs WDK boot options
- boot menu time-outs WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





