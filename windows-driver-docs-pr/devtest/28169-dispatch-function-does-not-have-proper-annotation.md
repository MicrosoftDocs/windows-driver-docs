---
title: C28169 warning
description: Warning C28169 The dispatch function does not have any _Dispatch_type_ annotations.
ms.date: 04/20/2017
f1_keywords: 
  - "C28169" 
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

