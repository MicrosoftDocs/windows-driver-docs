---
title: Registry Key Objects
description: Registry Key Objects
ms.assetid: c666f0cc-5a8a-4df8-9c65-08e3b044a08f
keywords:
- helper objects WDK audio , registry key objects
- registry key objects WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Key Objects


## <span id="registry_key_objects"></span><span id="REGISTRY_KEY_OBJECTS"></span>


The PortCls system driver implements the [IRegistryKey](https://msdn.microsoft.com/library/windows/hardware/ff536965) interface for the benefit of miniport drivers. An IRegistryKey object represents a registry key. Miniport drivers use registry key objects to do the following:

-   Create and delete registry keys

-   Enumerate registry keys

-   Query and set registry keys

When querying a registry key object for information about a registry entry under the specified key, the query can output the information in one of three formats, each of which uses a different key-query structure. The following table shows the [**KEY\_INFORMATION\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff553373) enumeration values that indicate which of the three key-query structures is output by the query.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553355" data-raw-source="[&lt;strong&gt;KEY_BASIC_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553355)"><strong>KEY_BASIC_INFORMATION</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>KeyFullInformation</strong></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553367" data-raw-source="[&lt;strong&gt;KEY_FULL_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553367)"><strong>KEY_FULL_INFORMATION</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>KeyNodeInformation</strong></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553392" data-raw-source="[&lt;strong&gt;KEY_NODE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553392)"><strong>KEY_NODE_INFORMATION</strong></a></p></td>
</tr>
</tbody>
</table>

 

To open an existing registry key or create a new registry key, an adapter driver can call the [**PcNewRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff537716) function, and a miniport driver can call the port driver's [**IPort::NewRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff536945) method. The two calls are similar, except that the **PcNewRegistryKey** function requires two additional parameters, *DeviceObject* and *SubDevice*. For more information, see **PcNewRegistryKey**.

When a miniport driver creates a new [IRegistryKey](https://msdn.microsoft.com/library/windows/hardware/ff536965) object, the object either opens an existing subkey or creates a new registry subkey if none exists. In either case, the registry key object stores the handle to the key. When that object is later released and its reference count decrements to zero, the object automatically closes its handle to the key.

The [IRegistryKey](https://msdn.microsoft.com/library/windows/hardware/ff536965) interface supports the following methods:

[**IRegistryKey::DeleteKey**](https://msdn.microsoft.com/library/windows/hardware/ff536967)

[**IRegistryKey::EnumerateKey**](https://msdn.microsoft.com/library/windows/hardware/ff536968)

[**IRegistryKey::EnumerateValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff536969)

[**IRegistryKey::NewSubKey**](https://msdn.microsoft.com/library/windows/hardware/ff536970)

[**IRegistryKey::QueryKey**](https://msdn.microsoft.com/library/windows/hardware/ff536971)

[**IRegistryKey::QueryRegistryValues**](https://msdn.microsoft.com/library/windows/hardware/ff536972)

[**IRegistryKey::QueryValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff536973)

[**IRegistryKey::SetValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff536975)

 

 




