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





Drivers register the source of error messages in the registry. Drivers must set two keys under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\EventLog\\System\\***DriverName*:

<a href="" id="eventmessagefile--reg-expand-sz-"></a>**EventMessageFile** (REG\_EXPAND\_SZ)  
A list of error message sources separated by semicolons. If the driver uses standard error types, this list must include iologmsg.dll. If the driver uses error messages attached to the driver image, this must include the name of the driver image.

<a href="" id="typessupported--reg-dword-"></a>**TypesSupported** (REG\_DWORD)  
A bitmask of the possible severity levels that can be logged. Drivers typically set this to 7 to indicate they may log all severity levels.

For a description of how to set these registry keys from the driver's INF file, see [**Registering for Event Logging**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

 

 




