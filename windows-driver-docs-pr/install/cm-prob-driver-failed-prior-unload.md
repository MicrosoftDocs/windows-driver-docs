---
title: CM\_PROB\_DRIVER\_FAILED\_PRIOR\_UNLOAD
description: CM\_PROB\_DRIVER\_FAILED\_PRIOR\_UNLOAD
ms.assetid: c7639fd7-738f-4115-9abc-0bafca097b9e
keywords: ["CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD"]
---

# CM\_PROB\_DRIVER\_FAILED\_PRIOR\_UNLOAD


## <a href="" id="ddk-cm-prob-driver-failed-prior-unload-dg"></a>


The driver could not be loaded because a previous instance is still loaded.

### Error Code

38

### Display Message (Windows XP and later versions of Windows)

"Windows cannot load the device driver for this hardware because a previous instance of the device driver is still in memory. (Code 38)"

### Recommended Resolution (Windows XP and later versions of Windows)

A previous driver instance can still be loaded due to an incorrect reference count or a race between load and unload operations. Additionally, this message can appear if a driver is referenced by multiple [**INF AddService directives**](inf-addservice-directive.md) in one or more INF files.

Select **Restart Computer**, which will restart the computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




