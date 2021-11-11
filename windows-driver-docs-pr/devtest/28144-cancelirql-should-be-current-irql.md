---
title: C28144 warning
description: Warning C28144 Within a cancel routine, at the point of exit, the IRQL in Irp- CancelIrql should be the current IRQL.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28144"
---

# C28144


warning C28144: Within a cancel routine, at the point of exit, the IRQL in Irp-&gt;CancelIrql should be the current IRQL.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The value need not be restored by any specific function, but must be restored before exit. PREfast was unable to determine that it was restored to the required value.</p></td>
</tr>
</tbody>
</table>

 

When the driver's [**Cancel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine exits, the value of the **Irp-&gt;CancelIrql** member is not the current IRQL. Typically, this error occurs when the driver does not call [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)) with the IRQL that was supplied by the most recent call to [**IoAcquireCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff548196(v=vs.85)).

For more information about *Cancel* routines, see [Canceling IRPs](../kernel/canceling-irps.md). For information specific to this warning, see [Points to Consider When Canceling IRPs](../kernel/points-to-consider-when-canceling-irps.md).

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
IoReleaseCancelSpinLock(PASSIVE_LEVEL);
```

The following code example avoids this warning.

```
IoReleaseCancelSpinLock(Irp->CancelIrql);
```

 

