---
title: Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object
description: Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object
ms.assetid: 3aad8c7a-8c89-499a-bfe8-e3facdffcd15
---

# Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object


The following table shows the input parameter values that the function driver writes into the [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) IOCTL to obtain an [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) structure and a context object for the version of the HD Audio DDI that this structure defines.

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
<td align="left"><p><strong>GUID_HDAUDIO_BUS_INTERFACE_V2</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>USHORT <em>Size</em></p></td>
<td align="left"><p><strong>sizeof</strong>([<strong>HDAUDIO_BUS_INTERFACE_V2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff536418))</p></td>
</tr>
<tr class="odd">
<td align="left"><p>USHORT <em>Version</em></p></td>
<td align="left"><p>0x0100</p></td>
</tr>
<tr class="even">
<td align="left"><p>PINTERFACE <em>Interface</em></p></td>
<td align="left"><p>Pointer to [<strong>HDAUDIO_BUS_INTERFACE_V2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff536418) structure</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PVOID <em>InterfaceSpecificData</em></p></td>
<td align="left"><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

 

The function driver allocates the storage for the [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) structure and includes a pointer to this structure in the IOCTL. In the previous table, the pointer to the **HDAUDIO\_BUS\_INTERFACE\_V2** structure is cast to type **PINTERFACE**, which is a pointer to a structure of type [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825). The names and types of the first five members of **HDAUDIO\_BUS\_INTERFACE\_V2** match those of the five members of **INTERFACE**. **HDAUDIO\_BUS\_INTERFACE\_V2** contains additional members that are function pointers to the DDI routines. In response to receiving the IOCTL from the function driver, the HD Audio bus driver populates the **HDAUDIO\_BUS\_INTERFACE\_V2** structure.

The following table shows the values that the HD Audio bus driver writes into the first five members of the [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) structure.

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
<td align="left"><p><strong>sizeof</strong>([<strong>HDAUDIO_BUS_INTERFACE_V2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff536418))</p></td>
</tr>
<tr class="even">
<td align="left"><p>USHORT <strong>Version</strong></p></td>
<td align="left"><p>0x0100</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PVOID <strong>Context</strong></p></td>
<td align="left"><p>Context information that must be passed as the first call parameter to every DDI routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PINTERFACE_REFERENCE <strong>InterfaceReference</strong></p></td>
<td align="left"><p>A pointer to a routine that increments the context object's reference count.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PINTERFACE_DEREFERENCE <strong>InterfaceDereference</strong></p></td>
<td align="left"><p>A pointer to a routine that decrements the context object's reference count.</p></td>
</tr>
</tbody>
</table>

 

In the previous table, the **Context** member points to a context object that contains information that is specific to the particular instance of the baseline HD Audio DDI. The client obtains this baseline HD Audio DDI from the IOCTL. When the client function driver calls any of the routines in the DDI, it must always specify the **Context** member value as the first call parameter. The context information is opaque to the client. The HD Audio bus driver creates a different context object for each client. When the context object is no longer required, the client frees the context object by calling the **InterfaceDereference** routine shown in the previous table. If it is required, a client can create additional references to the object by calling the **InterfaceDereference** routine, but the client is responsible for releasing these references when it no longer requires them.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Obtaining%20an%20HDAUDIO_BUS_INTERFACE_V2%20DDI%20Object%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




