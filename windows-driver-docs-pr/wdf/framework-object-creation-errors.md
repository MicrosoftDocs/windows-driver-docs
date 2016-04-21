---
title: Framework Object Creation Errors
author: windows-driver-content
description: Framework Object Creation Errors
ms.assetid: f5345c88-1c3a-4b32-9c93-c252713f7641
keywords: ["framework objects WDK KMDF , creation errors", "errors WDK KMDF", "errors WDK KMDF , framework object creation"]
---

# Framework Object Creation Errors


When a driver's attempt to create a framework object fails, the object creation method returns an NTSTATUS value that indicates the failure type.

If the driver specifies invalid information in a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure, the framework can return:

<a href="" id="status-wdf-object-attributes-invalid"></a>STATUS\_WDF\_OBJECT\_ATTRIBUTES\_INVALID  
The driver specified an object context name, but the context size is zero.

The driver specified a context size override value, but it did not provide a [**WDF\_OBJECT\_CONTEXT\_TYPE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552407) structure.

The driver specified a **ContextSizeOverride** value in WDF\_OBJECT\_ATTRIBUTES that is less than the **ContextSize** member of the WDF\_OBJECT\_CONTEXT\_TYPE\_INFO structure.

The driver specified an **ExecutionLevel** value in WDF\_OBJECT\_ATTRIBUTES that is not within the valid range of values.

The driver specified an **SynchronizationScope** value in WDF\_OBJECT\_ATTRIBUTES that is not within the valid range of values.

<a href="" id="status-wdf-parent-assignment-not-allowed"></a>STATUS\_WDF\_PARENT\_ASSIGNMENT\_NOT\_ALLOWED  
The driver attempted to assign a parent to the object, but the framework does not allow drivers to assign parents to the object type.

<a href="" id="status-wdf-parent-already-assigned"></a>STATUS\_WDF\_PARENT\_ALREADY\_ASSIGNED  
The driver attempted to assign a parent to an object, but a parent is already assigned to the object.

<a href="" id="status-wdf-parent-is-self"></a>STATUS\_WDF\_PARENT\_IS\_SELF  
The driver attempted to make an object its own parent.

<a href="" id="status-wdf-synchronization-scope-invalid"></a>STATUS\_WDF\_SYNCHRONIZATION\_SCOPE\_INVALID  
The driver specified a [**WDF\_SYNCHRONIZATION\_SCOPE**](https://msdn.microsoft.com/library/windows/hardware/ff552518)-typed value that is invalid for the object type.

<a href="" id="status-wdf-execution-level-invalid"></a>STATUS\_WDF\_EXECUTION\_LEVEL\_INVALID  
The driver specified a [**WDF\_EXECUTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff551310)-typed value that is invalid for the object type.

If the **Size** member of any framework-defined structure does not match the structure's actual size, the framework can return STATUS\_INFO\_LENGTH\_MISMATCH.

If the framework cannot allocate memory for the new object, it can return STATUS\_INSUFFICIENT\_RESOURCES.

Individual object creation methods might also return additional [NTSTATUS values](https://msdn.microsoft.com/library/windows/hardware/ff557697). For more information about each creation method's additional return values, see the method's reference page.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Object%20Creation%20Errors%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




