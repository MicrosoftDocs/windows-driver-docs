---
title: C28715
description: Warning C28715 Cast between semantically different integer types.
ms.assetid: 49e37718-9950-4f63-a554-f924ae8cf0a4
---

# C28715


warning C28715: Cast between semantically different integer types

This warning indicates that a Boolean is being cast to **NTSTATUS**. This is likely to give undesirable results. For example, the typical failure value for functions that return a Boolean (**FALSE**) is a success status when tested as an **NTSTATUS**.

Typically, a function that returns Boolean returns either 1 (for **TRUE**) or 0 (for **FALSE**). Both these values are treated as success codes by the **NT\_SUCCESS** macro. Thus, the failure case will never be detected.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

PREfast reports the warning for the following example.

```
extern BOOL SomeFunction(void);

if (NT_SUCCESS(SomeFunction())) {
   return 0;
} else {
   return -1;
}
```

The following example avoids the error.

```
extern BOOL SomeFunction(void);

if (SomeFunction() == TRUE) {
   return 0;
} else {
   return -1;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28715%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




