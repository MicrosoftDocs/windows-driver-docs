---
title: DEVPKEY_DrvPkg_DetailedDescription
description: DEVPKEY_DrvPkg_DetailedDescription
keywords: ["DEVPKEY_DrvPkg_DetailedDescription Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_DetailedDescription
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_DrvPkg_DetailedDescription


The DEVPKEY_DrvPkg_DetailedDescription device property represents a detailed description of the capabilities of a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DrvPkg_DetailedDescription</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data format</strong></p></td>
<td align="left"><p>Limited set of XML tags</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The detailed description string is in XML format. XML format makes it possible for Windows to format the display of the information based on the following subset of supported Hypertext Markup Language (HTML) tags. The operation of these tags resembles the operation of HTML tags.

<a href="" id="heading-level-tags"></a>Heading level tags  
&lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;

<a href="" id="list-tags"></a>List tags  
&lt;ul&gt;, &lt;ol&gt;, &lt;li&gt;

<a href="" id="paragraph-tag"></a>Paragraph tag  
&lt;p&gt;

You can set the value of DEVPKEY_DrvPkg_DetailedDescription by an [**INF AddProperty directive**](./inf-addproperty-directive.md) that is included in the [**INF *DDInstall* section**](./inf-ddinstall-section.md) of the INF file that installs the device. You can retrieve the value of DEVPKEY_DrvPkg_DetailedDescription by calling [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

The following is an example of how to use an INF **AddProperty** directive to set the value of DEVPKEY_DrvPkg_DetailedDescription for a device instance that is installed by an INF *DDInstall* section "SampleDDInstallSection":

```cpp
[SampleDDinstallSection]
...
AddProperty=SampleAddPropertySection
...

[SampleAddPropertySection] 
DeviceDetailedDescription,,,,"<xml><h1>Microsoft DiscoveryCam 530</h1><h2>Overview<h2>The Microsoft DiscoveryCam is great.<p>Really.<p><h2>Features</h2>The Microsoft DiscoveryCam has three features.<ol><li>Feature 1</li><li>Feature 2</li><li>Feature 3</li></ol></xml>"
...
```

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also


[**INF AddProperty Directive**](./inf-addproperty-directive.md)

[**INF *DDInstall* Section**](./inf-ddinstall-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

