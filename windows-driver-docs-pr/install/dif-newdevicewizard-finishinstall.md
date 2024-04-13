---
title: DIF_NEWDEVICEWIZARD_FINISHINSTALL
description: DIF_NEWDEVICEWIZARD_FINISHINSTALL
keywords: ["DIF_NEWDEVICEWIZARD_FINISHINSTALL Device and Driver Installation"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DIF_NEWDEVICEWIZARD_FINISHINSTALL
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DIF_NEWDEVICEWIZARD_FINISHINSTALL


A DIF_NEWDEVICEWIZARD_FINISHINSTALL request allows an installer to supply finish-install wizard pages that Windows displays to the user after a device is installed but before Windows displays the standard finish page. Windows sends this request when it installs Plug and Play (PnP) devices and when an administrator uses the **Add Hardware Wizard** to install non-PnP devices.

### When Sent

After Windows installs a device (on successful completion of [**DIF_INSTALLDEVICE**](dif-installdevice.md) processing), but before it displays the Finish wizard page.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
A handle to the [device information set](./device-information-sets.md) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
A pointer to an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_NEWDEVICEWIZARD_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_newdevicewizard_data) structure is associated with the *DeviceInfoData*.

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the flags in the device installation parameters.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the SP_NEWDEVICEWIZARD_DATA structure to supply finish-install wizard pages.

### Installer Return Value

If a co-installer does not handle this DIF request, the co-installer returns NO_ERROR from its preprocessing pass. If a co-installer handles this request, the co-installer can return NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

A class installer returns NO_ERROR if the installer successfully supplies pages. Otherwise, a class installer returns ERROR_DI_DO_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

For more information about DIF codes, see [Handling DIF Codes](./handling-dif-codes.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Supported in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Setupapi.h (include Setupapi.h)</td>
</tr>
</tbody>
</table>

## See also


[**DIF_FINISHINSTALL_ACTION**](dif-finishinstall-action.md)

[**DIF_INSTALLDEVICE**](dif-installdevice.md)

[**SetupDiChangeState**](/windows/win32/api/setupapi/nf-setupapi-setupdichangestate)

[**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data)

[**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)

[**SP_NEWDEVICEWIZARD_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_newdevicewizard_data)

 

