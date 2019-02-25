---
title: Obsolete Port Class Functions
description: Obsolete Port Class Functions
ms.assetid: 6fcb5ae6-81bc-423e-9757-34955a2de522
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Obsolete Port Class Functions


## <span id="ddk_obsolete_port_class_functions_ks"></span><span id="DDK_OBSOLETE_PORT_CLASS_FUNCTIONS_KS"></span>


The header file portcls.hdefines macros that contain the names of obsolete PortCls functions that have been replaced by new PortCls functions. These macros allow old source code that contains references to obsolete PortCls function names to be recompiled to use the new PortCls functions without requiring any edits to the source files.

When compiling source code that uses the obsolete names, define the parameter name PC\_OLD\_NAMES. This parameter can be defined by the compiler command-line argument "-DPC\_OLD\_NAMES" if that is more convenient than introducing the statement `#define PC_OLD_NAMES` into the source files themselves.

The following table lists the obsolete PortCls function names in the left column. For each obsolete name, the center column contains the name of the new PortCls function that replaces it.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Obsolete function name</th>
<th align="left">New function name</th>
<th align="left">Did arguments change?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>AddAdapterDevice</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537683" data-raw-source="[&lt;strong&gt;PcAddAdapterDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537683)"><strong>PcAddAdapterDevice</strong></a></p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="even">
<td align="left"><p>CompletePendingPropertyRequest</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537687" data-raw-source="[&lt;strong&gt;PcCompletePendingPropertyRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537687)"><strong>PcCompletePendingPropertyRequest</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GetTimeInterval</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537702" data-raw-source="[&lt;strong&gt;PcGetTimeInterval&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537702)"><strong>PcGetTimeInterval</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>InitializeAdapterDriver</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537703" data-raw-source="[&lt;strong&gt;PcInitializeAdapterDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537703)"><strong>PcInitializeAdapterDriver</strong></a></p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NewDmaChannel</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537712" data-raw-source="[&lt;strong&gt;PcNewDmaChannel&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537712)"><strong>PcNewDmaChannel</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>NewMiniport</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537714" data-raw-source="[&lt;strong&gt;PcNewMiniport&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537714)"><strong>PcNewMiniport</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NewPort</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537715" data-raw-source="[&lt;strong&gt;PcNewPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537715)"><strong>PcNewPort</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>NewResourceList</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537717" data-raw-source="[&lt;strong&gt;PcNewResourceList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537717)"><strong>PcNewResourceList</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NewResourceSublist</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537718" data-raw-source="[&lt;strong&gt;PcNewResourceSublist&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537718)"><strong>PcNewResourceSublist</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>NewServiceGroup</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537719" data-raw-source="[&lt;strong&gt;PcNewServiceGroup&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537719)"><strong>PcNewServiceGroup</strong></a></p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RegisterPhysicalConnection</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537726" data-raw-source="[&lt;strong&gt;PcRegisterPhysicalConnection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537726)"><strong>PcRegisterPhysicalConnection</strong></a></p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="even">
<td align="left"><p>RegisterPhysicalConnectionFromExternal</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537728" data-raw-source="[&lt;strong&gt;PcRegisterPhysicalConnectionFromExternal&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537728)"><strong>PcRegisterPhysicalConnectionFromExternal</strong></a></p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RegisterPhysicalConnectionToExternal</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537729" data-raw-source="[&lt;strong&gt;PcRegisterPhysicalConnectionToExternal&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537729)"><strong>PcRegisterPhysicalConnectionToExternal</strong></a></p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="even">
<td align="left"><p>RegisterSubdevice</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537731" data-raw-source="[&lt;strong&gt;PcRegisterSubdevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537731)"><strong>PcRegisterSubdevice</strong></a></p></td>
<td align="left"><p>YES</p></td>
</tr>
</tbody>
</table>

 

In some cases, the change amounts to no more than a simple name change: The qualifier `Pc` is inserted at the beginning of the name to indicate that the function is implemented in PortCls. In other cases, however, the argument list has changed in addition to the name of the function. The right column in the preceding table indicates whether the arguments have changed.

In cases in which the arguments changed, the macros in portcls.hconvert the argument lists for the obsolete PortCls functions to the equivalent arguments for the new PortCls functions. The following macros contain argument conversions:

```cpp
#define InitializeAdapterDriver(c1,c2,a) \
    PcInitializeAdapterDriver(PDRIVER_OBJECT(c1),PUNICODE_STRING(c2),PDRIVER_ADD_DEVICE(a))
#define AddAdapterDevice(c1,c2,s,m) \
    PcAddAdapterDevice(PDRIVER_OBJECT(c1),PDEVICE_OBJECT(c2),s,m,0)
#define RegisterSubdevice(c1,c2,n,u) \
    PcRegisterSubdevice(PDEVICE_OBJECT(c1),n,u)
#define RegisterPhysicalConnection(c1,c2,fs,fp,ts,tp) \
    PcRegisterPhysicalConnection(PDEVICE_OBJECT(c1),fs,fp,ts,tp)
#define RegisterPhysicalConnectionToExternal(c1,c2,fs,fp,ts,tp) \
    PcRegisterPhysicalConnectionToExternal(PDEVICE_OBJECT(c1),fs,fp,ts,tp)
#define RegisterPhysicalConnectionFromExternal(c1,c2,fs,fp,ts,tp) \
    PcRegisterPhysicalConnectionFromExternal(PDEVICE_OBJECT(c1),fs,fp,ts,tp)
```

 

 





