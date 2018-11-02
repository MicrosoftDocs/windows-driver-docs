---
title: rcdrkd.rcdrcrashdump
description: The rcdrkd.rcdrcrashdump extension is used with a minidump file to display the recorder log (if the log is present in the minidump).
ms.assetid: 61DB0462-31F1-4756-87BB-60188887ACAF
keywords: ["rcdrkd.rcdrcrashdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rcdrkd.rcdrcrashdump
api_type:
- NA
ms.localizationpriority: medium
---

# !rcdrkd.rcdrcrashdump


The [**!rcdrkd.rcdrcrashdump**](-usb3kd-device-info.md) extension is used with a minidump file to display the recorder log (if the log is present in the minidump).

```dbgcmd
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

 

 






