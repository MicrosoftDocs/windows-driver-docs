---
title: DEVPKEY_DrvPkg_DocumentationLink
description: DEVPKEY_DrvPkg_DocumentationLink
ms.assetid: a4ae1f6c-edf5-4490-8f92-6d7a24040304
keywords: ["DEVPKEY_DrvPkg_DocumentationLink Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_DocumentationLink
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DrvPkg_DocumentationLink


The DEVPKEY_DrvPkg_DocumentationLink device property represents a URL to the documentation for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DrvPkg_DocumentationLink</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The documentation link URL should be a link to a file that contains information about a device. This property is intended to provide Web-accessible documentation for a device. The file can be an HTML page, a *.pdf* file, a *.doc* file, or other file type. The only restriction is that all the documentation content must be contained within the URL-specified file. For example, an \**.htm* file that is self-contained is valid, an \**.htm* file that refers to other graphics files is not valid, and an \**.mta* Web archive file that contains referenced graphic files is valid.

The URL can contain parameters. For example, the following URL contains a **prod** parameter that supplies the value "DSC530", a **rev** parameter that supplies the value "34", and a **type** parameter that supplies the value "doc":

```cpp
http://www.microsoft.com/redirect?prod=DSC530&rev=34&type=docs
```

Microsoft does not provide Web hosting or redirection for a webpage that is specified by a DEVPKEY_DrvPkg_DocumentationLink property value. The URL must link to a webpage that is maintained by the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) provider.

When a user clicks the website link that is displayed in Setup-generated end-user dialog box, Windows adds the following information to the HTTP request that includes the URL supplied by DEVPKEY_DrvPkg_DocumentationLink:

-   The Windows version, as specified by a **pver** parameter. For example, "pver=6.0" specifies Windows Vista.

-   The stock keeping unit (SKU), as specified by the **sbp** parameter, which can be set to per or pro. For example, "sbp=pro" specifies the professional edition.

-   The local identifier (LCID), as specified by the **olcid** parameter. For example, "olcid=0x409" specifies the English (Standard) language.

-   The most specific hardware identifier for a device, as specified by the **pnpid** parameter. For example, "pnpid=PCI%5CVEN_8086%26DEV_2533%26SUBSYS_00000000%26REV_04" specifies the hardware identifier for a PCI device.

For privacy reasons, user information and the serial number of device is not included in the HTTP request.

```cpp
The following example shows the type of HTTP request that would be sent to a web server: http://www.microsoft.com/redirect?prod=DSC530&rev34&type=docs&pver=6.0&spb=pro&olcid=0x409&pnpid=PCI%5CVEN_8086%26DEV_2533%26SUBSYS_00000000%26REV_04
```

You can set the value of DEVPKEY_DrvPkg_DocumentationLink by an [**INF AddProperty directive**](https://msdn.microsoft.com/library/windows/hardware/ff546318) that is included in the [**INF *DDInstall* section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of the INF file that installs the device. You can retrieve the value of DEVPKEY_DrvPkg_DocumentationLinkproperty by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963).

The following is an example of how to use an INF **AddProperty** directive to set the value of DEVPKEY_DrvPkg_DocumentationLink for a device that is installed by an INF *DDInstall* section "SampleDDInstallSection":

```cpp
[SampleDDinstallSection]
...
AddProperty=SampleAddPropertySection
...

[SampleAddPropertySection] 
DeviceDocumentationLink,,,,"http://www.microsoft.com/redirect?prod=DSC530&rev34&type="docs"
...
```

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


[**INF AddProperty Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546318)

[**INF *DDInstall* Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






