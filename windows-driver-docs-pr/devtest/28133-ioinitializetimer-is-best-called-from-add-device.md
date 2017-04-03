---
title: C28133
description: Warning C28133 IoInitializeTimer is best called from AddDevice.
ms.assetid: c832cf67-1fc2-491b-a9e3-d35c5d9f6b73
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28133


warning C28133: IoInitializeTimer is best called from AddDevice

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>IoInitializeTimer can only be called once per device object. Calling it from the AddDevice routine helps assure that it is not unexpectedly called more than once.</p></td>
</tr>
</tbody>
</table>

 

The driver is calling [**IoInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549344) in a routine other than its **AddDevice** routine. The Code Analysis tool is using this opportunity to suggest a best practice recommendation that can prevent errors and make the driver code more reliable.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28133%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




