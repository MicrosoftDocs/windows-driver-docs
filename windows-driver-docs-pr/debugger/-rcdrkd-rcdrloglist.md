---
title: rcdrkd.rcdrloglist
description: The rcdrkd.rcdrloglist extension displays a list of the recorder logs owned by a driver or a set of drivers.
ms.assetid: D4D3C313-EFD4-482B-B4A3-307F2407D2BA
keywords: ["rcdrkd.rcdrloglist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rcdrkd.rcdrloglist
api_type:
- NA
ms.localizationpriority: medium
---

# !rcdrkd.rcdrloglist


The **!rcdrkd.rcdrloglist** extension displays a list of the recorder logs owned by a driver or a set of drivers.

```dbgcmd
!rcdrkd.rcdrloglist DriverName [DriverName ...]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
The name of a driver, not including the .sys extension.

## <span id="DLL"></span><span id="dll"></span>DLL


Rcdrkd.dll

Remarks
-------

This command is relevant only for drivers that log messages to different logs by using the WppRecorder API.

Examples
--------

The following example displays a list of all recorder logs owned by the USB 3.0 host controller driver (usbxhci.sys).

```dbgcmd
3: kd> !rcdrloglist usbxhci
Log dump command                           Log ID                   Size
================                           ======                   ====
!rcdrlogdump  usbxhci -a fffffa8005ff2b60  03 SLT02 DCI04           1024
!rcdrlogdump  usbxhci -a fffffa8005ff2010  03 SLT02 DCI03           1024
!rcdrlogdump  usbxhci -a fffffa8005b36010  03 SLT01 DCI03           1024
!rcdrlogdump  usbxhci -a fffffa8005b379e0  03 SLT01 DCI04           1024
!rcdrlogdump  usbxhci -a fffffa8005b33350  03 SLT02 DCI01           1024
!rcdrlogdump  usbxhci -a fffffa8005b2bb60  03 SLT01 DCI01           1024
!rcdrlogdump  usbxhci -a fffffa8005a2bb60  03 CMD                   1024
!rcdrlogdump  usbxhci -a fffffa8005a1ab60  03 INT00                 1024
!rcdrlogdump  usbxhci -a fffffa8005085330  03 RUNDOWN               512
!rcdrlogdump  usbxhci -a fffffa8005311780  03 1033 0194             1024
```

## <span id="see_also"></span>See also


[RCDRKD Extensions](rcdrkd-extensions.md)

 

 






