---
title: DEVPKEY_DeviceClass_LowerFilters
description: DEVPKEY_DeviceClass_LowerFilters
keywords: ["DEVPKEY_DeviceClass_LowerFilters Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_LowerFilters
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_LowerFilters


The DEVPKEY_DeviceClass_LowerFilters device property represents a list of the service names of the lower-level filter drivers that are installed for a [device setup class](./overview-of-device-setup-classes.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_LowerFilters</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data format</strong></p></td>
<td align="left"><p>"<em>service-name1</em>\0<em>service-name2</em>\0…<em>service-nameN</em>\0\0"</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers after a class filter is installed</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Corresponding SPCRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPCRP_LOWERFILTERS</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding registry value name</strong></p></td>
<td align="left"><p><strong>LowerFilters</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of DEVPKEY_DeviceClass_LowerFilters is set when a class filter driver is installed. For more information about how to install a class filter driver, see [Installing a Filter Driver](./installing-a-filter-driver.md) and [**INF ClassInstall32 Section**](./inf-classinstall32-section.md).

You can call [**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) or [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) to retrieve the value of DEVPKEY_DeviceClass_LowerFilters.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceClass_LowerFilters property key. On these earlier versions of Windows, you can access the value of this property by accessing the corresponding **LowerFilters** registry value under the class registry key. For information about how to access this property value on these earlier versions of Windows, see [Accessing Registry Entry Values Under the Class Registry Key](./accessing-device-setup-class-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF ClassInstall32 Section**](./inf-classinstall32-section.md)

[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiOpenClassRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey)
