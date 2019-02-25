---
title: Obtaining an HDAUDIO_BUS_INTERFACE_BDL DDI Object
description: Obtaining an HDAUDIO_BUS_INTERFACE_BDL DDI Object
ms.assetid: 142eb2f0-6c6d-4441-8ad7-0875546c1ab2
keywords:
- HDAUDIO_BUS_INTERFACE_BDL structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining an HDAUDIO\_BUS\_INTERFACE\_BDL DDI Object


As explained previously, the function driver for an audio or modem codec obtains a counted reference to an object with an HD Audio DDI by sending an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) IOCTL to the HD Audio bus driver.

The following table shows the input parameter values that the function driver writes into the IOCTL to obtain an [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) structure and a context object for the version of the HD Audio DDI that this structure defines.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CONST GUID *<em>InterfaceType</em></p></td>
<td align="left"><p><strong>GUID_HDAUDIO_BUS_INTERFACE_BDL</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>USHORT <em>Size</em></p></td>
<td align="left"><p><strong>sizeof</strong>(<a href="https://msdn.microsoft.com/library/windows/hardware/ff536416" data-raw-source="[&lt;strong&gt;HDAUDIO_BUS_INTERFACE_BDL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536416)"><strong>HDAUDIO_BUS_INTERFACE_BDL</strong></a>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>USHORT <em>Version</em></p></td>
<td align="left"><p>0x0100</p></td>
</tr>
<tr class="even">
<td align="left"><p>PINTERFACE <em>Interface</em></p></td>
<td align="left"><p>Pointer to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536416" data-raw-source="[&lt;strong&gt;HDAUDIO_BUS_INTERFACE_BDL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536416)"><strong>HDAUDIO_BUS_INTERFACE_BDL</strong></a> structure</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PVOID <em>InterfaceSpecificData</em></p></td>
<td align="left"><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

 

The function driver allocates the storage for the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) structure and includes a pointer to this structure in the IOCTL. In the preceding table, the pointer to the **HDAUDIO\_BUS\_INTERFACE\_BDL** structure is cast to type **PINTERFACE**, which is a pointer to a structure of type [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825). The names and types of the first five members of **HDAUDIO\_BUS\_INTERFACE\_BDL** match those of the five members of **INTERFACE**. **HDAUDIO\_BUS\_INTERFACE\_BDL** contains additional members that are function pointers to the DDI routines. In response to receiving the IOCTL from the function driver, the HD Audio bus driver fills in the entire **HDAUDIO\_BUS\_INTERFACE\_BDL** structure.

The following table shows the values that the HD Audio bus driver writes into the first five members of the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) structure.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>USHORT <strong>Size</strong></p></td>
<td align="left"><p><strong>sizeof</strong>(<a href="https://msdn.microsoft.com/library/windows/hardware/ff536416" data-raw-source="[&lt;strong&gt;HDAUDIO_BUS_INTERFACE_BDL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536416)"><strong>HDAUDIO_BUS_INTERFACE_BDL</strong></a>)</p></td>
</tr>
<tr class="even">
<td align="left"><p>USHORT <strong>Version</strong></p></td>
<td align="left"><p>0x0100</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PVOID <strong>Context</strong></p></td>
<td align="left"><p>Context information that needs to be passed as the first call parameter to every DDI routine</p></td>
</tr>
<tr class="even">
<td align="left"><p>PINTERFACE_REFERENCE <strong>InterfaceReference</strong></p></td>
<td align="left"><p>Pointer to a routine that increments the context object&#39;s reference count</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PINTERFACE_DEREFERENCE <strong>InterfaceDereference</strong></p></td>
<td align="left"><p>Pointer to a routine that decrements the context object&#39;s reference count</p></td>
</tr>
</tbody>
</table>

 

In the preceding table, the **Context** member points to a context object that contains information that is specific to the particular instance of the HDAUDIO\_BUS\_INTERFACE\_BDL version of the DDI that the client obtains from the IOCTL. As explained previously, when calling any of the routines in the DDI, the client function driver must always specify the **Context** pointer value as the first call parameter.

 

 




