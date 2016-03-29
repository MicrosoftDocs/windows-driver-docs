---
title: Sample Port Monitor
description: Sample Port Monitor
ms.assetid: dac754bf-f39d-439c-974b-889436211ef3
keywords: ["port monitors WDK print , samples"]
---

# Sample Port Monitor


## <a href="" id="ddk-sample-port-monitor-gg"></a>


Source code for LOCALMON (Localmon.dll), the port monitor that supports local LPT and COM ports, is included in the Windows Driver Kit (WDK).

Beginning with Windows 2000, all of the functions that LOCALMON exports were incorporated into Localspl.dll, the Local Print Provider. Another change in Windows 2000 and later operating system versions is that port monitors are divided into two DLLs: a port monitor server DLL, and a port monitor user interface DLL. The source code for these DLLs is located in the \\Src\\Print\\Monitors\\Localmon and \\Src\\Print\\Monitors\\Localui subdirectories.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Sample%20Port%20Monitor%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




