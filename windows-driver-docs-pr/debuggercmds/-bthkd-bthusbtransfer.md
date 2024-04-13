---
title: "!bthkd.bthusbtransfer"
description: "The !bthkd.bthusbtransfer command displays the Bluetooth usb transfer context including Irp, Bip and transfer buffer information."
keywords: ["!bthkd.bthusbtransfer Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- bthkd.bthusbtransfer
api_type:
- NA
---

# !bthkd.bthusbtransfer


The **!bthkd.bthusbtransfer** command displays the Bluetooth usb transfer context including Irp, Bip and transfer buffer information.

```dbgsyntax
!bthkd.bthusbtransfer addr 
```

## Parameters


<span id="_______addr______"></span><span id="_______ADDR______"></span> *addr*   
Address of the Bluetooth USB transfer context.

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


You can use the !bthinfo command to display the address of USB transfer context. It is listed under the transfer list section.

## DLL


Bthkd.dll

## See also


[Bluetooth Extensions (Bthkd.dll)](bluetooh-extensions--bthkd-dll-.md)


