---
title: NDIS\_RAISE\_IRQL\_TO\_DISPATCH macro
description: The NDIS\_RAISE\_IRQL\_TO\_DISPATCH macro raises the current IRQL to DISPATCH\_LEVEL on the current processor.
MS-HAID:
- 'ndis\_interrupts\_sync\_macros\_ref\_e2b1e130-0060-4468-8e76-53f890e2d7a4.xml'
- 'netvista.ndis\_raise\_irql\_to\_dispatch'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 37e78374-8ac1-4aa4-9a53-bce3a3411064
keywords: ["NDIS_RAISE_IRQL_TO_DISPATCH macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_RAISE_IRQL_TO_DISPATCH
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NDIS\_RAISE\_IRQL\_TO\_DISPATCH macro


The NDIS\_RAISE\_IRQL\_TO\_DISPATCH macro raises the current IRQL to DISPATCH\_LEVEL on the current processor.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_RAISE_IRQL_TO_DISPATCH(
   PKIRQL _pIrql_
);
```

Parameters
----------

*\_pIrql\_*   
A pointer to a KIRQL-type variable where NDIS\_RAISE\_IRQL\_TO\_DISPATCH stores the original (that is, unraised) IRQL value. You should use this original IRQL value in a subsequent call to the [**NDIS\_LOWER\_IRQL**](ndis-lower-irql.md) macro.

Return value
------------

None

Remarks
-------

NDIS network drivers should use the NDIS\_RAISE\_IRQL\_TO\_DISPATCH macro to raise the current IRQL.

If the current IRQL is greater than DISPATCH\_LEVEL, a bugcheck occurs. Otherwise, the macro sets the current IRQL to DISPATCH\_LEVEL.

NDIS\_RAISE\_IRQL\_TO\_DISPATCH is an NDIS wrapper for the [**KeRaiseIrql**](https://msdn.microsoft.com/library/windows/hardware/ff553079) routine.

The caller should call the [**NDIS\_LOWER\_IRQL**](ndis-lower-irql.md) macro to restore the original IRQL as soon as possible.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td>[<strong>Irql_IrqlSetting_Function</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547962)</td>
</tr>
</tbody>
</table>

## See also


[**KeRaiseIrql**](https://msdn.microsoft.com/library/windows/hardware/ff553079)

[**NDIS\_LOWER\_IRQL**](ndis-lower-irql.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_RAISE_IRQL_TO_DISPATCH%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





