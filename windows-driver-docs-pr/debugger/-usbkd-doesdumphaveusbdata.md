---
title: usbkd.doesdumphaveusbdata
description: The usbkd.doesdumphaveusbdata command checks to see which types of USB data are in a crash dump file that was generated as a result of Bug Check 0xFE.
ms.assetid: 5E475E9F-BC8E-4185-9F63-5BAD49A83904
keywords: ["usbkd.doesdumphaveusbdata Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.doesdumphaveusbdata
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.doesdumphaveusbdata


The **!usbkd.doesdumphaveusbdata** command checks to see which types of USB data are in a crash dump file that was generated as a result of [**Bug Check 0xFE**](bug-check-0xfe--bugcode-usb-driver.md).

```dbgcmd
!usbkd.doesdumphaveusbdata
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Remarks
-------

Use this command only when you are debugging a crash dump file that was generated as a result of [**Bug Check 0xFE: BUGCODE\_USB\_DRIVER**](bug-check-0xfe--bugcode-usb-driver.md).

Examples
--------

Here is an example of the output of **!doesdumphaveusbdata**

```dbgcmd
1: kd> !analyze -v
*** ...
BUGCODE_USB_DRIVER (fe) 
...
1: kd> !usbkd.doesdumphaveusbdata

Retrieving crashdump information Please Wait...

Checking for GuidUsbHubPortArrayData information...
There is no data for this GUID in the mini dump.
No data to print  

Checking for GuidUsbHubExt information...
There is no data for this GUID in the mini dump.
No data to print  

Checking for GuidUsbPortLog information...
GuidUsbPortLog Exists with PORT Log Size = 8000 

Checking for GuidUsbPortContextData information...
GuidUsbPortContextData Exists with Data Length = 4c8 

Checking for GuidUsbPortExt information...
GuidUsbPortExt Exists (DEVICE_EXTENSION + DeviceDataSize ) = 2250
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






