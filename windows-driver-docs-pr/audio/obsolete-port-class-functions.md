---
title: Obsolete Port Class Functions
description: Obsolete Port Class Functions
ms.assetid: 6fcb5ae6-81bc-423e-9757-34955a2de522
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
<td align="left"><p>[<strong>PcAddAdapterDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537683)</p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="even">
<td align="left"><p>CompletePendingPropertyRequest</p></td>
<td align="left"><p>[<strong>PcCompletePendingPropertyRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537687)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GetTimeInterval</p></td>
<td align="left"><p>[<strong>PcGetTimeInterval</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537702)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>InitializeAdapterDriver</p></td>
<td align="left"><p>[<strong>PcInitializeAdapterDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537703)</p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NewDmaChannel</p></td>
<td align="left"><p>[<strong>PcNewDmaChannel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537712)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>NewMiniport</p></td>
<td align="left"><p>[<strong>PcNewMiniport</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537714)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NewPort</p></td>
<td align="left"><p>[<strong>PcNewPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537715)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>NewResourceList</p></td>
<td align="left"><p>[<strong>PcNewResourceList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537717)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NewResourceSublist</p></td>
<td align="left"><p>[<strong>PcNewResourceSublist</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537718)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="even">
<td align="left"><p>NewServiceGroup</p></td>
<td align="left"><p>[<strong>PcNewServiceGroup</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537719)</p></td>
<td align="left"><p>no</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RegisterPhysicalConnection</p></td>
<td align="left"><p>[<strong>PcRegisterPhysicalConnection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537726)</p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="even">
<td align="left"><p>RegisterPhysicalConnectionFromExternal</p></td>
<td align="left"><p>[<strong>PcRegisterPhysicalConnectionFromExternal</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537728)</p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RegisterPhysicalConnectionToExternal</p></td>
<td align="left"><p>[<strong>PcRegisterPhysicalConnectionToExternal</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537729)</p></td>
<td align="left"><p>YES</p></td>
</tr>
<tr class="even">
<td align="left"><p>RegisterSubdevice</p></td>
<td align="left"><p>[<strong>PcRegisterSubdevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537731)</p></td>
<td align="left"><p>YES</p></td>
</tr>
</tbody>
</table>

 

In some cases, the change amounts to no more than a simple name change: The qualifier `Pc` is inserted at the beginning of the name to indicate that the function is implemented in PortCls. In other cases, however, the argument list has changed in addition to the name of the function. The right column in the preceding table indicates whether the arguments have changed.

In cases in which the arguments changed, the macros in portcls.hconvert the argument lists for the obsolete PortCls functions to the equivalent arguments for the new PortCls functions. The following macros contain argument conversions:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Obsolete%20Port%20Class%20Functions%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




