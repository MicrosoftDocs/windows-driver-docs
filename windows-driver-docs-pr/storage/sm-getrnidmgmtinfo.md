---
title: SM\_GetRNIDMgmtInfo function
description: The SM\_GetRNIDMgmtInfo WMI method retrieves FC3 management information that is associated with a Fibre Channel adapter.
ms.assetid: 0d414701-6e60-4d9d-85ae-f82b742ee907
keywords: ["SM_GetRNIDMgmtInfo function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_GetRNIDMgmtInfo
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# SM\_GetRNIDMgmtInfo function


The SM\_GetRNIDMgmtInfo WMI method retrieves FC3 management information that is associated with a Fibre Channel adapter.

Syntax
------

```ManagedCPlusPlus
void SM_GetRNIDMgmtInfo(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus,
   [out] HBAFC3MgmtInfo                    MgmtInfo
);
```

Parameters
----------

*HBAStatus*   
A WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_GetRNIDMgmtInfo\_OUT structure.

*MgmtInfo*   
A structure of type HBAFC3MgmtInfo that holds FC3 management information that is associated with a fibre channel adapter.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_FabricAndDomainManagementMethods WMI Class.

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

[**SM\_GetRNIDMgmtInfo\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566252)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SM_GetRNIDMgmtInfo%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





