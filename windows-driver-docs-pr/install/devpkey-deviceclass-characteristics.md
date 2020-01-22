---
title: DEVPKEY_DeviceClass_Characteristics
description: DEVPKEY_DeviceClass_Characteristics
ms.assetid: dd50a97b-7230-46a5-b6d2-0f741d7ae5d4
keywords: ["DEVPKEY_DeviceClass_Characteristics Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_Characteristics
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_Characteristics


The DEVPKEY_DeviceClass_Characteristics device property represents the default device characteristics of all devices in a [device setup class](https://docs.microsoft.com/windows-hardware/drivers/install/device-setup-classes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_Characteristics</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers after a device setup class is installed</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPCRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPCRP_CHARACTERISTICS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

DEVPKEY_DeviceClass_Characteristics should only be set when a device setup class is installed and not modified later. For information about how to install a device setup class and setting this property, see [**INF ClassInstall32 Section**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-classinstall32-section) and the information about the registry entry value **DeviceCharacteristics** that is provided in the "Special *value-entry-name* Keywords" section of [**INF AddReg Directive**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addreg-directive).

You can call [**SetupDiGetClassProperty**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdigetclasspropertyw) or [**SetupDiGetClassPropertyEx**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdigetclasspropertyexw) to retrieve the value of DEVPKEY_DeviceClass_Characteristics.

Windows Server 2003 and Windows XP support this property, but do not support the DEVPKEY_DeviceClass_Characteristics property key. On these earlier versions of Windows, you can use the SPCRP_CHARACTERISTICS identifier to access the value of this property. For information about how to access the value of this property, see [Retrieving Device Setup Class SPCRP_Xxx Properties](https://docs.microsoft.com/windows-hardware/drivers/install/retrieving-spcrp-xxx-properties).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**IoCreateDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice)

[**INF AddReg Directive**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addreg-directive)

[**INF ClassInstall32 Section**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-classinstall32-section)

[**SetupDiGetClassProperty**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiGetClassPropertyEx**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdigetclasspropertyexw)

 

 






