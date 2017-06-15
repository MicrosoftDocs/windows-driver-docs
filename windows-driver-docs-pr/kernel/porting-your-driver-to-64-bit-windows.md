---
title: Porting Your Driver to 64-Bit Windows
author: windows-driver-content
description: Porting Your Driver to 64-Bit Windows
MS-HAID:
- 'Other\_394c38ae-a3e6-45fb-87f2-c3e227cb6b7c.xml'
- 'kernel.porting\_your\_driver\_to\_64\_bit\_windows'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f06e6aae-fc44-481c-a277-1c266d6e6d7b
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "thunking WDK", "WOW64 thunking layer WDK", "converting parameters to fixed-precision types"]
---

# Porting Your Driver to 64-Bit Windows


## <a href="" id="ddk-porting-your-driver-to-64-bit-windows-kg"></a>


The 64-bit version of Windows is designed to make it possible for developers to use a single source-code base for their 32-bit and 64-bit Windows applications. To a large extent, this is also true for 32-bit and 64-bit Windows drivers.

For user-mode applications, 64-bit Windows includes a Windows on Windows (WOW64) *thunking layer* that enables 32-bit applications to execute (with some performance degradation) on 64-bit versions of Windows. It does this by intercepting 32-bit function calls and converting pointer-precision parameter types to fixed-precision types as appropriate before making the transition to the 64-bit kernel. This conversion process is called *thunking*.

**Note**  This thunking is only done for 32-bit *applications*; 32-bit *drivers* are not supported on 64-bit versions of Windows.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Porting%20Your%20Driver%20to%2064-Bit%20Windows%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


