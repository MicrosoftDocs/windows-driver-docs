---
title: C28176
description: Warning C28176 The member of struct should not be modified by a driver.
ms.assetid: 837b2dcd-0682-460f-a3ae-ebd82bcc451b
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28176


warning C28176: The member of struct should not be modified by a driver

This warning indicates that a driver changed an undocumented structure member that drivers should never change.

Drivers should not write to the specified undocumented structure member. For most undocumented members of opaque or partially opaque structures, this prohibition is absolute. However, drivers may write certain undocumented structure members from within particular routines. For example, the [**DEVICE\_OBJECT.NextDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543147) member can be written only within a DRIVER\_INITIALIZE or DRIVER\_UNLOAD routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28176%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




