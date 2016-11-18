---
title: C28144
description: Warning C28144 Within a cancel routine, at the point of exit, the IRQL in Irp- CancelIrql should be the current IRQL.
ms.assetid: f89a2f9b-6e84-4696-80c3-79b8760c9b4a
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
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

 

When the driver's [**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine exits, the value of the **Irp-&gt;CancelIrql** member is not the current IRQL. Typically, this error occurs when the driver does not call [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) with the IRQL that was supplied by the most recent call to [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196).

For more information about *Cancel* routines, see [Canceling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff540748). For information specific to this warning, see [Points to Consider When Canceling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff559700).

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
IoReleaseCancelSpinLock(PASSIVE_LEVEL);
```

The following code example avoids this warning.

```
IoReleaseCancelSpinLock(Irp->CancelIrql);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28144%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




