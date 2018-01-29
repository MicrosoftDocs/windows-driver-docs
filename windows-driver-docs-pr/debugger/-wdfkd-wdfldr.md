---
title: wdfkd.wdfldr
description: The wdfkd.wdfldr extension displays information about the KMDF and UMDF drivers that are currently dynamically bound to the Windows Driver Frameworks. 
ms.assetid: 0965632d-922b-4812-9cfb-7663af0e3847
keywords: ["wdfkd.wdfldr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfldr
api_type:
- NA
---

# !wdfkd.wdfldr


The **!wdfkd.wdfldr** extension displays information about the drivers that are currently dynamically bound to the Windows Driver Frameworks. This includes both the Kernel-Mode Driver Framework (KMDF) and the User-Mode Driver Framework (UMDF).

```
!wdfkd.wdfldr [DriverName]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
The name of a driver, including the filename extension. If you supply a driver name, this command displays detailed information about the one driver. If you do not supply a drive name, this command displays information about all drivers that are bound to the Windows Driver Frameworks.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

Here is an example of the output of **!wdfldr**.

```
## 0: kd> !wdfkd.wdfldr

##  KMDF Drivers

##  LoadedModuleList      0xfffff800003b61f8

LIBRARY_MODULE  0xffffe0000039f7c0
  Version       v1.13
  Service       \Registry\Machine\System\CurrentControlSet\Services\Wdf01000
  ImageName     Wdf01000.sys
  ImageAddress  0xfffff800002e7000
  ImageSize     0xc5000
  Associated Clients: 16

  ImageName                      Ver   WdfGlobals         FxGlobals          ImageAddress       ImageSize
  peauth.sys                     v1.7  0xffffe00003a95880 0xffffe00003a956e0 0xfffff80002678000 0x000ab000
  monitor.sys                    v1.11 0xffffe000001abc70 0xffffe000001abad0 0xfffff800022e7000 0x0000e000
  UsbHub3.sys                    v1.11 0xffffe000028a47b0 0xffffe000028a4610 0xfffff8000220b000 0x00077000
##   ...

## Total: 1 library loaded

##  UMDF Drivers

  DriverManagerProcess: 0xffffe00003470500

  ImageName                      Ver
  MyUmdfDriver.dll               v1.11 
  SomeUmdf2Driver.dll            v2.0  
  MyUmdf2Driver.dll              v2.0
```

Here is another example that supplies a driver name.

```
0: kd> !wdfldr MyUmdf2Driver.dll

Version    v2.0
Service    \Registry\Machine\System\CurrentControlSet\Services\MyUmdf2Driver

## !wdflogdump  MyUmdf2Driver.dll

##  UMDF Device Instances using MyUmdf2Driver.dll

Process             DevStack           DeviceId
0xffffe00000c32900  a5a3ab5f70         \Device\00000052 !wdfdriverinfo
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfldr%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




