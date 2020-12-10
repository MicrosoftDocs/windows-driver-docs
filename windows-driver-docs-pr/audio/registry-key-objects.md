---
title: Registry Key Objects
description: Registry Key Objects
keywords:
- helper objects WDK audio , registry key objects
- registry key objects WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Key Objects


## <span id="registry_key_objects"></span><span id="REGISTRY_KEY_OBJECTS"></span>


The PortCls system driver implements the [IRegistryKey](/windows-hardware/drivers/ddi/portcls/nn-portcls-iregistrykey) interface for the benefit of miniport drivers. An IRegistryKey object represents a registry key. Miniport drivers use registry key objects to do the following:

-   Create and delete registry keys

-   Enumerate registry keys

-   Query and set registry keys

When querying a registry key object for information about a registry entry under the specified key, the query can output the information in one of three formats, each of which uses a different key-query structure. The following table shows the [**KEY\_INFORMATION\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_key_information_class) enumeration values that indicate which of the three key-query structures is output by the query.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">KEY_INFORMATION_CLASS Value</th>
<th align="left">Key-Query Structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>KeyBasicInformation</strong></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_key_basic_information" data-raw-source="[&lt;strong&gt;KEY_BASIC_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_key_basic_information)"><strong>KEY_BASIC_INFORMATION</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>KeyFullInformation</strong></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_key_full_information" data-raw-source="[&lt;strong&gt;KEY_FULL_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_key_full_information)"><strong>KEY_FULL_INFORMATION</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>KeyNodeInformation</strong></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_key_node_information" data-raw-source="[&lt;strong&gt;KEY_NODE_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_key_node_information)"><strong>KEY_NODE_INFORMATION</strong></a></p></td>
</tr>
</tbody>
</table>

 

To open an existing registry key or create a new registry key, an adapter driver can call the [**PcNewRegistryKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewregistrykey) function, and a miniport driver can call the port driver's [**IPort::NewRegistryKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iport-newregistrykey) method. The two calls are similar, except that the **PcNewRegistryKey** function requires two additional parameters, *DeviceObject* and *SubDevice*. For more information, see **PcNewRegistryKey**.

When a miniport driver creates a new [IRegistryKey](/windows-hardware/drivers/ddi/portcls/nn-portcls-iregistrykey) object, the object either opens an existing subkey or creates a new registry subkey if none exists. In either case, the registry key object stores the handle to the key. When that object is later released and its reference count decrements to zero, the object automatically closes its handle to the key.

The [IRegistryKey](/windows-hardware/drivers/ddi/portcls/nn-portcls-iregistrykey) interface supports the following methods:

[**IRegistryKey::DeleteKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-deletekey)

[**IRegistryKey::EnumerateKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-enumeratekey)

[**IRegistryKey::EnumerateValueKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-enumeratevaluekey)

[**IRegistryKey::NewSubKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-newsubkey)

[**IRegistryKey::QueryKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-querykey)

[**IRegistryKey::QueryRegistryValues**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-queryregistryvalues)

[**IRegistryKey::QueryValueKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-queryvaluekey)

[**IRegistryKey::SetValueKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iregistrykey-setvaluekey)

