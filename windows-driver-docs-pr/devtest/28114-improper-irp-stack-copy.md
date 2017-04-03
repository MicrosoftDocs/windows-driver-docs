---
title: C28114
description: Warning C28114 Copying a whole IRP stack entry leaves certain fields initialized that should be cleared or updated.
ms.assetid: 39e3e313-e40f-4cb9-a534-c9e74fd1e88b
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28114


warning: C28114: Copying a whole IRP stack entry leaves certain fields initialized that should be cleared or updated.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Use <strong>IoCopyCurrentIrpStackLocationToNext</strong> to accomplish this</p></td>
</tr>
</tbody>
</table>

 

The driver is copying an IRP improperly. Improperly copying an IRP can cause serious problems with a driver, including loss of data and system crashes. If an IRP must be copied and [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387) does not suffice, then certain members of the IRP should not be copied or should be zeroed after copying.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28114%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




