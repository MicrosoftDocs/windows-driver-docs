---
title: Registering as a Source of Error Messages
author: windows-driver-content
description: Registering as a Source of Error Messages
ms.assetid: 5428950c-9c28-411a-9ec0-b029ad311a00
keywords: ["source registration WDK errors", "errors WDK kernel", "registering error message sources", "registry WDK error logs"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering as a Source of Error Messages


## <a href="" id="ddk-registering-as-a-source-of-error-messages-kg"></a>


Drivers register the source of error messages in the registry. Drivers must set two keys under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\EventLog\\System\\***DriverName*:

<a href="" id="eventmessagefile--reg-expand-sz-"></a>**EventMessageFile** (REG\_EXPAND\_SZ)  
A list of error message sources separated by semicolons. If the driver uses standard error types, this list must include iologmsg.dll. If the driver uses error messages attached to the driver image, this must include the name of the driver image.

<a href="" id="typessupported--reg-dword-"></a>**TypesSupported** (REG\_DWORD)  
A bitmask of the possible severity levels that can be logged. Drivers typically set this to 7 to indicate they may log all severity levels.

For a description of how to set these registry keys from the driver's INF file, see [**Registering for Event Logging**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20as%20a%20Source%20of%20Error%20Messages%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


