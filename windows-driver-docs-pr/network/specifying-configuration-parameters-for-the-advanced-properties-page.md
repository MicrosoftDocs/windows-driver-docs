---
title: Specifying config parameters for the Advanced Properties page
description: Specifying Configuration Parameters for the Advanced Properties Page
ms.assetid: 9c243edb-f667-4244-8de2-8335fac43220
keywords:
- add-registry-sections WDK networking , Advanced properties page configuration
- Advanced properties page configuration WDK networking
- parameters WDK networking
- configuration parameters WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Configuration Parameters for the Advanced Properties Page

> [!NOTE]
> Prior to Windows 10, version 1703, driver upgrades and Windows updates could result in changes to INF values that the driver had previously defined in the **Advanced** properties page.
> Starting in Windows 10, version 1703, advanced properties that a driver specifies in its INF file persist through these updates.



An INF file that installs a Net component (adapter) can specify adapter configuration parameters for display in the **Advanced** properties page for the component. Configuration values specified by the user in the **Advanced** properties page are written to the root instance key for the component.

Note that if an adapter supports an **Advanced** properties page, the **Characteristics** entry in the *DDInstall* section for the adapter must include the NCF\_HAS\_UI value.

A network INF file specifies configuration parameters for display in the Advanced page through an *add-registry-section* that is referenced by the *DDInstall* section for the component. Such an *add-registry-section* adds one or more configuration subkeys to the **Ndi\\params** key. The format for a configuration parameter subkey is **Ndi\\params\\**<em>SubKeyName</em>, where *SubKeyName* is a REG\_SZ value that specifies a vendor-specific parameter name. For example, the key for a parameter that specifies a transceiver type could be named **Ndi\\params\\TransceiverType**.

The following keywords are reserved and cannot be used as an **Ndi\\params\\**<em>SubKeyName</em>: **BundleId**, **BusType**, **Characteristics**, **ComponentId**, **Description**, **DeviceInstanceId**, **DriverDate**, **DriverDesc**, **DriverVersion**, **InfPath**, **InfSection**, **InfSectionExt**,** *IfType** **InstallTimeStamp**, **Manufacturer**,** *MediaType*<em>, **NetCfgInstanceId</em>*, **NetLuidIndex*<em>,</em>* *PhysicalMediaType*<em>, **Provider</em><em>, and **ProviderName</em>*.

For each parameter subkey that is added to **Ndi\\params**, the *add-registry-section* must add **ParamDesc**(parameter description) and **Type** values. The *add-registry-section* can also add **Default** and **Optional** values for the parameter and, if the parameter is numeric, **Min**, **Max**, and **Step** values. The following table describes the values that can be added to each **Ndi\\params** key.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ParamDesc</p></td>
<td align="left"><p><em>String</em></p></td>
<td align="left"><p>Name displayed for the parameter on the <strong>Advanced</strong> page</p></td>
</tr>
<tr class="even">
<td align="left"><p>Type</p></td>
<td align="left"><p><strong>int</strong>, <strong>long</strong>, <strong>Word</strong>, <strong>dword</strong>, <strong>edit</strong>, or <strong>enum</strong></p></td>
<td align="left"><p>Type of parameter: <strong>int</strong>, <strong>long</strong>, <strong>Word</strong>, and <strong>dword</strong> specify a numeric parameter; <strong>edit</strong> and <strong>enum</strong> specify a text parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Default</p></td>
<td align="left"><p><em>default value</em></p></td>
<td align="left"><p>Default value for the parameter: for a numeric parameter, must be a numeric value ( <strong>int</strong>, <strong>long</strong>, <strong>Word</strong>, or <strong>dword</strong>) that matches the specified parameter type; for a text parameter, must be a string. Default values must be specified for required parameters. Default values can also be specified for optional parameters. When a user selects the option to enter a value for an optional parameter, the default value, if specified, appears in the edit box for that parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><strong>0</strong> or <strong>1</strong></p></td>
<td align="left"><p></p>
<strong>0</strong> required. Specify a value for the parameter or use the default value.
<strong>1</strong> optional. Can be marked <strong>Not Present</strong> on the <strong>Advanced</strong> page.</td>
</tr>
<tr class="odd">
<td align="left"><p>Min</p></td>
<td align="left"><p><em>numeric value</em></p></td>
<td align="left"><p>Minimum value for a numeric parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Max</p></td>
<td align="left"><p><em>numeric value</em></p></td>
<td align="left"><p>Maximum value for a numeric parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Step</p></td>
<td align="left"><p><em>numeric value</em></p></td>
<td align="left"><p>Step (interval) between valid values for a numeric parameter. The minimum value is the starting point.</p></td>
</tr>
</tbody>
</table>

 

The range of values for an **enum** parameter are specified with a subkey that has the following format:

**Ndi\\params\\**<em>SubKeyName</em>**\\enum**

Each enumerated value must have a subkey. Each **enum** subkey specifies a numeric value (starting with zero for the first enumerated value) and a description for that value.

The following is an example of an *add-registry-section* that adds a configuration parameter named **TransType**.

```INF
[a1.params.reg]
HKR, Ndi\params\TransType,      ParamDesc, 0, "Transceiver Type"
HKR, Ndi\params\TransType,      Type,      0, "enum"
HKR, Ndi\params\TransType,      Default,   0, "0"
HKR, Ndi\params\TransType,      Optional,  0, "0"
HKR, Ndi\params\TransType\enum, "0",       0, "Auto-Connector"
HKR, Ndi\params\TransType\enum, "1",       0, "Thick Net(AUI/DIX)"
HKR, Ndi\params\TransType\enum, "2",       0, "Thin Net (BNC/COAX)"
HKR, Ndi\params\TransType\enum, "3",       0, "Twisted-Pair (TPE)"
```

 

 





