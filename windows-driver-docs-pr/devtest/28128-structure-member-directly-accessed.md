---
title: C28128
description: Warning C28128 An access to a field has been made directly. It should be made by a routine.
ms.assetid: 66b3345b-fab8-4f1a-b7ab-dfc5e70ca312
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28128


warning C28128: An access to a field has been made directly. It should be made by a routine.

The driver directly accessed a structure member that should be accessed only by using specialized functions.

For example, you should use the [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) instead of directly modifying the **CancelRoutine** member of the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
irp->CancelRoutine = myCancelRoutine;
```

The following code example avoids this warning.

```
oldCancel = IoSetCancelRoutine(irp, myCancelRoutine);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28128%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




