---
title: SM\_GetBindingCapability function
description: The SM\_GetBindingCapability method retrieves the binding capabilities for the indicated port.
ms.assetid: 11b7df8b-2694-4c49-a97a-ed475f3e841f
keywords: ["SM_GetBindingCapability function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_GetBindingCapability
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# SM\_GetBindingCapability function


The SM\_GetBindingCapability method retrieves the binding capabilities for the indicated port.

Syntax
------

```ManagedCPlusPlus
void SM_GetBindingCapability(
   [in, HBAType("HBA_WWN")] uint8                 HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                 DomainPortWWN[8],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS        HBAStatus,
   [out, HBAType("SMHBA_BIND_CAPABILITY")] uint32 HBAType
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the port whose persistent bindings will be retrieved.

*DomainPortWWN*   
The worldwide name (WWN) for the callback. It is the Port\_Identifier that has the smallest value of any Port\_Identifier of an SMP port that was discovered by using the physical fibre channel port. It has a value of zero if no SMP port has been discovered by using the physical fibre channel port.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see the [HBA\_STATUS](hba-status.md) structure. The miniport driver returns this information in the HBAStatus member of a GetBindingCapability\_OUT structure.

*HBAType*   
The ability of an HBA and its miniport driver to provide a specific set of features that are related to persistent binding. For a list of values that this parameter can have, see the description of the HBA\_BIND\_TYPE WMI class qualifier.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

The SM\_GetBindingSupport method returns the binding capability that is currently enabled, whereas the SM\_GetBindingCapability method indicates the binding capability of the port without reference to whether particular bindings are enabled or not. This WMI method belongs to the MS\_SM\_TargetInformationMethods WMI Class.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Hbapiwmi.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

[**SM\_GetBindingCapability\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566224)

[**SM\_GetBindingCapability\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566227)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SM_GetBindingCapability%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





