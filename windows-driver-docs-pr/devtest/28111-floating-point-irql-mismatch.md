---
title: C28111
description: Warning C28111 The IRQL where the floating-point state was saved does not match the current IRQL (for this restore operation).
ms.assetid: 3573ebf0-5f5b-4b04-835a-7dba36e95e8c
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28111


warning C28111: The IRQL where the floating-point state was saved does not match the current IRQL (for this restore operation).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The floating Save/Restore functions require that the IRQL be the same at the time of save and the corresponding restore.</p></td>
</tr>
</tbody>
</table>

 

The IRQL at which the driver is executing when it restores a floating-point state is different than the IRQL at which it was executing when it saved the floating-point state.

Because the IRQL at which the driver runs determines how the floating-point state is saved, the driver must be executing at the same IRQL when it calls the functions to save and to restore the floating-point state.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
void driver_utility()
{
    // running at APC level
    KFLOATING_SAVE FloatBuf;
    if (KeSaveFloatingPointState(&FloatBuf))
    {
        KeLowerIrql(PASSIVE_LEVEL);
        ...
        KeRestoreFloatingPointState(&FloatBuf);
    }
}
```

The following code example avoids this warning.

```
void driver_utility()
{
    // running at APC level
    KFLOATING_SAVE FloatBuf;
    if (KeSaveFloatingPointState(&FloatBuf))
    {
        KeLowerIrql(PASSIVE_LEVEL);
        ...
        KeRaiseIrql(APC_LEVEL, &old);
        KeRestoreFloatingPointState(&FloatBuf);
    }
}
```

 

 





