---
title: SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)
description: SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)
ms.assetid: 5b35fad3-09d6-4b2f-9831-661fe69f2f99
keywords: ["SetupAPI WDK device installations , logging", "logging WDK SetupAPI", "SetupAPI logging WDK Windows Server 2003", "SetupAPI logging WDK Windows 2000", "SetupAPI logging WDK Windows XP"]
---

# SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)


## <a href="" id="ddk-using-setupapi-logging-dg"></a>


The Windows Setup and Device Installer Services, also known as SetupAPI, include the Windows functions that control Setup and device installation. As Setup proceeds, the [general Setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985) (**Setup***Xxx* functions) and [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) (**SetupDi***Xxx* functions) create a log file that provides useful information for troubleshooting device installation problems.

SetupAPI logs to the file %*systemroot*%\\*setupapi.log*. The log file is a plain text file. To reset the log, rename or delete the file.

This section includes the following information:

[Setting SetupAPI Logging Levels](setting-setupapi-logging-levels.md)

[Interpreting a Sample SetupAPI Log File](interpreting-a-sample-setupapi-log-file.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20SetupAPI%20Logging%20%28Windows%20Server%202003,%20Windows%20XP,%20and%20Windows%202000%29%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




