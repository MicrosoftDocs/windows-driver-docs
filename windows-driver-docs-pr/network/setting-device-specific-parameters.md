---
title: Setting Device-Specific Parameters
description: Setting Device-Specific Parameters
ms.assetid: 5df72c11-e8d4-4e06-8f34-c9b85ad779f6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Device-Specific Parameters





It is expected that most Remote NDIS devices will function well without the need to configure parameters on the host. However, there may be cases where proper network operation requires some configuration on the host. If the device supports configurable parameters, then it should include the following optional OID in the list of supported OIDs it reports in response to a query for [OID\_GEN\_SUPPORTED\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569642):

```C++
#define OID_GEN_RNDIS_CONFIG_PARAMETER 0x0001021B
```

If the device supports the [OID\_GEN\_RNDIS\_CONFIG\_PARAMETER](https://msdn.microsoft.com/library/windows/hardware/ff569639) OID, the host uses it to set device-specific parameters, soon after the device enters a state initialized by Remote NDIS from the uninitialized state. The host will send zero or more REMOTE\_NDIS\_SET\_MSGs to the device, with OID\_GEN\_RNDIS\_CONFIG\_PARAMETER as the OID value to set. Each such [**REMOTE\_NDIS\_SET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570654) corresponds to one device-specific parameter that is configured on the host.

The *InformationBuffer* associated with each such [**REMOTE\_NDIS\_SET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570654) has the following format. Note that the Offset values are relative to the beginning of the information buffer.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset</th>
<th align="left">Size</th>
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>ParameterNameOffset</p></td>
<td align="left"><p>Specifies the byte offset from the beginning of the ParameterNameOffset field at which a Unicode character string representing the parameter name is located. The string does not include a NULL terminator.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>ParameterNameLength</p></td>
<td align="left"><p>Specifies the byte length of the parameter name string.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>8</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>ParameterType</p></td>
<td align="left"><p>Specifies the data type of the parameter value. This is one of the following: 0 - numeric value; 2 - string value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>12</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>ParameterValueOffset</p></td>
<td align="left"><p>Specifies the byte offset from the beginning of the ParameterNameOffset field at which the parameter value is located.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>16</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>ParameterValueLength</p></td>
<td align="left"><p>Specifies the byte length of the parameter value.</p></td>
</tr>
</tbody>
</table>

 

The device sends a [**REMOTE\_NDIS\_SET\_CMPLT**](https://msdn.microsoft.com/library/windows/hardware/ff570651) in response to each [**REMOTE\_NDIS\_SET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570654), after applying the parameter value. If the parameter setting is acceptable, it returns a status of RNDIS\_STATUS\_SUCCESS in the response. If the parameter setting is not acceptable, and the device cannot apply a useful default value for this parameter, then the device returns an appropriate error status value (see section on status values). If an error status is returned, then the host will initiate a halt process for the device.

Device-specific parameters are expected to be configured in the Windows registry. The keys that define parameter values are typically created in the registry during the process of device installation. The list of keys, type information, default values and optional range of valid values are specified in the INF file for the device. For more information about using an INF to set up configuration parameters in the registry for network devices, consult the Windows 2000 Driver Development Kit (DDK).

 

 





