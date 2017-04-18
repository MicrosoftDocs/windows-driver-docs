---
title: C28101
description: Warning C28101 The Drivers module has inferred that the current function is not the correct type of function.
ms.assetid: 81a68dd6-ff9d-4cb2-9bd9-3a0f0d152230
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28101


warning C28101: The Drivers module has inferred that the current function is not the correct type of function

The Code Analysis tool has detected that a function is of a particular type, such as a callback function. This is an informational message only. It does not indicate an error.

This message indicates that the Code Analysis tool is applying rules that are specific to that function type. If this inference is wrong, the Code Analysis tool will generate false-positive warnings, but those warnings can be safely ignored. For more information, see [Using Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=227826).

The *function signature* (the arguments and result type) are used to identify the function whenever possible. Some standard driver routines, such as [**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) and [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858), have the same signature, so the name is checked to see if it matches the conventional name for that function. Other functions might be checked for conventional names.

To suppress this warning when it is redundant, you can explicitly declare the function to be of a particular function type. The functions that are detected this way are typically callback functions. The proper action is to declare them using a function typedef. For more information, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28101%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




