---
Description: Registry Key Objects
MS-HAID: 'audio.registry\_key\_objects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Registry Key Objects
---

# Registry Key Objects


## <span id="registry_key_objects"></span><span id="REGISTRY_KEY_OBJECTS"></span>


The PortCls system driver implements the [IRegistryKey](audio.iregistrykey) interface for the benefit of miniport drivers. An IRegistryKey object represents a registry key. Miniport drivers use registry key objects to do the following:

-   Create and delete registry keys

-   Enumerate registry keys

-   Query and set registry keys

When querying a registry key object for information about a registry entry under the specified key, the query can output the information in one of three formats, each of which uses a different key-query structure. The following table shows the [**KEY\_INFORMATION\_CLASS**](kernel.key_information_class) enumeration values that indicate which of the three key-query structures is output by the query.

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
<td align="left"><p>[<strong>KEY_BASIC_INFORMATION</strong>](kernel.key_basic_information)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>KeyFullInformation</strong></p></td>
<td align="left"><p>[<strong>KEY_FULL_INFORMATION</strong>](kernel.key_full_information)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>KeyNodeInformation</strong></p></td>
<td align="left"><p>[<strong>KEY_NODE_INFORMATION</strong>](kernel.key_node_information)</p></td>
</tr>
</tbody>
</table>

 

To open an existing registry key or create a new registry key, an adapter driver can call the [**PcNewRegistryKey**](audio.pcnewregistrykey) function, and a miniport driver can call the port driver's [**IPort::NewRegistryKey**](audio.iport_newregistrykey) method. The two calls are similar, except that the **PcNewRegistryKey** function requires two additional parameters, *DeviceObject* and *SubDevice*. For more information, see **PcNewRegistryKey**.

When a miniport driver creates a new [IRegistryKey](audio.iregistrykey) object, the object either opens an existing subkey or creates a new registry subkey if none exists. In either case, the registry key object stores the handle to the key. When that object is later released and its reference count decrements to zero, the object automatically closes its handle to the key.

The [IRegistryKey](audio.iregistrykey) interface supports the following methods:

[**IRegistryKey::DeleteKey**](audio.iregistrykey_deletekey)

[**IRegistryKey::EnumerateKey**](audio.iregistrykey_enumeratekey)

[**IRegistryKey::EnumerateValueKey**](audio.iregistrykey_enumeratevaluekey)

[**IRegistryKey::NewSubKey**](audio.iregistrykey_newsubkey)

[**IRegistryKey::QueryKey**](audio.iregistrykey_querykey)

[**IRegistryKey::QueryRegistryValues**](audio.iregistrykey_queryregistryvalues)

[**IRegistryKey::QueryValueKey**](audio.iregistrykey_queryvaluekey)

[**IRegistryKey::SetValueKey**](audio.iregistrykey_setvaluekey)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Registry%20Key%20Objects%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



