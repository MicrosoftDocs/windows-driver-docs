---
title: Providing a UVC INF File
author: windows-driver-content
description: Providing a UVC INF File
MS-HAID:
- 'uvcds\_2d986a38-5165-4c35-a8ff-5d1fe152c8e3.xml'
- 'stream.providing\_a\_uvc\_inf\_file'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 44311eb8-1035-466c-878b-a5d964b34490
keywords: ["INF files WDK USB Video Class", "UVC INF files WDK USB Video Class", "UVC INF files WDK USB Video Class , sample code", "sample code WDK USB Video Class , UVC INF files"]
---

# Providing a UVC INF File


This section illustrates various portions of a device-specific INF file.

An INF file like this one could be used to provide a device-specific name or to register the Extension Unit plug-in.

In general, vendors who supply a setup package can register the plug-in DLL by using the setup package, in which case the vendor does not provide an INF file. For driver signing, it may be easier to provide a setup package instead of a device-specific INF file.

Be aware, however, that you must install this specific sample by using an INF file.

To do so, include the following code in the INF file, here arbitrarily named *Xuplgin.inf*:

```
; Copyright (c) CompanyName. All rights reserved.

[Version]
Signature="$CHICAGO$"
Class=Image
ClassGUID={6bdd1fc6-810f-11d0-bec7-08002be2092f}
Provider=%CompanyName%

[SourceDisksNames]
1=%Package%

[SourceDisksFiles.x86]
MyPlugin.ax=1

[ControlFlags]
ExcludeFromSelect=*

[DestinationDirs]
MyDevice.CopyList=11    ; %systemroot%\system32 on 
   NT-based systems

[Manufacturer]
%CompanyName%=CompanyName
```

The device-specific INF file is matched with the device based on the VID/PID identifier. In this case, the device-specific INF file takes precedence over *Usbvideo.inf*.

```
[CompanyName]
%MyDevice.DeviceDesc%=MyDevice,USB\Vid_XXXX&Pid_XXXX&MI_XX

[MyDevice.NT]
Include=usbvideo.inf, ks.inf, kscaptur.inf, dshowext.inf
Needs=USBVideo.NT, KS.Registration, KSCAPTUR.Registration.NT,
DSHOWEXT.Registration
AddReg=MyDevice.Plugins
CopyFiles=MyDevice.CopyList
```

The following portion of the INF file shows the registry entries for a node-based Extension Unit plug-in. Refer to *Usbvideo.inf* for similar examples.

```
[MyDevice.PlugIns]
HKCR,CLSID\%Plugin.CLSID%,,,%PlugIn_IExtensionUnit%
HKCR,CLSID\%Plugin.CLSID%\InprocServer32,,,MyPlugin.ax
HKCR,CLSID\%Plugin.CLSID%\InprocServer32,ThreadingModel,,Both

; The IID is aggregated onto the node given the GUID of the property set
HKLM,System\CurrentControlSet\Control\NodeInterfaces\%XU_GUID%,,,
   %PlugIn_IExtensionUnit%
; IID in Little-Endian form
HKLM,System\CurrentControlSet\Control\NodeInterfaces\%XU_GUID%,IID,
   1,yy,yy,yy,yy,yy,yy,yy,yy,yy,yy,yy,yy,yy,yy,yy,yy
;CLSID in Little-Endian form
HKLM,System\CurrentControlSet\Control\NodeInterfaces\%XU_GUID%,
   CLSID,1,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz
```

```
[MyDevice.NT.Interfaces]
AddInterface=%KSCATEGORY_CAPTURE%,GLOBAL,MyDevice.Interface
AddInterface=%KSCATEGORY_RENDER%,GLOBAL,MyDevice.Interface
AddInterface=%KSCATEGORY_VIDEO%,GLOBAL,MyDevice.Interface

[MyDevice.Interface]
AddReg=MyDevice.Interface.AddReg
 
[MyDevice.Interface.AddReg]
HKR,,CLSID,,%ProxyVCap.CLSID%
HKR,,FriendlyName,,%MyDevice.DeviceDesc%
HKR,,RTCFlags,0x00010001,0x00000010
```

You can also define an optional registry value called **UvcFlags**. **UvcFlags** should be a DWORD value. When the device is plugged in, the UVC driver receives a Plug and Play (PnP) Start request. The driver then searches for **UvcFlags** in the device registry key. The DWORD value is a bitmask and can contain the values in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Bitmask name</strong></p></td>
<td><p><strong>Value</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td><p>WORKAROUNDS_DV_INTERLEAVED_DEFAULT_MASK</p></td>
<td><p>0x00000001</p></td>
<td><p>UVC supports video-only data ranges and interleaved DV data ranges. Set this bitmask for interleaved DV.</p></td>
</tr>
<tr class="odd">
<td><p>WORKAROUNDS_SUPPRESS_CLOCK_MASK</p></td>
<td><p>0x00000002</p></td>
<td><p>Currently not used.</p></td>
</tr>
<tr class="even">
<td><p>WORKAROUNDS_MPEG2TS_SUPPORT_FID</p></td>
<td><p>0x00000004</p></td>
<td><p>The FID mask indicates that the stream header contains an FID bit.</p></td>
</tr>
<tr class="odd">
<td><p>WORKAROUNDS_MPEG2TS_SUPPORT_EOF</p></td>
<td><p>0x00000008</p></td>
<td><p>The EOF mask indicates that the payload headers contain an end-of-frame bit.</p></td>
</tr>
<tr class="even">
<td><p>WORKAROUNDS_VARIABLE_FRAME_RATE_MASK</p></td>
<td><p>0x00000010</p></td>
<td><p>Set this mask if your device might vary frame rate. Fixed-rate DV devices should not set this mask.</p></td>
</tr>
</tbody>
</table>

 

Include a line similar to the following example to specify the bitmask to be applied:

```
HKR,,UvcFlags,0x00010001,0x00000010
```

If you are using the UVC driver on Windows Server 2003 and Windows Vista or later versions of the operating system, the FID and EOF masks can be used with stream-based formats such as MPEG-2 TS.

In low frame rate conditions, the EOF bit might report completion faster than the FID bit of the following frame. The EOF bit can be used to reduce latency in the delivery of MPEG-2 frames.

For more information about the positional syntax of AddReg directives, see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

```
[MyDevice.NT.Services]
AddService = usbvideo,0x00000002,MyDevice.ServiceInstall

[MyDevice.ServiceInstall]
DisplayName   = %USBVideo.SvcDesc%
ServiceType   = %SERVICE_KERNEL_DRIVER%
StartType     = %SERVICE_DEMAND_START%
ErrorControl  = %SERVICE_ERROR_NORMAL%
ServiceBinary = %10%\System32\Drivers\usbvideo.sys

[MyDevice.CopyList]
MyPlugin.ax
```

```
[Strings]
; Non-localizable
Plugin.CLSID="{zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz}"
ProxyVCap.CLSID="{17CCA71B-ECD7-11D0-B908-00A0C9223196}"
XU_GUID="{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}"
KSCATEGORY_RENDER="{65E8773E-8F56-11D0-A3B9-00A0C9223196}"
KSCATEGORY_CAPTURE="{65E8773D-8F56-11D0-A3B9-00A0C9223196}"
KSCATEGORY_VIDEO="{6994AD05-93EF-11D0-A3CC-00A0C9223196}"
SERVICE_KERNEL_DRIVER=1
SERVICE_DEMAND_START=3
SERVICE_ERROR_NORMAL=1

; Localizable
CompanyName="CompanyName"
Package="Installation Package"
MyDevice.DeviceDesc="CompanyName Camera"
USBVideo.SvcDesc="USB Video Device (WDM)"

PlugIn_IMyExtensionUnit="CompanyName Extension Unit Interface"
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Providing%20a%20UVC%20INF%20File%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


