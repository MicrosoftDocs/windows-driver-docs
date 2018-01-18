---
title: PnpRemove rule (wdm)
description: The PnpRemove rule specifies that the driver cannot complete IRP\_MN\_SURPRISE\_REMOVAL, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_STOP\_DEVICE, or IRP\_MN\_REMOVE\_DEVICE requests with a failure.
ms.assetid: 2713F943-36A2-41B9-B9C0-86FC06B22443
keywords: ["PnpRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpRemove
api_type:
- NA
---

# PnpRemove rule (wdm)


The **PnpRemove** rule specifies that the driver cannot complete IRP\_MN\_SURPRISE\_REMOVAL, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_STOP\_DEVICE, or IRP\_MN\_REMOVE\_DEVICE requests with a failure.

> [!NOTE]
> In Windows 8.1, you can test the **PnpRemove** rule using [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448). The rule is not currently available for use with [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808).

 

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00043006) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20PnpRemove%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




