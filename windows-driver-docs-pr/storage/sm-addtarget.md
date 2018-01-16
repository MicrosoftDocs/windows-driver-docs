---
title: SM\_AddTarget function
description: The SM\_AddTarget WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.
ms.assetid: 78e19496-1eb0-4d05-8637-f2e6d123208b
keywords: ["SM_AddTarget function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_AddTarget
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# SM\_AddTarget function


The SM\_AddTarget WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.

Syntax
------

```ManagedCPlusPlus
void SM_AddTarget(
   [in, HBAType("HBA_WWN")] uint8          HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DiscoveredPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DomainPortWWN[8],
   [in] uint32                             AllTargets,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*HbaPortWWN*   
The worldwide name (WWN) of the local port whose events the WMI client will receive.

*DiscoveredPortWWN*   
A worldwide name (WWN) that specifies the discovered target whose events the WMI client will receive.

*DomainPortWWN*   
A worldwide name (WWN) that specifies the SAS domain worldwide name of the local port whose events the WMI client will receive.

*AllTargets*   
The scope of the target events to report. If this member is zero, the WMI client receives events that are associated with the port that is indicated by DiscoveredPortWWN. If this member is nonzero, the WMI client receives all events that are associated with all currently discovered targets as well as targets that are discovered in the future.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_AddTarget\_OUT structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_EventControl WMI Class.

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

[**SM\_AddTarget\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566218)

[**SM\_AddTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566219)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SM_AddTarget%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





