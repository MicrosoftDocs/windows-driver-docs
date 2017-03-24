---
title: C28169
description: Warning C28169 The dispatch function does not have any \_Dispatch\_type\_ annotations.
ms.assetid: ce33993f-f967-43b0-89fb-d8553517aae3
---

# C28169


warning C28169: The dispatch function does not have any **\_Dispatch\_type\_** annotations

The Code Analysis tool reports this warning when the right-hand side of an assignment to the **MajorFunction** table has no (valid) **\_Dispatch\_type\_** annotations. The warning can sometimes occur if the right-hand side has a cast that strips off the **\_Dispatch\_type\_** annotation. The right-hand side should be a function of type DRIVER\_DISPATCH type with the appropriate **\_Dispatch\_type\_** annotations.

For more information, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following function declaration elicits this warning, if the function is used in a dispatch routine assignment for a **MajorFunction**.

```
NTSTATUS
DispatchSystemControl (
    PDEVICE_OBJECT  DeviceObject,
    PIRP            Irp
    );
```

The following function declaration, used in the same way, does not elicit this warning.

```
// Function: DispatchSystemControl
// This is an example of a fully annotated declaration.  
// IRP_MJ_SYSTEM_CONTROL is the type of IRP handled by this function.  
// Multiple _Dispatch_type_ lines are acceptable if the function handles more than 1 IRP type.
//
_Dispatch_type_(IRP_MJ_SYSTEM_CONTROL) 
DRIVER_DISPATCH DispatchSystemControl;
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28169%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




