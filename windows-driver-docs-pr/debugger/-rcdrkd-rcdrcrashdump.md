---
title: rcdrkd.rcdrcrashdump
description: The rcdrkd.rcdrcrashdump extension is used with a minidump file to display the recorder log (if the log is present in the minidump).
ms.assetid: 61DB0462-31F1-4756-87BB-60188887ACAF
keywords: ["rcdrkd.rcdrcrashdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- rcdrkd.rcdrcrashdump
api_type:
- NA
---

# !rcdrkd.rcdrcrashdump


The [**!rcdrkd.rcdrcrashdump**](-usb3kd-device-info.md) extension is used with a minidump file to display the recorder log (if the log is present in the minidump).

```
!rcdrkd.rcdrcrashdump TraceProviderGuid
!rcdrkd.rcdrcrashdump DriverName
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______TraceProviderGuid______"></span><span id="_______traceproviderguid______"></span><span id="_______TRACEPROVIDERGUID______"></span> *TraceProviderGuid*   
GUID of the trace provider. This parameter must include braces: {*guid*}

<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
The name of the driver. The driver name can be used instead of the trace provider GUID for drivers that use the Inflight Trace Recorder (IFR).

## <span id="DLL"></span><span id="dll"></span>DLL


Rcdrkd.dll

## <span id="see_also"></span>See also


[RCDRKD Extensions](rcdrkd-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!rcdrkd.rcdrcrashdump%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





