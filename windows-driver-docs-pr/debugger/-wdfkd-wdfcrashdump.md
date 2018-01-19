---
title: wdfkd.wdfcrashdump
description: The wdfkd.wdfcrashdump extension displays error log information and other crash dump information from a minidump file, if the data is present.
ms.assetid: 419c76b1-e291-4503-8c59-aa46140e40b3
keywords: ["wdfkd.wdfcrashdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfcrashdump
api_type:
- NA
---

# !wdfkd.wdfcrashdump


The **!wdfkd.wdfcrashdump** extension displays error log information and other crash dump information from a minidump file, if the data is present.

KMDF

```
!wdfkd.wdfcrashdump [InfoType]
```

UMDF

```
!wdfkd.wdfcrashdump [DriverName.dll][-d | -f | -m]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______InfoType______"></span><span id="_______infotype______"></span><span id="_______INFOTYPE______"></span> *InfoType*   
Specifies the kind of information to display. *InfoType* is optional and can be any one of the following values:

<span id="log"></span><span id="LOG"></span>**log**  
Displays error log information, if available in the crash dump file. This is the default value.

<span id="loader"></span><span id="LOADER"></span>**loader**  
Displays the minidump's dynamic-bound drivers.

<span id="drivername.dll"></span><span id="DRIVERNAME.DLL"></span>*DriverName*.dll  
Specifies the name of a UMDF driver. You must include the .dll file suffix. If this optional parameter is omitted, output includes metadata, the loaded module list, and available logs.

<span id="-d"></span><span id="-D"></span>**-d**  
Displays only the driver logs.

<span id="-f"></span><span id="-F"></span>**-f**  
Displays only the framework logs.

<span id="-m"></span><span id="-M"></span>**-m**  
Merges framework and driver logs in their recorded order.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF

UMDF 2.15

Remarks
-------

This example shows how to use **!wdfkd.wdfcrashdump** to view information about KMDF drivers. If you specify **loader** for *InfoType*, the output includes dynamic-bound drivers in the minidump file.

```
0: kd> !wdfcrashdump loader 
Retrieving crashdump loader information...
## Local buffer 0x002B4D00, bufferSize 720
----------------------------------------------
  ImageName      Version    FxGlobals

  Wdf01000       v1.9(6902)
  msisadrv       v1.9(6913) 0x84deb260
  vdrvroot       v1.9(6913) 0x860e8260
  storflt        v1.5(6000) 0x861dfe90
  cdrom          v1.9(6913) 0x84dca008
  intelppm       v1.9(6913) 0x864704a8
  HDAudBus       v1.7(6001) 0x86101c98
  1394ohci       v1.7(6001) 0x8610d2e8
  CompositeBus   v1.9(6913) 0x86505b98
  ObjTestClassExt v1.9(6902) 0x865b7f00
  mqfilter       v1.9(6902) 0x865b8008
  mqueue         v1.9(6902) 0x865b6910
  umbus          v1.9(6913) 0x8618aea0
  monitor        v1.9(6913) 0x86aac1d8
  PEAUTH         v1.5(6000) 0x854e5350
----------------------------------------------
```

This example shows how to use **!wdfkd.wdfcrashdump** to view information about UMDF drivers. If you issue **!wdfkd.wdfcrashdump** with no parameters, the output includes the driver that caused the crash and a list of all loaded drivers in the host process that failed. You can click on drivers in this list that have associated logs.

```
0:001> !wdfkd.wdfcrashdump
Opening minidump at location C:\temp\WudfHost_ext__1312.dmp

Faulting driver: wpptest.dll
Failure type: Unhandled Exception (WUDFUnhandledException)
Faulting thread ID: 2840

Listing all drivers loaded in this host process at the time of the failure:

  ServiceName
  wpptest 
  CoverageCx0102
  coverage
  WUDFVhidmini
  ToastMon
  WUDFOsrUsbFilter
```

In the example above, output includes failure type, which is the event type in the WER report. Here, it can be **WUDFVerifierFailure** or **WUDFUnhandledException**. For more information, see [Accessing UMDF Metadata in WER Reports](https://msdn.microsoft.com/library/windows/hardware/ff542975). The output for UMDF includes an error code, if event type is **WUDFVerifierFailure**.

To display the framework's error log records from a [complete memory dump](complete-memory-dump.md), a [kernel memory dump](kernel-memory-dump.md), or a [live kernel-mode target](live-kernel-mode-targets.md), you can also try the [**!wdfkd.wdflogdump**](-wdfkd-wdflogdump.md) extension.

**Additional Information**

For information about enabling the inflight trace recorder for your driver, see [Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers](https://msdn.microsoft.com/library/windows/hardware/dn940485). For more information about debugging WDF drivers, see [Debugging WDF Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540790). For information about KMDF debugging, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

## <span id="see_also"></span>See also


[**!wdfkd.wdflogdump**](-wdfkd-wdflogdump.md)

[**!wdfkd.wdfsettraceprefix**](-wdfkd-wdfsettraceprefix.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfcrashdump%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





